# Music bed (synthesized, sectioned by chapter, cut out under punchlines) + sound effects at cue times -> assets/audio/bed_fx.wav
import json, wave, numpy as np, subprocess
SR = 48000
tlj = json.load(open("timeline.json")); TOTAL = tlj["total"]; N = int(TOTAL * SR) + SR
L = np.zeros(N); R = np.zeros(N)
starts = {}; t = 0
import re
for sid, lid in tlj["scenes"]:
    d = float(re.search(r'tl\.to\(\{\}, \{ duration: ([\d.]+) \}', open(f"compositions/{sid}.html").read()).group(1))
    starts[sid] = (t, t + d); t += d
def add(sig, at, g=1.0, pan=0.0):
    i = int(at * SR); sig = sig[:max(0, N - i)]
    L[i:i + len(sig)] += sig * g * (1 - max(0, pan)); R[i:i + len(sig)] += sig * g * (1 + min(0, pan))
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
def piano(m, d=2.6):
    n = int(d * SR); x = np.arange(n) / SR; f = hz(m)
    return sum(a * np.sin(2 * np.pi * f * k * x) for k, a in [(1, 1), (2, .35), (3, .12), (4, .05)]) * np.minimum(1, x / .006) * np.exp(-x * 2.0)
def drone(m, d):
    n = int(d * SR); x = np.arange(n) / SR; f = hz(m)
    return (np.sin(2*np.pi*f*x) + .5*np.sin(2*np.pi*f*2.003*x) + .25*np.sin(2*np.pi*f*1.5*x)) * np.minimum(1, x/1.2) * np.minimum(1, np.maximum(0, d-x)/1.2)
def pulse():
    n = int(.35 * SR); x = np.arange(n) / SR
    return np.sin(2 * np.pi * (48 + 40 * np.exp(-x * 25)) * x) * np.exp(-x * 9)
# sections: (start scene, progression, pulse density, piano gain)
MIN = [(45, [57, 60, 64]), (41, [57, 60, 65]), (48, [55, 60, 64]), (43, [55, 59, 62])]   # Am F C G
MAJ = [(48, [55, 60, 64]), (43, [55, 59, 62]), (45, [57, 60, 64]), (41, [57, 60, 65])]   # C G Am F
secs = [("l00", MIN, 2, .10), ("ch1", MAJ, 1, .12), ("ch2", MIN, 1, .11), ("ch3", MAJ, 2, .12), ("ch4", MIN, 2, .10), ("ch5", MIN, 0, .09), ("l57", MIN, 0, .10)]
B = 60 / 74; bar = 4 * B
order = [s for s, _ in tlj["scenes"]]
for k, (sid, prog, pd, pg) in enumerate(secs):
    a = starts[sid][0]; b = starts[secs[k + 1][0]][0] if k + 1 < len(secs) else TOTAL
    t = a; i = 0
    while t < b - 0.5:
        root, notes = prog[i % 4]; seg = min(2 * bar, b - t)
        add(drone(root, seg + 1.2), t, .09)
        for j, bb in enumerate([0, 1.5, 3, 4.5, 6]):
            if t + bb * B < b - 0.3: add(piano(notes[j % 3] + (12 if j == 3 else 0)), t + bb * B, pg, -.3 if j % 2 else .3)
        if pd:
            for q in range(8):
                if q % (2 if pd == 1 else 1) == 0 and t + q * B < b: add(pulse(), t + q * B, .2 if q % 4 == 0 else .11)
        t += 2 * bar; i += 1
# cut the bed out under punchlines; it slams back at the next scene
gain = np.ones(N)
for sid in ("l03", "l07", "l60"):
    a, b = starts[sid]; ia, ib = int(a * SR), int(b * SR); f = int(.04 * SR)
    gain[ia:ib] = 0; gain[ia:ia + f] = np.linspace(1, 0, f)
m = np.max(np.abs(np.r_[L, R])) or 1; L *= gain / m * 0.5; R *= gain / m * 0.5
fo = int(2.5 * SR); end = int(TOTAL * SR); L[end - fo:end] *= np.linspace(1, 0, fo); R[end - fo:end] *= np.linspace(1, 0, fo); L[end:] = 0; R[end:] = 0
# sound effects
KIT = "/home/ak-david-dev/.claude/skills/editor-v1/sfx"
files = {"click": [f"{KIT}/ev1kit/click_{k}.wav" for k in (1, 2, 3, 4)], "train": [f"{KIT}/ev1kit/clicktrain_1.wav"],
         "impact": [f"{KIT}/ev1kit/impact_1.wav", f"{KIT}/ev1kit/impact_2.wav"], "pop": [f"{KIT}/ev1/tick.wav"]}
def load(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32).reshape(-1, 2); return a
cache = {}; rot = {}
for kind, at, vol in tlj["cues"]:
    lst = files[kind]; rot[kind] = rot.get(kind, -1) + 1; f = lst[rot[kind] % len(lst)]
    if f not in cache: cache[f] = load(f)
    a = cache[f]; i = int((at + 1 / 30) * SR); n = min(len(a), N - i)
    if n > 0: L[i:i + n] += a[:n, 0] * vol; R[i:i + n] += a[:n, 1] * vol
pk = max(np.max(np.abs(L)), np.max(np.abs(R)))
if pk > 0.95: L *= 0.95 / pk; R *= 0.95 / pk
w = wave.open("assets/audio/bed_fx.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.c_[L[:end], R[:end]] * 32767).astype("<i2").tobytes()); w.close()
print("mix ok", round(TOTAL, 1), "s,", len(tlj["cues"]), "cues")
