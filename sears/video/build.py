# Sears: "It sold the roof over its head" (Paper Empire). One block per voice line. Run: python3 build.py
import sys, os; sys.path.insert(0, os.path.abspath("../../kit"))
from build_lib import *
import build_lib; build_lib.GAP = 1.15

PH = "Photo: Wikimedia Commons (credits in description)"
S1  = "Source: company histories via Wikipedia, \"Sears\""
S2  = "Source: early Sears catalogues via Wikipedia, \"Sears\""
S3  = "Source: company histories via Wikipedia, \"Sears\""
S5  = "Source: company histories via Wikipedia, \"Sears\""
S6  = "Source: Willis Tower / Sears Tower records via Wikipedia"
S7  = "Source: \"How Sears Lost the American Shopper\", Times"
S8  = "Source: AP via NBC News (17 Nov 2004)"
S9  = "Source: Washington Post (11 Mar 2007) via Wikipedia"
S10 = "Source: Seritage Growth Properties, SEC EX-99.2 (Form 8-K)"
S11 = "Source: Seritage SEC filing; NYT DealBook (12 Jun 2015)"
S12 = "Source: Reuters via RTE (15 Oct 2018)"
S13 = "Source: ESL Investments (11 Feb 2019) via Wikipedia"
S14 = "Source: AP (27 Dec 2011); Wikipedia, \"Sears Holdings\""
S15 = "Source: Wikipedia, \"Sears\" and \"Sears Holdings\""
S17 = "Source: Wikipedia, \"Prodigy (online service)\" citing NYT (6 Sep 1990)"
S18 = "Source: Wikipedia, \"Sears\" (company history)"
S19 = "Source: Wikipedia, \"Sears\" citing CNN Money (14 May 2018)"
S20 = "Source: Wikipedia, \"Sears\" citing CoStar and SlashGear (31 Aug 2025)"
DIM = '<div class="fill" style="background:rgba(20,20,20,.55)"></div>'
FADE = '<div class="fill" style="background:linear-gradient(0deg,rgba(20,20,20,.92),rgba(20,20,20,0) 62%)"></div>'

# =========================== COLD OPEN ===========================
s, c = line_scene("For most of the twentieth century", "ink")
s.photos([("catalog_old", 0), ("catalog", c("sears", off=-0.2)), ("organ", c("wrote", off=-0.2))], rate=0.03)
s.raw(DIM)
s.raw('<div id="l00-bk" style="position:absolute;left:100px;top:190px;width:1060px;height:600px;background:rgba(20,20,20,.93)"></div>',
      js="on('#l00-bk', 0.0);")
s.kicker("Sears, Roebuck and Co.", 214, 626, 0.15, "np")
s.text("You wrote\nto Sears.", 236, 268, 190, color="np", t=0.05, mode="on")
s.source(S1, light=True)

s, c = line_scene("Watches, bicycles, sewing machines")
s.photos([("catalog", 0), ("organ", c("organ|sewing", off=-0.3))], rate=0.03)
s.raw(DIM)
s.kicker("Sears catalogue", 192, 200, c("watches|Sears" ), "np")
s.count(186, 270, 340, c("houses|house"), 532, INT, color="np", d=1.4)
s.kicker("pages in the 1895 catalogue", 192, 660, c("build"), "np")
s.source(S2, light=True)

s, c = line_scene("By nineteen seventy-four")
s.photos([("tower", 0)], rate=0.02)
s.raw(FADE)
s.text("The tallest\nin the world.", 186, 640, 150, color="np", t=0.05)
s.kicker("No. 1 retailer in America", 192, 420, 0.25, "np")
s.source(S6 + "; " + S7, light=True)

s, c = line_scene("And on October fifteenth")
s.kicker("15 October 2018", 192, 220, 0.05)
s.text("Chapter 11", 186, 300, 280, color="red", t=0.2)
s.kicker("about 700 stores left", 192, 700, c("seven|700"))
s.source(S12)

s, c = line_scene("Everyone tells the same story")
s.photos([("closing_sale", 0)], rate=0.02)
s.raw(DIM)
s.text("MISSED THE\nINTERNET", 186, 280, 190, color="np", t=c("everyone|tells" ))
s.hrule(192, 700, 1000, c("internet"), 8, "#E9E6DF")
s.source(S12, light=True)

s, c = line_scene("But look at what Sears", "ink", punch=True)
s.photos([("closing_night", 0)], rate=0.02)
s.raw(DIM)
s.raw('<div style="position:absolute;left:140px;top:200px;width:1200px;height:360px;background:rgba(20,20,20,.9)"></div>')
s.text("CASH", 186, 240, 200, color="np", t=c("selling" ))
s.text("→", 560, 250, 180, color="np", t=c("renting", off=0.1))
s.text("A LEASE", 760, 240, 200, color="np", t=c("renting"))
s.source(S10 + "; " + S11, light=True)

s, c = line_scene("This is the story", "ink", hold=0.6)
s.raw(f'<div id="g06-crown" class="o0" style="position:absolute;left:192px;top:300px">{CROWN_SVG.format(s=180)}</div>', js="on('#g06-crown', 0.25);")
s.kicker("Paper Empire", 410, 360, 0.3, "np")
s.text("Sears", 186, 500, 340, color="np", t=c("company" ))
s.kicker("It sold the roof over its head.", 192, 860, c("business"), "np")
s.click(c("company"), "impact", 0.4)

# =========================== CHAPTER 1 ===========================
chapter("ch1", "You wrote to Sears",
        ["catalog_old", "catalog", "store_1920s", "farm_store", "louisville", "palmtree", "tower", "organ", "store_1920b"], d=3.0)

s, c = line_scene("Sears started in eighteen ninety-two")
s.kicker("1892", 192, 220, c("1892|eighteen" ))
s.text("Watches,\nby mail.", 186, 290, 190, t=c("watches"))
s.text("Alvah Roebuck", 186, 720, 130, color="grey", t=c("robuck|Robuck|roebuck"))
s.source(S1)

s, c = line_scene("The catalogue was the idea")
photo_card(s, "catalog", 1150, 150, 620, 640, c("catalogue"), rot=-1.4)
s.kicker("The catalogue", 192, 220, c("catalogue" ))
s.text("One book.\nHundreds\nof pages.", 186, 290, 160, t=c("book"))
s.source(S2)

s, c = line_scene("In eighteen ninety-five")
s.count(186, 260, 300, c("$75|75000|75"), 75000, money("$"), d=1.3)
s.kicker("Roebuck sells his half, 1895", 192, 640, c("share" ))
s.source(S3)

s, c = line_scene("By nineteen oh seven")
s.count(186, 260, 340, c("$50|50"), 50, "v => '$' + Math.round(v) + 'M'", d=1.4)
s.kicker("annual sales, 1907", 192, 660, c("year" ))
s.source(S5)

s, c = line_scene("That was money from farms")
s.photos([("farm_store", 0)], rate=0.02)
s.raw(FADE)
s.text("By post.", 186, 260, 260, color="np", t=c("post" ), mode="on")
s.kicker("farms and small towns", 192, 720, c("farms"), "np")
s.source(S2, light=True)

s, c = line_scene("Then Sears did something smart")
photo_card(s, "store_1920s", 1140, 150, 640, 480, c("stores"), rot=1.2)
s.kicker("1925", 192, 220, c("1925|twenty" ))
s.text("The catalogue\ngot a front door.", 186, 290, 150, t=c("door"))
s.source(S1)

s, c = line_scene("For decades the formula held")
s.photos([("louisville", 0)], rate=0.02)
s.raw(FADE)
s.text("Trust.", 186, 240, 320, color="np", t=c("trusted" ), mode="on")
s.source(S1, light=True)

s, c = line_scene("The book was not a side business")
s.photos([("store_1920b", 0)], rate=0.02)
s.raw(DIM)
s.text("A warehouse\nthe size\nof a town.", 186, 220, 170, color="np", t=c("warehouse" ))
s.source(S2, light=True)

s, c = line_scene("And Sears did not just sell")
x = 192
for w, lab in [("made|own", "KENMORE"), ("made", "CRAFTSMAN"), ("own", "DIEHARD")]:
    s.el(lab, f"left:{x}px;top:300px;background:#141414;padding:18px 26px", "kick np", c(w, off=0.15 * (x // 300))); x += len(lab) * 36 + 100
s.text("Its own brands.", 186, 520, 190, t=c("own" ))
s.kicker("not just other people's products", 192, 760, c("products"))
s.source(S18)

s, c = line_scene("Those names were the reason")
photo_card(s, "steam", 1150, 200, 620, 460, c("tool"), rot=-1.2)
s.kicker("A SEARS TOOL WAS A SEARS TOOL", 192, 220, c("reason" ))
s.text("CRAFTSMAN", 186, 290, 190, t=c("seer|names|tool"))
s.text("Kenmore. DieHard.", 186, 600, 130, color="grey", t=c("names"))
s.source(S18)

s, c = line_scene("Most of the twentieth century")
s.raw('<svg style="position:absolute;left:186px;top:300px" width="1540" height="500" viewBox="0 0 1540 500">'
      '<polyline id="g17-ln" points="0,470 300,380 620,260 960,140 1540,40" fill="none" stroke="#141414" stroke-width="14" stroke-dasharray="1700" stroke-dashoffset="1700"/></svg>',
      js=f"tl.fromTo('#g17-ln', {{ strokeDashoffset: 1700 }}, {{ strokeDashoffset: 0, duration: 1.8, ease: 'power1.inOut' }}, 0.2);")
s.kicker("1900 to 1980", 192, 220, c("most|20th" ))
s.text("Straight up.", 186, 700, 190, t=c("straight"))
s.source(S7)

s, c = line_scene("It was the biggest retailer")
s.text("No. 1", 186, 280, 380, t=c("biggest" ), mode="on")
s.kicker("the largest retailer in the United States", 192, 720, c("states"))
s.source(S7)

s, c = line_scene("In nineteen seventy-four it finished")
s.photos([("tower2", 0)], rate=0.02)
s.raw(FADE)
s.kicker("1974", 192, 220, c("1974|seventy" ), "np")
s.text("Sears Tower", 186, 700, 170, color="np", t=c("name"))
s.source(S6, light=True)

s, c = line_scene("A hundred and ten floors")
photo_card(s, "tower", 1140, 150, 600, 620, c("floors|110"), rot=-1.2)
s.text("110\nfloors", 186, 260, 230, t=c("hundred|110" ))
s.kicker("built for a catalog company", 192, 720, c("catalog"))
s.source(S6)

s, c = line_scene("And then in nineteen eighty-nine")
s.text("Walmart", 186, 240, 240, t=c("wal|-mart|Mart" ))
s.text("passed it.", 186, 520, 240, color="grey", t=c("passed"))
s.hrule(192, 790, 900, c("passed", off=0.3), 10, "#D7261E")
s.source(S7)

# =========================== CHAPTER 2 ===========================
chapter("ch2", "A hedge fund with a store attached",
        ["closing_sale", "parking", "closed_mall", "closing_night", "mannequin", "walmart", "catalog", "tower2", "farm_store"], d=3.0)

s, c = line_scene("Here is where the story usually jumps")
s.text("Not the web.\nNot yet.", 186, 260, 200, color="grey", t=c("internet" ))
s.hrule(192, 780, 800, c("internet"))
s.source(S9)

s, c = line_scene("In two thousand and four")
s.kicker("2004", 192, 220, c("2004|two" ))
s.text("Eddie\nLampert", 186, 290, 220, t=c("lampard|lampert|Lampert"))
s.text("ESL Investments", 186, 740, 130, color="grey", t=c("man"))
s.source(S8 + "; " + S9)

s, c = line_scene("His company, Kmart")
s.kicker("Kmart buys Sears", 192, 220, c("kmart|Kmart" ))
s.count(186, 290, 320, c("$11|11"), 11, "v => '$' + Math.round(v) + ' billion'", d=1.4)
s.kicker("Kmart had left bankruptcy in 2003", 192, 700, c("bankruptcy"))
s.source(S8)

s, c = line_scene("Lampert was not a retailer")
s.text("A hedge\nfund\nmanager.", 186, 200, 170, t=c("hedge" ))
s.text("He saw a balance sheet.", 186, 760, 130, color="grey", t=c("sheet"))
s.source(S9)

s, c = line_scene("By two thousand and seven")
s.quote(192, 170, 1536, 600, "WASHINGTON POST, 2007", "A hedge fund with a store that sells things.",
        "on what Sears Holdings had become", c("hedge|fund"), qsize=100)
s.source(S9)

s, c = line_scene("But Sears had been more")
s.photos([("store_1920s", 0)], rate=0.02)
s.raw(DIM)
s.kicker("1981", 192, 220, c("1981|ninety" ), "np")
s.text("A stockbroker.\nA real estate\nfirm.", 186, 290, 150, color="np", t=c("stockbroker"))
s.source(S18)

s, c = line_scene("It launched the Discover card")
s.photos([("louisville", 0)], rate=0.02)
s.raw(DIM)
s.kicker("TWO BUSINESSES, 1981-1985", 192, 200, c("retail" ), "np")
s.text("A SHOP", 186, 290, 190, color="np", t=c("shop|retail"))
s.text("A BANK", 186, 520, 190, color="np", t=c("insurance|card"))
s.source(S18)

s, c = line_scene("And here is the part", "ink", punch=True)
s.photos([("tower2", 0)], rate=0.02)
s.raw(DIM)
s.text("1984.", 186, 240, 300, color="np", t=0.15, mode="on")
s.kicker("before there was a web", 192, 700, c("internet"), "np")
s.text("Sears, IBM and CBS", 186, 760, 90, color="np", t=c("sears|part"))
s.source(S17, light=True)

s, c = line_scene("It was called Prodigy")
s.photos([("store_1920b", 0)], rate=0.02)
s.raw(DIM)
s.kicker("Prodigy · a joint venture", 192, 220, c("prodigy|Prodigy" ), "np")
s.text("SEARS", 186, 300, 150, color="np", t=c("sears|Sears"))
s.text("+ IBM", 500, 300, 150, color="np", t=c("ibm|IBM"))
s.text("+ CBS", 800, 300, 150, color="np", t=c("cbs|CBS"))
s.kicker("shop and send messages, from home", 192, 760, c("shop" ), "np")
s.source(S17, light=True)

s, c = line_scene("By nineteen ninety, Prodigy")
s.count(186, 250, 330, c("four|465|hundred"), 465000, INT, d=1.4)
s.kicker("subscribers by 1990", 192, 660, c("subscribers" ))
s.text("No. 2 online service in America", 186, 760, 120, color="grey", t=c("second|largest"))
s.source(S17)

s, c = line_scene("Sears was there first")
s.photos([("farm_store", 0)], rate=0.02)
s.raw(DIM)
s.text("There first.", 186, 280, 220, color="np", t=c("first" ), mode="on")
s.text("It didn't treat it as the future.", 186, 620, 130, color="np", t=c("future"))
s.source(S17 + "; " + S9, light=True)

s, c = line_scene("The plan was not to sell more")
photo_card(s, "closed_mall", 1180, 200, 580, 420, c("plan"), rot=1.2)
s.text("Sell what\nSears owned.", 186, 300, 150, t=c("owned" ))
s.source(S9)

s, c = line_scene("First Lands' End")
s.photos([("closing_night", 0)], rate=0.02)
s.raw(FADE)
x = 192
for w, lab in [("lands|Lands", "LANDS' END"), ("canadian|Canadian", "SEARS CANADA"), ("craftsmen|craftsman", "CRAFTSMAN")]:
    s.el(lab, f"left:{x}px;top:300px;background:#141414;padding:18px 26px", "kick np", c(w)); x += len(lab) * 36 + 90
s.text("sold off", 186, 500, 200, color="np", t=c("sold" ))
s.source(S15 + "; " + S19, light=True)

s, c = line_scene("In the same years")
s.photos([("closing_sale", 0)], rate=0.02)
s.raw(DIM)
s.text("101 years", 186, 280, 260, color="np", t=c("101|hundred" ))
s.kicker("Sears stops selling Whirlpool", 192, 640, c("whirlpool|Whirlpool"), "np")
s.source(S19, light=True)


# =========================== CHAPTER 3 ===========================
chapter("ch3", "Selling the building to pay the rent",
        ["store_1920s", "closing_night", "parking", "tower", "closed_mall", "mannequin", "closing_sale", "louisville", "palmtree"], d=3.0)

s, c = line_scene("A hundred and one years of selling")
s.photos([("closing_sale", 0)], rate=0.02)
s.raw(DIM)
s.kicker("Whirlpool, ended", 192, 220, c("years|Whirlpool" ), "np")
s.text("1916", 186, 300, 200, color="np", t=0.15)
s.text("2017", 560, 300, 200, color="np", t=c("2017|years"))
s.text("over price", 186, 640, 130, color="np", t=c("price"))
s.source(S19, light=True)

s, c = line_scene("And the tools went too")
s.photos([("farm_store", 0)], rate=0.02)
s.raw(DIM)
s.kicker("Craftsman", 192, 220, c("tools|Craftsman|craftsman" ), "np")
s.text("CRAFTSMAN", 186, 300, 220, color="np", t=0.1)
s.strike(176, 580, 1180, c("sold"), 22)
s.kicker("sold to a competitor", 192, 640, c("competitor" ), "np")
s.source(S19, light=True)

s, c = line_scene("In twenty fifteen, Sears made")
s.photos([("store_1920b", 0)], rate=0.02)
s.raw(DIM)
s.kicker("2015", 192, 220, c("2015|twenty" ), "np")
s.text("Seritage", 186, 290, 280, color="np", t=c("saratage|seritage|Seritage"))
s.text("a company Sears created", 186, 680, 130, color="np", t=c("created"))
s.source(S10, light=True)

s, c = line_scene("Then Seritage bought two hundred")
s.photos([("closing_night", 0)], rate=0.02)
s.raw(DIM)
s.count(186, 240, 300, c("234|two|thirty"), 234, INT, color="np", d=1.2)
s.kicker("Sears stores, bought by Seritage", 192, 600, c("stores" ), "np")
s.count(186, 660, 300, c("$2|2|point"), 2.7, "v => '$' + v.toFixed(1) + ' billion'", color="red", d=1.4)
s.source(S10, light=True)

s, c = line_scene("Sears got the cash")
s.photos([("parking", 0)], rate=0.02)
s.raw(DIM)
s.text("SEARS", 186, 260, 150, color="np", t=c("sears|Sears"))
s.text("gets the cash", 186, 430, 150, color="np", t=c("cash"))
s.text("SERITAGE", 966, 260, 150, color="np", t=c("saratage|seritage|Seritage"))
s.text("gets the buildings", 966, 430, 150, color="np", t=c("buildings"))
s.source(S10, light=True)

s, c = line_scene("To pay for it, Seritage raised")
s.photos([("closed_mall", 0)], rate=0.02)
s.raw(FADE)
s.text("A rights offering.", 186, 260, 180, color="np", t=c("raised|rights"))
s.text("Sears' own shareholders, buying back\ntheir own stores.", 186, 640, 110, color="np", t=c("shareholders"))
s.source(S10, light=True)

s, c = line_scene("Then it listed on the")
s.kicker("New York Stock Exchange", 192, 220, c("exchange|York" ))
s.text("SRG", 186, 290, 340, t=c("listed"), mode="on")
s.text("Sears' shops, as a share price", 186, 720, 130, color="grey", t=c("share"))
s.source(S10)

s, c = line_scene("So Sears leased the stores back")
s.stamp("TENANT", 186, 260, 280, c("tenant"), rot=-4)
s.text("in its own\nbuildings", 186, 640, 170, color="grey", t=c("buildings" ))
s.source(S11)

s, c = line_scene("Every quarter, it handed rent", "ink")
s.kicker("EVERY QUARTER", 192, 220, c("every" ))
s.text("SEARS", 186, 300, 190, color="np", t=c("rent"))
s.text("→ RENT →", 186, 540, 190, color="red", t=c("company"))
s.text("SERITAGE", 186, 760, 190, color="np", t=c("created"))
s.source(S11, light=True)

s, c = line_scene("Seritage even kept the right")
s.photos([("closed_mall", 0)], rate=0.02)
s.raw(DIM)
s.text("RECAPTURE", 186, 280, 200, color="np", t=c("right|take" ))
s.text("take the space back, rent it to someone else", 186, 620, 120, color="np", t=c("else"))
s.source(S10, light=True)

s, c = line_scene("That is not a rescue", punch=True)
s.photos([("mannequin", 0)], rate=0.02)
s.raw(DIM)
s.kicker("SELL THE ASSET", 192, 220, c("rescue" ))
s.text("PAY THE RENT", 186, 520, 190, color="red", t=c("heating"))
s.source(S10 + "; " + S11, light=True)

s, c = line_scene("And that is the whole problem")
s.photos([("parking", 0)], rate=0.02)
s.raw(FADE)
s.text("A shop sells\nfor 50 years.", 186, 200, 150, color="np", t=c("shop" ))
s.text("A building sells\nonce.", 186, 520, 150, color="red", t=c("once|building"))
s.source(S10 + "; " + S11, light=True)

s, c = line_scene("When the building is gone")
s.photos([("parking", 0)], rate=0.02)
s.raw(DIM)
s.text("Nothing left\nto borrow\nagainst.", 186, 220, 160, color="np", t=c("borrow" ))
s.source(S11, light=True)

# =========================== CHAPTER 4 ===========================
chapter("ch4", "The slow closing",
        ["closing_night", "closing_sale", "parking", "mannequin", "closed_mall", "walmart", "store_1920s", "palmtree", "closing_night"], d=3.0)

s, c = line_scene("None of this was sudden")
s.photos([("closing_night", 0)], rate=0.02)
s.raw(DIM)
s.kicker("2011", 192, 220, c("2011|eleven" ), "np")
s.count(186, 290, 260, c("shutting|stores"), 120, "v => Math.round(v) + ' stores'", color="red", d=1.2)
s.kicker("100 to 120 announced, December 2011", 192, 640, c("shutting|closing" ), "np")
s.source(S14, light=True)

s, c = line_scene("Every year, another round")
s.photos([("closing_sale", 0)], rate=0.02)
s.raw(FADE)
s.text("2011\n2012\n2013\n2014", 186, 200, 130, color="np", t=c("every" ))
s.text("2015\n2016\n2017\n2018", 700, 200, 130, color="np", t=c("round|another"))
s.source(S14, light=True)

s, c = line_scene("Each closed store took away")
s.photos([("parking", 0), ("closed_mall", c("closed", off=-0.2))], rate=0.03)
s.raw(FADE)
s.text("She went\nsomewhere else.", 186, 240, 180, color="np", t=c("away|closed" ))
s.source(S14, light=True)

s, c = line_scene("Meanwhile Walmart and Amazon")
s.photos([("walmart", 0)], rate=0.02)
s.raw(DIM)
s.raw('<div style="position:absolute;left:120px;top:220px;width:1000px;height:520px;background:rgba(20,20,20,.9)"></div>')
s.text("Bigger.\nCheaper.", 186, 280, 220, color="np", t=c("bigger" ))
s.source(S7, light=True)

s, c = line_scene("Sears had one thing")
s.photos([("closing_sale", 0)], rate=0.02)
s.raw(DIM)
s.kicker("WHAT SEARS STILL OWNED", 192, 220, c("thing" ))
s.text("THOUSANDS", 186, 300, 200, color="np", t=c("thousands"))
s.text("of buildings", 186, 560, 150, color="np", t=c("buildings"))
s.source(S10, light=True)

s, c = line_scene("By twenty eighteen, Sears Holdings")
s.photos([("parking", 0)], rate=0.02)
s.raw(FADE)
s.count(186, 260, 340, c("700|seven"), 700, "v => Math.round(v) + ' stores'", color="np", d=1.2)
s.kicker("once thousands", 192, 660, c("thousands" ), "np")
s.source(S12, light=True)

s, c = line_scene("On October fifteenth", "ink")
s.stamp("CHAPTER 11", 186, 300, 230, c("chapter|eleven|bankruptcy"), rot=-5)
s.kicker("15 October 2018", 192, 700, c("october|October|2018" ), "np")
s.source(S12, light=True)

s, c = line_scene("It planned to close")
s.photos([("closed_mall", 0)], rate=0.02)
s.raw(DIM)
s.count(186, 240, 340, c("142|hundred"), 142, "v => Math.round(v) + ' stores'", color="red", d=1.2)
s.kicker("closing straight away", 192, 640, c("close|closing" ), "np")
s.source(S12, light=True)

s, c = line_scene("In twenty nineteen the assets")
s.photos([("closed_mall", 0)], rate=0.02)
s.raw(DIM)
s.kicker("2019", 192, 220, 0.1, "np")
s.text("Transformco", 186, 290, 240, color="np", t=0.2)
s.kicker("Lampert's fund buys what is left", 192, 700, c("fund|assets" ), "np")
s.source(S13, light=True)

s, c = line_scene("The man who had run Sears", punch=True)
s.photos([("closing_night", 0)], rate=0.02)
s.raw(DIM)
s.text("He bought\nwhat was left.", 186, 260, 200, color="np", t=0.15)
s.source(S13, light=True)

s, c = line_scene("And then the ending", "ink", punch=True)
s.text("A real estate\ncompany.", 186, 240, 190, color="np", t=c("real" ))
s.kicker("not a retailer any more", 192, 700, c("retailer"), "np")
s.source(S20, light=True)

s, c = line_scene("It did not go for the merchandise")
s.photos([("parking", 0)], rate=0.02)
s.raw(FADE)
s.text("It went for\nthe land.", 186, 240, 220, color="np", t=c("land" ))
s.source(S20, light=True)

s, c = line_scene("By the end of twenty twenty-five")
s.photos([("palmtree", 0)], rate=0.02)
s.raw(FADE)
s.kicker("Sears stores left, December 2025", 192, 220, c("2025|twenty" ), "np")
s.count(186, 290, 400, c("five|5"), 5, INT, color="red", d=1.2)
s.source(S20, light=True)

s, c = line_scene("One of them had been open")
s.photos([("store_1920b", 0)], rate=0.02)
s.raw(DIM)
s.text("Since 1954.", 186, 280, 220, color="np", t=0.1)
s.text("One store, older than the shutdown.", 186, 660, 130, color="np", t=c("open"))
s.source(S20, light=True)

# =========================== ENDING ===========================
s, c = line_scene("So the tidy story is wrong")
s.text("MISSED THE WEB?", 186, 260, 190, color="grey", t=c("tidy|miss|simply" ))
s.strike(176, 320, 1080, c("so|tidy"), 20)
s.text("SOLD, NOT LOST", 186, 480, 180, t=c("sold"))
s.source(S10)

s, c = line_scene("A retailer's advantage")
s.text("Buildings", 186, 240, 200, t=c("buildings" ))
s.text("and a name", 186, 480, 200, color="grey", t=c("name"))
s.text("Spent to cover the losses.", 186, 760, 130, t=c("cover"))
s.source(S10)

s, c = line_scene("And a company can sell its assets")
s.text("Selling assets\nis not fixing\nthe business.", 186, 200, 160, t=c("assets" ))
s.source(S11)

s, c = line_scene("That is the quiet way to die")
s.text("A long series\nof sensible\ndecisions.", 186, 220, 160, t=c("sensible" ))
s.source(S20)

s, c = line_scene("The building was never the business", hold=1.0)
s.photos([("palmtree", 0)], rate=0.02)
s.raw(FADE)
s.kicker("WHAT WAS LEFT", 192, 220, c("building" ), "np")
s.text("THE BUILDING", 186, 300, 200, color="np", t=c("sell"))
s.text("nothing else", 186, 620, 140, color="np", t=c("thing|end"))
s.source(S20, light=True)

end_card("This is Paper Empire", "Costco", "The warehouse that charges you to shop there, and makes almost nothing on the goods")

finish()
