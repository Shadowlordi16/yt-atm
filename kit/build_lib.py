"""Shared build helpers for every Paper Empire video.

A video's build.py only lists scenes. Everything else (timing from the voice, cue lookup,
chapter cards, portraits, index.html, the sound cue list) lives here.

    import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
    from build_lib import *
    s, c = line_scene("First words of the voice line")      # one scene per voice line
    s.text("Headline", 186, 300, 200, t=c("word"))           # lands on the spoken word
    ...
    finish()                                                 # writes compositions/, index.html, timeline.json
"""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import Scene, CROWN_SVG, F   # noqa: F401  (re-exported for build.py)

LEAD = 0.2      # the voice starts this far into its scene
GAP = 0.7       # silence after each line
os.makedirs("compositions", exist_ok=True)
LINES = [l.split("|", 1) for l in open("../lines.txt").read().strip().splitlines()]
TEXT = {k: v for k, v in LINES}
INT = "v => Math.round(v).toLocaleString('en-US')"
CC = "Photo: Wikimedia Commons (credits in description)"

timeline = []           # [(Scene, voice line id or None)]
CHAPTERS = []           # scene ids of chapter cards (the music changes there)
PUNCH = []              # scene ids where the music cuts out (punchlines)


def money(prefix="$", suffix=""):
    return f"v => '{prefix}' + Math.round(v).toLocaleString('en-US') + '{suffix}'"


def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def L(prefix):
    """Find a voice line id by the first words of its text (as written in SCRIPT.md)."""
    for k, v in LINES:
        if v.startswith(prefix):
            return k
    raise KeyError(f"No line starts with: {prefix!r}")


def _norm(x):
    return re.sub(r"[^\w$.%-]", "", x.lower())


class Cue:
    """c("word") -> scene time (s) when that word is spoken. Use "a|b" for alternatives:
    the transcript writes numbers as digits, so c("fifty|50|$50") is safer than c("fifty").
    nth picks the n-th occurrence; off shifts the time."""
    def __init__(self, lid):
        self.lid = lid
        self.words = json.load(open(f"assets/vo/{lid}.words.json"))
        self.vo = dur(f"assets/vo/{lid}.wav")

    def __call__(self, word, nth=1, off=0.0):
        hits = []
        for w in [_norm(q) for q in word.split("|")]:
            hits = [x for x in self.words if _norm(x["text"]).startswith(w)]
            if len(hits) >= nth:
                break
        if len(hits) < nth:
            raise KeyError(f"{self.lid}: {word!r} #{nth} not heard. Transcript: " + " ".join(x["text"] for x in self.words))
        return round(LEAD + hits[nth - 1]["start"] + off, 3)

    def end(self, off=0.0):
        return round(LEAD + self.vo + off, 3)


def line_scene(prefix, ground="paper", hold=0.0, punch=False):
    """One scene for one voice line. ground: paper | ink | none. hold adds silence after.
    punch=True cuts the music out under this line."""
    lid = L(prefix)
    c = Cue(lid)
    s = Scene(lid.lower(), LEAD + c.vo + GAP + hold, ground)
    timeline.append((s, lid))
    if punch:
        PUNCH.append(s.sid)
    return s, c


def card_scene(sid, d, ground="ink"):
    s = Scene(sid, d, ground)
    timeline.append((s, None))
    return s


def chapter(sid, title, imgs, d=2.6):
    """Chapter card: 3x3 tile-flash of 9 photos, then the title on an ink band."""
    s = card_scene(sid, d, "ink")
    tend = s.tiles(imgs, 0.05)
    s.raw(f'<div id="{sid}-band" class="o0" style="position:absolute;left:0;top:380px;width:1920px;height:320px;background:#141414"></div>')
    s.js.append(f"on('#{sid}-band', {tend + 0.15:.3f});")
    size = min(230, int(1530 / (0.40 * max(len(title), 1))))   # long titles shrink to fit the band
    s.text(title, 192, 545 - int(size * 0.5), size, color="np", t=tend + 0.2, d=0.35)
    CHAPTERS.append(sid)   # no boom on chapter cards (owner: it sounded bad)
    return s


def portrait(s, img, name, role, t, pos="50% 22%", until=None):
    """Person on the right 55% of the frame, name + role on the paper at left."""
    s.raw(f'<div id="{s.sid}-pw" class="o0" style="position:absolute;left:860px;top:0;width:1060px;height:1080px;overflow:hidden">'
          f'<img id="{s.sid}-pi" src="assets/img/{img}.jpg" style="width:1060px;height:1080px;object-fit:cover;object-position:{pos}" alt=""></div>',
          js=f"on('#{s.sid}-pw', {t:.3f}); push('#{s.sid}-pi', {t:.3f}, {s.dur - t:.3f}, 1, 1.05);")
    k = s.el(role, "left:192px;top:600px;font-size:" + str(min(46, int(640 / (0.68 * max(len(role), 1))))) + "px", "kick grey", t + 0.15)
    n = s.text(name, 186, 660, min(170, int(640 / (0.40 * max(len(name), 1)))), t=t + 0.1)   # auto-fit beside the photo
    s.click(t)
    if until is not None:
        s.js.append(f"off('#{s.sid}-pw', {until:.3f}); off('#{k}', {until:.3f}); off('#{n}', {until:.3f});")


def photo_card(s, img, x, y, w, h, t, rot=-1.5, fit="contain"):
    """A real photo (a phone, a document, an advert) on a paper card that slides up into place, with a click."""
    cid = s.i("pc")
    s.raw(f'<div id="{cid}" class="o0" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#F7F5F0;box-shadow:0 14px 30px rgba(0,0,0,.22);overflow:hidden">'
          f'<img src="assets/img/{img}.jpg" style="width:100%;height:100%;object-fit:{fit}" alt=""></div>',
          js=f"tl.fromTo('#{cid}', {{ opacity: 1, y: 70, rotation: {rot * 2} }}, {{ y: 0, rotation: {rot}, duration: 0.5, ease: 'expo.out' }}, {t:.3f});")
    s.click(t)
    return cid


def end_card(prefix, next_title, next_line):
    """Animated crown + PAPER EMPIRE + the next video teaser. Use on the last voice line."""
    s, c = line_scene(prefix, "ink", hold=2.6)
    s.raw(f'<div id="{s.sid}-crown" style="position:absolute;left:810px;top:150px">{CROWN_SVG.format(s=300)}</div>',
          js=f"tl.fromTo('#{s.sid}-crown .cf', {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: 'expo.out', stagger: 0.08 }}, 0.2); "
             f"tl.fromTo('#{s.sid}-crown .cb', {{ scaleX: 0 }}, {{ scaleX: 1, transformOrigin: '50% 50%', duration: 0.4, ease: 'power2.inOut' }}, 0.5); "
             f"tl.fromTo('#{s.sid}-crown .cr', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, 1.0);")
    s.click(1.0, "impact", 0.35)
    s.text("Paper Empire", 0, 500, 200, color="np", t=0.6, extra="width:1920px;text-align:center")
    s.el(f"Next: {next_title}", "left:0;top:720px;width:1920px;text-align:center", "kick np", c("next"))
    s.el(next_line, "left:0;top:780px;width:1920px;text-align:center;font:400 40px Inter", "np", c("next", off=0.6))
    return s, c


def finish():
    """Write every scene, index.html and timeline.json (read by mix.py)."""
    import shutil; shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "gsap.min.js"), "assets/gsap.min.js")   # no internet needed at render
    for sc, _ in timeline:
        sc.write("compositions")
    t = 0.0
    hosts, vos, cues, scenes = [], [], [], []
    for sc, lid in timeline:
        hosts.append(f'      <div id="{sc.sid}" data-composition-id="{sc.sid}" data-composition-src="compositions/{sc.sid}.html" data-start="{t:.3f}" data-duration="{sc.dur}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>')
        if lid:
            vos.append(f'      <audio id="vo-{lid}" class="clip" src="assets/vo/{lid}.wav" data-start="{t + LEAD:.3f}" data-duration="{dur(f"assets/vo/{lid}.wav") - 0.01:.3f}" data-track-index="2" data-volume="1"></audio>')
        for kind, st, vol in sc.sfx:
            cues.append((kind, round(t + st, 3), vol))
        scenes.append(dict(sid=sc.sid, line=lid, start=round(t, 3), dur=sc.dur))
        t += sc.dur
    total = round(t, 3)
    json.dump({"total": total, "cues": cues, "scenes": scenes, "chapters": CHAPTERS, "punch": PUNCH},
              open("timeline.json", "w"), indent=1)
    open("index.html", "w").write(f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/gsap.min.js"></script>
    <style>* {{ margin: 0; padding: 0; box-sizing: border-box; }} html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #141414; }}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080">
{chr(10).join(hosts)}
{chr(10).join(vos)}
      <audio id="mix-fx" class="clip" src="assets/audio/bed_fx.wav" data-start="0" data-duration="{total}" data-track-index="3" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
''')
    print(f"scenes {len(timeline)} · total {total}s = {total // 60:.0f}:{total % 60:04.1f} · sound cues {len(cues)}")
    if total < 480:
        print("WARNING: under 8:00. Mid-roll ads need 8 minutes. Add sourced lines or longer holds.")
