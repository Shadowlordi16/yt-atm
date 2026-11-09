# Scenes for this video. One block per voice line, in script order. Run: python3 build.py
# Device reference: ../../kit/KIT.md   ·   Look at what the transcriber heard: python3 ../../kit/words.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *

# ---------- COLD OPEN ----------
s, c = line_scene("First words of line L00", "ink")          # ground: "paper" | "ink"
s.photos([("hq", 0)], rate=0.015)                             # full-bleed photo with a slow push
s.raw('<div class="fill" style="background:rgba(20,20,20,.55)"></div>')   # darken so light type reads
s.kicker("City · 2000", 192, 330, c("city"), "np")            # small caps label, lands on "city"
s.text("Big headline", 186, 400, 210, color="np", t=c("headline"))
s.source(CC, light=True)

s, c = line_scene("First words of line L01")
s.count(186, 300, 300, c("fifty|50|$50"), 50, money("$", " million"), color="red")   # red = a loss only
s.kicker("what the number is", 192, 640, c("million"))
s.source("Source: <short name> (year)")

s, c = line_scene("First words of the punchline", "ink", hold=0.8, punch=True)       # music cuts out
s.text("No.", 640, 160, 760, color="np", t=c("no"), mode="on")
s.click(c("no"), "impact", 0.55)

chapter("ch1", "Chapter title", ["hq", "hq", "hq", "hq", "hq", "hq", "hq", "hq", "hq"])  # 9 photos

s, c = line_scene("First words of a line about a person")
portrait(s, "p_founder", "Full Name", "Role · year", c("name"))
s.text("What they did", 186, 200, 150, t=c("did"))

# ---------- END ----------
end_card("This is Paper Empire", "Next company", "One-line teaser for the next video")
finish()
