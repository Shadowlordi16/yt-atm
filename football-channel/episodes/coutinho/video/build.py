# OFF THE PITCH · Ep 1 "The Transfer That Broke Barcelona". Run: python3 build.py
import sys, os
sys.path.insert(0, os.path.abspath("~/Videos/yt-atm/kit".replace("~", os.path.expanduser("~"))))
from build_lib import *
import build_lib; build_lib.GAP = 0.85

# football identity: deep pitch green ground, chalk cream, one blaze accent
PITCH = "#0E2A20"; CHALK = "#F2EFE4"; BLAZE = "#FF5A3C"; LINE = "#4E6F5E"; DIM = "#8FA79A"
P = f'<div class="fill" style="background:{PITCH}"></div>'
S1 = "Source: FC Barcelona (6 Jan 2018); reported fee £105m rising to £142m"
S2 = "Source: Daily Echo, Jan 2022"
S3 = "Source: UEFA club licensing rules; club accounting practice"
S4 = "Source: reported €222m PSG release-clause payment, 2017"
S5 = "Source: contemporary match reporting and tactical analysis"
S6 = "Source: 2019-20 Champions League quarter-final, Bayern 8-2 Barcelona"
S7 = "Source: La Liga squad-cost-limit reporting"
S8 = "Source: Messi free agent departure, 2021"

FADE = f'<div class="fill" style="background:linear-gradient(90deg,rgba(14,42,32,.94) 0%,rgba(14,42,32,.86) 46%,rgba(14,42,32,.30) 100%)"></div>'
DARK = '<div class="fill" style="background:rgba(14,42,32,.80)"></div>'

def photo(s, name, t=0.0, dim=FADE):
    """Full-bleed real photo with the pitch-green wash, slowly pushing in."""
    s.photos([(name, 0)], rate=0.02)
    s.raw(dim)

def pitch_svg(sid, t=0.0):
    """A chalk pitch board."""
    return (f'<svg id="{sid}" style="position:absolute;inset:0;width:1920px;height:1080px" viewBox="0 0 1920 1080">'
            f'<rect x="0" y="0" width="1920" height="1080" fill="{PITCH}"/>'
            f'<rect x="120" y="120" width="1680" height="840" fill="none" stroke="{LINE}" stroke-width="8"/>'
            f'<line x1="960" y1="120" x2="960" y2="960" stroke="{LINE}" stroke-width="8"/>'
            f'<circle cx="960" cy="540" r="150" fill="none" stroke="{LINE}" stroke-width="8"/>'
            f'<rect x="120" y="360" width="220" height="360" fill="none" stroke="{LINE}" stroke-width="8"/>'
            f'<rect x="1580" y="360" width="220" height="360" fill="none" stroke="{LINE}" stroke-width="8"/>'
            '</svg>')

# ---------------- COLD OPEN ----------------
s, c = line_scene("January two thousand and eighteen", "ink")
photo(s, "campnou_night", 0.0, DARK)
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.kicker("JANUARY 2018", 150, 170, c("january|January"), "np")
s.text("Coutinho", 142, 260, 170, color="np", t=0.15)
s.count(142, 470, 300, c("142|$142|£142"), 142, "v => '£' + Math.round(v) + 'M'", color="np", d=1.3)
s.el("LIVERPOOL  →  BARCELONA", "left:150px;top:830px;font:900 40px Inter;letter-spacing:.06em;", "np", c("liverpool|Liverpool"))
s.source(S1, light=True)

s, c = line_scene("It is the second most expensive")
photo(s, "campnou_aerial")
s.kicker("AT THE TIME", 150, 200, c("second|time"), "np")
s.text("2nd", 142, 270, 380, color="np", t=c("second"), mode="on")
s.text("most expensive transfer in football", 150, 780, 92, color="np", t=0.3)
s.source(S4, light=True)

s, c = line_scene("Four years later, he leaves", "ink")
photo(s, "campnou_ground")
s.kicker("JANUARY 2022", 150, 200, c("years|2022"), "np")
s.count(142, 280, 300, c("seventeen|17|million"), 17, "v => '£' + Math.round(v) + 'M'", color="np", d=1.2)
s.text("to Aston Villa", 150, 700, 110, color="np", t=0.2)
s.source(S2, light=True)

s, c = line_scene("That is roughly one pound", "ink", punch=True)
photo(s, "campnou_ext", 0.0, DARK)
s.text("1 in 8.", 142, 300, 340, color="np", t=c("eight|1|one"), mode="on")
s.kicker("OF THE MONEY CAME BACK", 150, 780, c("roughly"), "np")
s.source(S1 + "; " + S2, light=True)

s, c = line_scene("Everyone remembers the fee", "ink", hold=0.5)
s.raw(P)
s.kicker("OFF THE PITCH", 150, 240, 0.15, "np")
s.text("THE £142M\nHOLE", 142, 330, 230, color="np", t=c("accounting"))
s.hrule(150, 880, 900, c("accounting"), 10, BLAZE)
s.source("Episode 1", light=True)

# ---------------- CH1: HOW A FEE WORKS ----------------
s, c = line_scene("Here is the thing football")
photo(s, "campnou_aerial")
s.kicker("THE THING NOBODY EXPLAINS", 150, 200, c("thing"), "np")
s.text("A fee is not a bill.", 142, 300, 190, color="np", t=c("bill"))
s.text("It is an entry in the books.", 150, 620, 120, color="np", t=c("balance|books"))
s.source(S3, light=True)

s, c = line_scene("Barca pay one hundred")
photo(s, "campnou_ground")
s.kicker("SPREAD OVER THE CONTRACT", 150, 200, c("spread|barca|Barca"), "np")
s.text("5 years", 142, 300, 220, color="np", t=c("contract"))
s.source(S3, light=True)

s, c = line_scene("In accounting, it is called")
photo(s, "campnou_field", 0.0, DARK)
s.text("AMORTISATION", 142, 380, 200, color="np", t=c("amortization|amortisation"), mode="on")
s.kicker("THE WORD THAT RUNS FOOTBALL", 150, 720, c("called"), "np")
s.source(S3, light=True)

s, c = line_scene("A five-year contract turns")
photo(s, "campnou_night", 0.0, DARK)
s.kicker("£142M ÷ 5", 150, 200, c("five|5"), "np")
# five equal bars
for i in range(5):
    bid = f"{s.sid}-b{i}"
    s.raw(f'<div id="{bid}" style="position:absolute;left:{150 + i * 330}px;top:430px;width:290px;height:260px;background:{BLAZE};opacity:0"></div>',
          js=f"tl.fromTo('#{bid}', {{opacity:0, scaleY:0}}, {{opacity:1, scaleY:1, duration:0.35, transformOrigin:'50% 100%', ease:'power2.out'}}, {0.2 + i*0.18:.3f});")
s.text("£28M a year", 150, 780, 150, color="np", t=c("28|$28"))
s.source(S3, light=True)

s, c = line_scene("That number sits on the books")
photo(s, "anfield2")
s.text("It stays.", 142, 320, 260, color="np", t=c("sits|stays|books"))
s.kicker("WHETHER HE PLAYS OR NOT", 150, 700, c("plays"), "np")
s.source(S3, light=True)

# ---------------- CH2: WHAT THEY ALREADY HAD ----------------
s, c = line_scene("So why buy him")
photo(s, "campnou_aerial")
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.kicker("THE QUESTION", 150, 190, c("why"), "np")
s.text("Not a player.\nAn answer.", 142, 280, 200, color="np", t=c("answer"))
s.source(S5, light=True)

s, c = line_scene("Neymar had left for Paris")
photo(s, "campnou_field")
s.kicker("SUMMER 2017", 150, 200, c("summer|Neymar"), "np")
s.count(142, 300, 330, c("222|two hundred"), 222, "v => '€' + Math.round(v) + 'M'", color="np", d=1.4)
s.text("the release clause. Paid in full.", 150, 760, 104, color="np", t=c("clause|world|record"))
s.source(S4, light=True)

s, c = line_scene("Barca had the money")
photo(s, "campnou_ext")
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.kicker("THE HOLE", 150, 190, c("hole|money"), "np")
s.text("Left wing.", 142, 280, 190, color="np", t=c("left"))
s.source(S5, light=True)

s, c = line_scene("The problem")
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.raw(f'<div id="{s.sid}-ten" style="position:absolute;left:700px;top:430px;width:340px;height:220px;border:10px solid {CHALK};opacity:0"></div>',
      js=f"on('#{s.sid}-ten', {c('number|10'):.3f});")
s.kicker("HIS BEST POSITION", 150, 190, c("problem|winger"), "np")
s.text("No. 10", 142, 280, 210, color="np", t=c("middle"))
s.source(S5, light=True)

s, c = line_scene("Liverpool knew exactly where")
photo(s, "anfield", 0.0, DARK)
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.raw(f'<rect id="{s.sid}-lz" x="160" y="180" width="420" height="720" fill="{BLAZE}" opacity="0.18"/>'
      f'<path id="{s.sid}-ar" d="M300 300 Q460 540 360 800" fill="none" stroke="{CHALK}" stroke-width="10" stroke-dasharray="600" stroke-dashoffset="600"/>',
      js=f"on('#{s.sid}-lz', {c('liverpool|Liverpool'):.3f}); tl.fromTo('#{s.sid}-ar', {{strokeDashoffset:600}}, {{strokeDashoffset:0, duration:1.1, ease:'power1.inOut'}}, {c('cutting|late', off=-0.2):.3f});")
s.kicker("WHERE IT WORKED", 150, 190, c("knew|exactly"), "np")
s.text("Left. Cutting in.", 142, 720, 110, color="np", t=c("cutting|left"))
s.source(S5, light=True)

s, c = line_scene("Barcelona's middle already had Messi")
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.raw(f'<circle id="{s.sid}-m" cx="980" cy="540" r="150" fill="none" stroke="{CHALK}" stroke-width="12"/>',
      js=f"on('#{s.sid}-m', {c('messi|Messi'):.3f});")
s.kicker("THE SAME SQUARE METRES", 150, 190, c("middle|room"), "np")
s.text("Messi's.", 142, 740, 120, color="np", t=c("room|best"))
s.source(S5, light=True)

s, c = line_scene("So Barca played him wide")
s.raw(pitch_svg(f"{s.sid}-p", 0.0), js=f"on('#{s.sid}-p', 0.0);")
s.text("Wrong\nrectangle.", 142, 260, 220, color="np", t=c("wide|system"))
s.source(S5, light=True)

s, c = line_scene("He was not bad")
s.raw(P)
s.kicker("THE POINT", 150, 220, c("bad"), "np")
s.text("Not bad.\nBadly placed.", 142, 310, 200, color="np", t=c("wrong|placed|rectangle"))
s.hrule(150, 860, 1000, c("rectangle"), 10, BLAZE)
s.source(S5, light=True)

# ---------------- CH3: 8-2 ----------------
s, c = line_scene("2019. Barcelona are in the Champions")
photo(s, "allianz_night", 0.0, DARK)
s.kicker("2019-20 CHAMPIONS LEAGUE QUARTER-FINAL", 150, 190, c("2019|quarter|champions"), "np")
s.text("Bayern  8\nBarcelona  2", 142, 320, 220, color="np", t=c("8|2|Bayern"))
s.source(S6, light=True)

s, c = line_scene("Two of Bayern's goals")
photo(s, "allianz")
s.text("×2", 142, 280, 340, color="np", extra=f"color:{BLAZE}", t=c("two|2"), mode="on")
s.kicker("SCORED BY BARCELONA'S OWN RECORD SIGNING, ON LOAN", 150, 720, c("goals|cautinho|coutinho|Coutinho"), "np")
s.source(S6, light=True)

s, c = line_scene("The club that bought him", "ink", punch=True)
s.raw(P)
s.text("He demolished\nthe club that\nbought him.", 142, 240, 150, color="np", t=c("demolish|watched"))
s.source(S6, light=True)

s, c = line_scene("That is not a football failure", "ink", punch=True)
photo(s, "allianz", 0.0, DARK)
s.text("A very expensive\ncomedy.", 142, 300, 180, color="np", t=c("comedy"))
s.source(S6, light=True)

s, c = line_scene("Bayern did not even want")
s.raw(P)
s.kicker("END OF LOAN", 150, 200, c("loan|Bayern"), "np")
s.text("Sent back.", 142, 300, 240, color="np", t=c("back|sent"))
s.source(S6, light=True)

# ---------------- CH4: THE MECHANISM ----------------
s, c = line_scene("But the real damage")
photo(s, "campnou_aerial", 0.0, DARK)
s.kicker("AWAY FROM THE PITCH", 150, 220, c("damage|pitch"), "np")
s.text("The accounts.", 142, 320, 200, color="np", t=c("damage|pitch"))
s.source(S7, light=True)

s, c = line_scene("Barcelona's wage bill")
photo(s, "campnou_aerial")
s.count(142, 300, 320, c("500|five hundred"), 500, "v => '€' + Math.round(v) + 'M'", color="np", d=1.4)
s.kicker("WAGES, PER YEAR. THE HIGHEST IN FOOTBALL.", 150, 720, c("wage|bill"), "np")
s.source(S7, light=True)

s, c = line_scene("Here is the mechanism")
photo(s, "campnou_ground", 0.0, DARK)
s.kicker("THE RULE IN SPAIN", 150, 200, c("mechanism|rule|spain|Spain"), "np")
s.text("Your spend limit\nis tied to your revenue.", 142, 290, 140, color="np", t=c("tied|revenue"))
s.source(S7, light=True)

s, c = line_scene("Spend future revenue")
photo(s, "campnou_night", 0.0, DARK)
s.text("Bigger.", 142, 260, 300, color="np", t=c("bigger"))
s.text("Poorer.", 142, 620, 300, color="np", extra=f"color:{BLAZE}", t=c("poorer"))
s.source(S7, light=True)

s, c = line_scene("They had spent the Neymar money")
photo(s, "campnou_ground")
s.kicker("THE €222M, REINVESTED", 150, 190, c("spent|Neymar|money"), "np")
x = 150
for lab, w in [("COUTINHO", "coutinho|Cautonho|cautinho|cow tinho|Koutinho|Coughtonho"), ("DEMBÉLÉ", "dembele|Dembele"), ("GRIEZMANN", "greisman|Griezmann|griezmann")]:
    s.el(lab, f"left:{x}px;top:300px;border:8px solid {LINE};padding:22px 30px;font:900 56px Inter;color:{CHALK};opacity:0",
         None, c(w)); x += 560
s.text("None of it worked.", 150, 640, 130, color="np", t=c("worked|none"))
s.source(S4 + "; " + S7, light=True)

s, c = line_scene("Under La Liga's salary rules")
photo(s, "messi2", 0.0, DARK)
s.kicker("THE CONSEQUENCE", 150, 190, c("salary|rules|consequence"), "np")
s.text("Could not\nregister players.", 142, 280, 170, color="np", t=c("register"))
s.text("Not even Messi.", 150, 760, 150, color=BLAZE, t=c("messi|Messi", nth=1))
s.source(S7, light=True)

s, c = line_scene("Messi left in 2021")
photo(s, "p_messi", 0.0, DARK)
s.count(142, 280, 320, c("2021"), 2021, "v => String(Math.round(v))", color="np", d=1.2)
s.kicker("FREE TRANSFER", 150, 700, c("free|2021"), "np")
s.text("The best player of his generation.", 150, 790, 96, color="np", t=c("greatest|generation"))
s.source(S8, light=True)

s, c = line_scene("So the Coutinho deal was not the cause")
photo(s, "campnou_ext")
s.text("Not the cause.\nThe test case.", 142, 280, 180, color="np", t=c("test|case"))
s.source(S3 + "; " + S7, light=True)

s, c = line_scene("And that is why this is not really")
photo(s, "campnou_field", 0.0, DARK)
s.kicker("THE HONEST VERSION", 150, 220, c("why|honest|invoice"), "np")
s.text("He was the invoice.\nNot the policy.", 142, 310, 170, color="np", t=c("policy|invoice"))
s.source(S3, light=True)

# ---------------- ENDING ----------------
s, c = line_scene("In 2022, Barca sold Coutinho")
photo(s, "campnou_ground")
s.count(142, 300, 330, c("17|$17|seventeen"), 17, "v => '£' + Math.round(v) + 'M'", color="np", d=1.2)
s.kicker("ASTON VILLA, 2022", 150, 720, c("villa|Villa|2022"), "np")
s.source(S2, light=True)

s, c = line_scene("On the balance sheet")
photo(s, "anfield2")
s.kicker("TWO DIFFERENT LEDGERS", 150, 200, c("balance"), "np")
s.text("The books: settled.", 142, 300, 140, color="np", t=c("amortized|books"))
s.text("The pitch: four years.", 150, 520, 140, color=BLAZE, t=c("years|pitch"))
s.source(S2, light=True)

s, c = line_scene("This is what a transfer actually is")
photo(s, "campnou_aerial")
s.text("A bet with\na payment plan.", 142, 300, 180, color="np", t=c("bet|payment"))
s.source(S3, light=True)

s, c = line_scene("Barcelona bet big", hold=1.2, punch=True)
photo(s, "campnou_night", 0.0, DARK)
s.text("Still running.", 142, 340, 240, color="np", t=c("running"), mode="on")
s.source(S2, light=True)

s, c = line_scene("Next time", "ink", hold=1.6)
s.raw(P)
s.kicker("OFF THE PITCH", 150, 300, 0.3, "np")
s.text("NEXT", 142, 400, 260, color="np", t=c("next|Next"))
s.el("The manager hired to fix a club, and the dressing room that decided otherwise",
     "left:150px;top:760px;width:1500px;font:400 52px Inter;color:#F2EFE4;line-height:1.3", "np", c("manager"))
s.click(c("next|Next"), "impact", 0.4)
finish()
