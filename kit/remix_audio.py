"""Swap a finished video's sound for a fresh mix (voice + music + effects) WITHOUT re-rendering the picture.
Use after changing the music or sound effects.   usage (in video/): python3 ../../kit/remix_audio.py renders/<name>.mp4
Runs mix.py first, rebuilds the full soundtrack at -14 LUFS, copies the picture untouched, replaces the file in place."""
import json, os, re, subprocess, sys

KIT = os.path.dirname(os.path.abspath(__file__))
video = sys.argv[1]
subprocess.run([sys.executable, f"{KIT}/mix.py"], check=True)
tl = json.load(open("timeline.json"))
scenes = tl["scenes"]
if scenes and isinstance(scenes[0], list):
    t, out = 0.0, []
    for sid, lid in scenes:
        d = float(re.search(r"tl\.to\(\{\}, \{ duration: ([\d.]+) \}", open(f"compositions/{sid}.html").read()).group(1))
        out.append(dict(sid=sid, line=lid, start=t, dur=d)); t += d
    scenes = out
inputs, flt, n = ["-i", "assets/audio/bed_fx.wav"], [], 1
for s in scenes:
    if s["line"] and os.path.exists(f"assets/vo/{s['line']}.wav"):
        ms = int((s["start"] + 0.2) * 1000)
        inputs += ["-i", f"assets/vo/{s['line']}.wav"]
        flt.append(f"[{n}:a]adelay={ms}|{ms},aformat=channel_layouts=stereo[v{n}]"); n += 1
graph = ";".join(flt) + ";[0:a]" + "".join(f"[v{i}]" for i in range(1, n)) + f"amix=inputs={n}:normalize=0,atrim=0:{tl['total']},loudnorm=I=-14:TP=-1.5:LRA=11[a]"
tmp_audio = "renders/_soundtrack.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", graph, "-map", "[a]", "-ar", "48000", tmp_audio], check=True)
tmp = video + ".tmp.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", tmp_audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                "-c:a", "aac", "-b:a", "192k", "-shortest", tmp], check=True)
os.replace(tmp, video); os.remove(tmp_audio)
r = subprocess.run(["ffmpeg", "-nostats", "-i", video, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
loud = re.search(r"I:\s+(-?[\d.]+) LUFS", r.split("Summary")[-1]); peak = re.search(r"Peak:\s+(-?[\d.]+)", r.split("Summary")[-1])
print(f"New sound in {video}: {loud.group(1) if loud else '?'} LUFS, peak {peak.group(1) if peak else '?'} dBFS (picture untouched)")
