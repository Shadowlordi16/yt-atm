"""Quality gate. finish.sh runs it before check AND (with --render) before render; a FAIL stops the pipeline.
It catches the shortcuts a model can take while still "following the commands".
Gaming this gate (placeholder images, counters appended to make lines "different", touching REVIEWED
without looking) is the worst failure there is: the whole video gets thrown away. If you are blocked, STOP and say so.
usage (in video/): python3 ../../kit/gate.py [--render]"""
import glob, json, os, re, sys
from collections import Counter

fails, warns = [], []
root = ".."
render = "--render" in sys.argv
script = open(f"{root}/SCRIPT.md").read()
strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()
nodig = lambda s: re.sub(r"\d+", "#", s.lower())

# 1. The owner approved the script (they add a line:  APPROVED: <name> <date>)
if not re.search(r"^APPROVED:", script, re.M):
    fails.append("SCRIPT.md has no 'APPROVED: <name> <date>' line. The owner must approve the script before voice/build/render.")

# 2. Real photos, not the template or placeholders
try:
    photos = {k: v for k, v in json.load(open(f"{root}/photos.json")).items() if not k.startswith("_")}
except Exception:
    photos = {}
fake = re.compile(r"example|texture|placeholder|blank|dummy|solid colou?r", re.I)
bad = [f"{k}: {v}" for k, v in photos.items() if fake.search(str(v)) or re.match(r"(paper|texture|bg|blank|placeholder)_?\d*$", k, re.I)]
if bad:
    fails.append(f"photos.json has template/placeholder entries ({len(bad)}), e.g. {bad[0]}. Use real photos of the people, places and products named in the script (AGENTS.md stage 4).")
credits = open(f"{root}/CREDITS.md").read() if os.path.exists(f"{root}/CREDITS.md") else ""
n_cred = len(re.findall(r"^- .+ by .+, .+", credits, re.M))
if n_cred < 12:
    fails.append(f"CREDITS.md lists {n_cred} credited photos (need >= 12, written by photos.py).")
imgs = sorted(glob.glob("assets/img/*.jpg") + glob.glob("assets/img/*.png"))
comp = "".join(open(f).read() for f in sorted(glob.glob("compositions/*.html")))
used = set(re.findall(r"assets/img/([\w-]+)\.(?:jpg|png)", comp))
if len(imgs) < 15:
    fails.append(f"only {len(imgs)} treated photos in assets/img (need >= 15).")
if len(used) < 12:
    fails.append(f"only {len(used)} different photos used on screen (need >= 12).")
# a photo has detail; a generated blank/texture does not
try:
    from PIL import Image, ImageStat
    flat = []
    for p in imgs:
        g = Image.open(p).convert("L").resize((160, 90))
        if ImageStat.Stat(g).stddev[0] < 18:
            flat.append(os.path.basename(p))
    if len(flat) > max(2, len(imgs) // 5):
        fails.append(f"{len(flat)} images in assets/img are nearly blank (no detail), e.g. {flat[:3]}. These are placeholders, not photos.")
except ImportError:
    warns.append("PIL not installed: could not check images for blanks.")

# 3. On-screen text must not be the narration pasted onto the screen
lines = dict(l.split("|", 1) for l in open(f"{root}/lines.txt").read().strip().splitlines())
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower())
pasted = 0
heads, kicks, numeric = [], [], 0
num_words = re.compile(r"\d|hundred|thousand|million|billion|percent", re.I)
num_lines = 0
for f in sorted(glob.glob("compositions/l*.html")):
    lid = os.path.basename(f)[:-5].upper()
    html = open(f).read()
    shown_raw = [strip(t) for t in re.findall(r'class="lg[^"]*"[^>]*>(.*?)</div>', html, re.S)]
    heads += shown_raw
    kicks += [strip(t) for t in re.findall(r'class="kick[^"]*"[^>]*>(.*?)</div>', html, re.S)]
    if lid not in lines: continue
    shown = [norm(s) for s in shown_raw]
    words = norm(lines[lid]).split()
    starts = {" ".join(words[i:i + 5]) for i in range(len(words) - 4)}
    if any(any(st in s for st in starts) for s in shown):
        pasted += 1
    if num_words.search(lines[lid]):
        num_lines += 1
        if re.search(r"\d", strip(html.split("<script")[0]).replace("Source:", "")) or "count(" in html:
            numeric += 1
n_line = len(glob.glob("compositions/l*.html")) or 1
if pasted > 0.15 * n_line:
    (fails if pasted > 0.30 * n_line else warns).append(f"{pasted} scenes show 5+ words copied from their own narration line. The screen must SHOW the idea (a number, a name, a photo), not repeat the sentence.")

# 3b. Each scene shows its own idea: no headline/kicker repeated across the video
for name, items in (("headline", heads), ("kicker", kicks)):
    if not items: continue
    c = Counter(nodig(x) for x in items if re.search(r"[a-z]", nodig(x)))   # a bare date/number label is fine
    if not c: continue
    top, k = c.most_common(1)[0]
    if k > max(3, len(items) // 10):
        fails.append(f"the same {name} '{top}' appears {k} times. Every scene must show what ITS line is about.")
    if len(c) < 0.5 * len(items):
        fails.append(f"only {len(c)} different {name}s across {len(items)} (numbers ignored): the scenes are copies.")
if len(heads) < 0.5 * n_line:
    fails.append(f"only {len(heads)} headlines for {n_line} scenes: most scenes show nothing.")
if num_lines and numeric < 0.6 * num_lines:
    fails.append(f"only {numeric} of {num_lines} lines that say a number/date show one on screen. Show the figure (count, stamp, date).")

# 4. Layout variety: not every headline at the same spot and size
pos = re.findall(r'class="lg[^"]*"[^>]*style="[^"]*left:(\d+)px;top:(\d+)px;font-size:(\d+)px', comp)
if pos and len(set(pos)) < max(8, len(pos) // 6):
    fails.append(f"headlines use only {len(set(pos))} distinct position/size combinations across {len(pos)}: every scene looks the same.")

# 5. Sources are real and specific, not one line pasted everywhere (numbers ignored, so "reference 1..60" doesn't count)
srcs = [strip(s) for s in re.findall(r'class="src[^"]*"[^>]*>([^<]+)<', comp)]
if srcs and len({nodig(s) for s in srcs}) < 6:
    fails.append(f"only {len({nodig(s) for s in srcs})} different source lines (numbers ignored): name the actual source on each fact.")
fakesrc = [s for s in srcs if re.search(r"editorial|narration|paper empire|reference \d", s, re.I)]
if fakesrc:
    fails.append(f"{len(fakesrc)} source lines are not a real source, e.g. '{fakesrc[0]}'. A source names the publication from SOURCES.md; no source = no s.source().")

# 6. Devices beyond plain text
devices = sum(comp.count(k) for k in ("count(", "stamp", "-ph", "tw", "-dg", "card", "sheet"))
if devices < 25:
    warns.append(f"few visual devices ({devices}): use counts, stamps, photos, dots, sheets (kit/KIT.md).")

# 7. Before render: the stills were really made from THIS build, and they don't all look the same
if render:
    rv = "snapshots/review"
    frames = sorted(glob.glob(f"{rv}/frame-*.png"))
    sheets = glob.glob(f"{rv}/contact-sheet-*.jpg")
    newest_build = max(os.path.getmtime(f) for f in glob.glob("compositions/*.html") + ["index.html"])
    if not sheets or len(frames) < 0.9 * n_line:
        fails.append(f"{len(frames)} stills for {n_line} scenes in {rv}/. Run 'finish.sh check' to make them, then LOOK at them.")
    elif min(os.path.getmtime(f) for f in frames) < newest_build:
        fails.append("the stills are older than the current build. Run 'finish.sh check' again and look at the new stills.")
    if os.path.exists(f"{rv}/REVIEWED") and frames and os.path.getmtime(f"{rv}/REVIEWED") < max(os.path.getmtime(f) for f in frames):
        fails.append("REVIEWED was touched before the latest stills were made.")
    try:
        from PIL import Image, ImageChops, ImageStat
        sm = [Image.open(f).convert("L").resize((96, 54)) for f in frames]
        diffs = sorted(ImageStat.Stat(ImageChops.difference(a, b)).mean[0] for a, b in zip(sm, sm[1:]))
        if diffs and diffs[len(diffs) // 2] < 6:
            fails.append(f"consecutive stills barely differ (median difference {diffs[len(diffs)//2]:.1f}): the video is the same frame over and over.")
        plain = sum(ImageStat.Stat(s).stddev[0] < 25 for s in sm)
        if frames and plain > 0.4 * len(sm):
            fails.append(f"{plain} of {len(sm)} stills are mostly empty paper. Each scene needs a photo or a big designed element.")
    except ImportError:
        pass

for w in warns: print("WARN:", w)
for f in fails: print("FAIL:", f)
print("GATE", "PASSED" if not fails else "FAILED - fix the FAIL lines before going on")
sys.exit(1 if fails else 0)
