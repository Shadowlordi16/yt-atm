"""Stage 9: a vertical YouTube Short (1080x1920) from the finished video's cold open.
usage (in the video folder, after finish.sh render):
    python3 ../kit/short.py --title "THEY WERE\\nWINNING"            # cold open, auto length (<= 59 s)
    python3 ../kit/short.py --title "..." --from 12.5 --to 58         # any other moment (seconds in the long video)
Layout (inside YouTube's Shorts safe zones: nothing in the bottom 340 px or the right 140 px):
    ink ground · PAPER EMPIRE kicker + headline on top · the 16:9 video in the middle ·
    word-by-word captions under it · "Full story on the channel" for the last 3 s.
Writes video/renders/short.mp4 and SHORT.txt (title + description)."""
import argparse, glob, json, os, re, subprocess

KIT = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--title", required=True, help="2-6 words, use \\n for a line break")
ap.add_argument("--from", dest="t0", type=float, default=None)
ap.add_argument("--to", dest="t1", type=float, default=None)
ap.add_argument("--name", default="short", help="output name: renders/<name>.mp4 (make several Shorts per video)")
a = ap.parse_args()

V = "video"
src = [f for f in glob.glob(f"{V}/renders/*.mp4") if not os.path.basename(f).startswith(("short", "_"))]
if not src: raise SystemExit("No finished video in video/renders/. Run finish.sh render first.")
src = max(src, key=os.path.getmtime)
tl = json.load(open(f"{V}/timeline.json"))

# scene starts (new kit format has them; older projects: rebuild from composition durations)
scenes = tl["scenes"]
if scenes and isinstance(scenes[0], list):
    t, out = 0.0, []
    for sid, lid in scenes:
        d = float(re.search(r"tl\.to\(\{\}, \{ duration: ([\d.]+) \}", open(f"{V}/compositions/{sid}.html").read()).group(1))
        out.append(dict(sid=sid, line=lid, start=t, dur=d)); t += d
    scenes = out
LEAD = 0.2

# default range: the cold open = every voice scene before the first chapter card, minus the title card
if a.t0 is None:
    a.t0 = 0.0
    first_ch = next((s["start"] for s in scenes if s["sid"].startswith("ch")), 59)
    cold = [s for s in scenes if s["start"] < first_ch and s["line"]]
    if len(cold) > 2: cold = cold[:-1]          # drop the "This is how..." title card
    end = cold[-1]["start"] + cold[-1]["dur"]
    while end > 59 and len(cold) > 1:           # keep it under a minute
        cold = cold[:-1]; end = cold[-1]["start"] + cold[-1]["dur"]
    a.t1 = end
dur = a.t1 - a.t0
END_CARD = 3.0
total = dur + END_CARD

# word-by-word captions (2-3 words per card) from the per-line transcripts
def ts(x):
    h, x = divmod(x, 3600); m, s = divmod(x, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"
events = []
for s in scenes:
    if not s["line"]: continue
    wf = f"{V}/assets/vo/{s['line']}.words.json"
    if not os.path.exists(wf): continue
    words = json.load(open(wf))
    lines = dict(l.split("|", 1) for l in open("lines.txt").read().strip().splitlines())
    script_words = lines.get(s["line"], "").split()
    # captions show the SCRIPT words (correct spelling), timed by the transcript when the counts match
    use = script_words if len(script_words) == len(words) else [w["text"] for w in words]
    for i in range(0, len(words), 3):
        chunk = words[i:i + 3]
        st = s["start"] + LEAD + chunk[0]["start"] - a.t0
        en = s["start"] + LEAD + chunk[-1]["end"] - a.t0
        if en <= 0 or st >= dur: continue
        text = " ".join(use[i:i + 3]).upper().replace("{", "").replace("}", "")
        events.append((max(st, 0), min(en + 0.08, dur), text))
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Cap,League Gothic,118,&H00DFE6E9,&H00DFE6E9,&H00141414,&H00141414,0,0,0,0,100,100,1,0,1,6,0,8,60,140,1330,1",
       "Style: End,League Gothic,96,&H00DFE6E9,&H00DFE6E9,&H00141414,&H00141414,0,0,0,0,100,100,1,0,1,0,0,8,60,140,1330,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
events.sort()
for k in range(len(events) - 1):          # one caption at a time: end each where the next begins
    st, en, text = events[k]
    events[k] = (st, min(en, events[k + 1][0] - 0.01), text)
for st, en, text in events:
    ass.append(f"Dialogue: 0,{ts(st)},{ts(en)},Cap,,0,0,0,,{text}")
ass.append(f"Dialogue: 0,{ts(dur)},{ts(total)},End,,0,0,0,,FULL STORY\\NON THE CHANNEL")
open(f"{V}/renders/{a.name}.ass", "w").write("\n".join(ass) + "\n")

title_lines = a.title.replace("\\n", "\n").upper().split("\n")
fonts = f"{KIT}/fonts"
draw = [f"drawtext=fontfile={fonts}/Inter.ttf:text='PAPER EMPIRE':fontsize=40:fontcolor=0xE9E6DF:x=60:y=250"]
for k, line in enumerate(title_lines[:3]):
    safe = line.replace(":", r"\:").replace("'", "’")
    draw.append(f"drawtext=fontfile={fonts}/LeagueGothic.ttf:text='{safe}':fontsize=150:fontcolor=0xE9E6DF:x=56:y={310 + k * 132}")
vf = (f"[0:v]trim=start={a.t0}:end={a.t1},setpts=PTS-STARTPTS,scale=1080:608,tpad=stop_mode=clone:stop_duration={END_CARD}[mid];"
      f"color=c=0x141414:s=1080x1920:d={total}[bg];"
      f"[bg][mid]overlay=0:{310 + len(title_lines[:3]) * 132 + 70}:shortest=1[v1];"
      f"[v1]{','.join(draw)},subtitles={V}/renders/{a.name}.ass:fontsdir={fonts}[v]")
af = f"[0:a]atrim=start={a.t0}:end={a.t1},asetpts=PTS-STARTPTS,afade=t=out:st={dur - 0.6}:d=0.6,apad=pad_dur={END_CARD}[a]"
out = f"{V}/renders/{a.name}.mp4"
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", vf + ";" + af, "-map", "[v]", "-map", "[a]",
                    "-t", f"{total}", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out], capture_output=True, text=True)
if r.returncode: raise SystemExit(r.stderr[-1500:])
os.remove(f"{V}/renders/{a.name}.ass")
open("SHORT.txt" if a.name == "short" else f"SHORT-{a.name}.txt", "w").write(
    f"TITLE (≤ 100 chars, end with #shorts):\n{os.path.basename(os.getcwd()).replace('-', ' ').title()}: {' '.join(title_lines).capitalize()} #shorts\n\n"
    "DESCRIPTION:\nThe full story is on the channel: Paper Empire.\n\n#shorts #business #history\n\n"
    "AFTER UPLOAD: in YouTube Studio, set 'Related video' on this Short to the full video.\n")
print(f"Short: {out} · {total:.1f}s from {src} [{a.t0:.1f}s → {a.t1:.1f}s] · {len(events)} caption cards · see SHORT.txt")
