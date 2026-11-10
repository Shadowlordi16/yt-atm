"""Stage 3b (fast): record every line with Kokoro and get word timings, loading each model ONCE.
Same output as voice.sh (video/assets/vo/Lxx.wav + Lxx.words.json), several times faster.
usage (in the video folder): ~/.venvs/kokoro/bin/python ../kit/voice_fast.py   [env VOICE=am_adam SPEED=0.9]
Lines that already have both files are skipped (so it also re-records only changed lines after relines.py)."""
import fcntl, json, os, re, subprocess, sys, time
import numpy as np

VOICE, SPEED = os.environ.get("VOICE", "am_adam"), float(os.environ.get("SPEED", "0.9"))
if not re.search(r"^APPROVED:", open("SCRIPT.md").read(), re.M):
    sys.exit("Refused: SCRIPT.md has no APPROVED: line. The owner approves the script first.")
lock = open("/tmp/paper_empire_render.lock", "w")
try:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except OSError:
    sys.exit("A render or another narration is running. Wait for it.")
VO = "video/assets/vo"
os.makedirs(VO, exist_ok=True)
lines = [l.split("|", 1) for l in open("lines.txt").read().strip().splitlines()]
todo = [(i, t) for i, t in lines if not (os.path.exists(f"{VO}/{i}.wav") and os.path.exists(f"{VO}/{i}.words.json"))]
print(f"{len(todo)} of {len(lines)} lines to record")
if not todo: sys.exit(0)

# 1) voice: one Kokoro load for every line
import soundfile as sf
from kokoro_onnx import Kokoro
cache = os.path.expanduser("~/.cache/hyperframes/tts")
k = Kokoro(f"{cache}/models/kokoro-v1.0.onnx", f"{cache}/voices/voices-v1.0.bin")
lang = "en-gb" if VOICE.startswith("b") else "en-us"
t0 = time.time()
for i, text in todo:
    if os.path.exists(f"{VO}/{i}.wav") and os.path.getsize(f"{VO}/{i}.wav") > 1000: continue
    audio, sr = k.create(text, voice=VOICE, speed=SPEED, lang=lang)
    sf.write(f"{VO}/{i}.wav", audio, sr)
print(f"voice: {len(todo)} lines in {time.time() - t0:.0f}s")

# 2) word timings: one Whisper load for every line (runs in the ASR environment)
asr = os.path.expanduser("~/.venvs/asr/bin/python")
code = r'''
import json, subprocess, sys, numpy as np
from faster_whisper import WhisperModel
import os
m = WhisperModel(os.environ.get("WHISPER_MODEL", "base.en"), device="cpu", compute_type="int8", cpu_threads=4)   # small model: we only need WHEN words are said
for f in sys.argv[1:]:
    raw = subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar","16000","-f","f32le","-"], capture_output=True).stdout
    segs, _ = m.transcribe(np.frombuffer(raw, np.float32), language="en", word_timestamps=True)
    words = [dict(id=f"w{n}", text=w.word.strip(), start=round(w.start, 3), end=round(w.end, 3))
             for n, w in enumerate(x for s in segs for x in s.words)]
    json.dump(words, open(f.replace(".wav", ".words.json"), "w"), indent=1)
'''
t0 = time.time()
need = [f"{VO}/{i}.wav" for i, _ in lines if os.path.exists(f"{VO}/{i}.wav") and not os.path.exists(f"{VO}/{i}.words.json")]
subprocess.run([asr, "-c", code, *need], check=True)
print(f"timings: {len(todo)} lines in {time.time() - t0:.0f}s")
