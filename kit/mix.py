"""Stage 6: music bed + sound effects -> video/assets/audio/bed_fx.wav
Music comes from ~/Videos/yt-atm/music/<mood>_<name>.mp3 (YouTube Audio Library tracks).
- each section (cold open, every chapter, ending) gets a mood and a track; sections crossfade
- the music ducks under the voice (lower while Adam speaks, back up in the pauses)
- the music cuts out under scenes built with punch=True and slams back after
- sound effects land at the cue times the scenes wrote
usage (in video/): python3 ../../kit/mix.py"""
import glob, json, os, re, subprocess, wave
import numpy as np

SR = 48000
KIT = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(os.path.dirname(KIT), "music")
tlj = json.load(open("timeline.json"))
TOTAL = tlj["total"]
N = int(TOTAL * SR) + SR
scenes = tlj["scenes"]
if scenes and isinstance(scenes[0], list):          # older project format
    t, out = 0.0, []
    for sid, lid in scenes:
        d = float(re.search(r"tl\.to\(\{\}, \{ duration: ([\d.]+) \}", open(f"compositions/{sid}.html").read()).group(1))
        out.append(dict(sid=sid, line=lid, start=t, dur=d)); t += d
    scenes = out
starts = {s["sid"]: (s["start"], s["start"] + s["dur"]) for s in scenes}


def load(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)


# ---------------- music ----------------
tracks = {}
for f in sorted(glob.glob(f"{MUSIC}/*.mp3") + glob.glob(f"{MUSIC}/*.wav")):
    mood = os.path.basename(f).split("_", 1)[0]
    tracks.setdefault(mood, []).append(f)
bed = np.zeros((N, 2))
heads = [scenes[0]["sid"]] + tlj.get("chapters", [])
ending = next((s["sid"] for s in reversed(scenes) if s["line"] and not s["sid"].startswith("ch")), None)
# mood plan: cold open dark · rises calm · middle drive · late chapters dark · last chapter sombre
plan = ["dark", "calm", "calm", "drive", "dark", "sombre", "sombre", "dark"]
FALLBACK = {"sombre": ["dark", "calm"], "drive": ["dark", "calm"], "calm": ["dark", "drive"], "dark": ["drive", "calm"]}
used = {}
if tracks:
    XF = 1.5
    for k, sid in enumerate(heads):
        a = starts[sid][0]
        b = starts[heads[k + 1]][0] if k + 1 < len(heads) else TOTAL
        mood = plan[min(k, len(plan) - 1)]
        pool = tracks.get(mood) or next((tracks[m] for m in FALLBACK[mood] if m in tracks), None)
        n = used.get(mood, 0); used[mood] = n + 1
        f = pool[n % len(pool)]
        x = load(f)
        x /= (np.sqrt(np.mean(x ** 2)) + 1e-9) * 10        # every track to the same loudness
        seg_len = int((b - a + XF) * SR)
        offs = int(min(8.0, len(x) / SR / 4) * SR)         # skip quiet intros
        loop = np.concatenate([x[offs:]] * (seg_len // max(len(x) - offs, 1) + 2))[:seg_len]
        env = np.ones(seg_len)
        fi = int(XF * SR)
        fin = fi if k else int(0.4 * SR)
        env[:fin] = np.linspace(0, 1, fin)
        env[-fi:] = np.linspace(1, 0, fi)
        i0 = int(a * SR)
        m = min(seg_len, N - i0)
        bed[i0:i0 + m] += loop[:m] * env[:m, None]
        print(f"  {sid:>5} {a:6.1f}s  {mood:<6} {os.path.basename(f)}")
else:
    print("  no tracks in", MUSIC, "- music bed is silent (add YouTube Audio Library tracks)")

# ducking: quieter under the voice, up in the gaps (voice times from the scene list)
LEAD = 0.2
speech = np.zeros(N)
for s in scenes:
    if not s["line"]: continue
    wf = f"assets/vo/{s['line']}.wav"
    if not os.path.exists(wf): continue
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", wf], capture_output=True, text=True).stdout)
    i0 = int((s["start"] + LEAD) * SR); speech[i0:i0 + int(d * SR)] = 1
k = int(0.35 * SR)
c = np.concatenate([[0], np.cumsum(speech)]); idx = np.arange(N)
smooth = (c[np.minimum(idx + k // 2, N)] - c[np.maximum(idx - k // 2, 0)]) / k   # moving average, O(N)
gain = 0.30 - 0.18 * smooth            # ~0.30 in pauses, ~0.12 under the voice
for sid in tlj.get("punch", []):        # cut out under punchlines
    a, b = starts[sid]; ia, ib = int(a * SR), int(b * SR); f = int(0.04 * SR)
    gain[ia:ib] = 0; gain[ia:ia + f] = np.linspace(gain[ia], 0, f)
end = int(TOTAL * SR)
fo = int(2.5 * SR); gain[end - fo:end] *= np.linspace(1, 0, fo); gain[end:] = 0
bed *= gain[:, None]

# ---------------- sound effects ----------------
files = {"click": [f"{KIT}/sfx/click_{k}.wav" for k in (1, 2, 3, 4)], "train": [f"{KIT}/sfx/clicktrain_1.wav"],
         "impact": [f"{KIT}/sfx/impact_2.wav"], "pop": [f"{KIT}/sfx/tick.wav"]}
cache, rot = {}, {}
for kind, at, vol in tlj["cues"]:
    lst = files[kind]; rot[kind] = rot.get(kind, -1) + 1; f = lst[rot[kind] % len(lst)]
    if f not in cache: cache[f] = load(f)
    x = cache[f]; i = int((at + 1 / 30) * SR); n = min(len(x), N - i)
    if n > 0: bed[i:i + n] += x[:n] * vol * (0.6 if kind == "impact" else 1.0)
pk = np.max(np.abs(bed))
if pk > 0.95: bed *= 0.95 / pk
os.makedirs("assets/audio", exist_ok=True)
w = wave.open("assets/audio/bed_fx.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((bed[:end] * 32767).astype("<i2").tobytes()); w.close()
print(f"mix ok {TOTAL:.1f}s · {len(tlj['cues'])} sound cues · music: {sum(len(v) for v in tracks.values())} tracks")
