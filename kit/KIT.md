# Paper Empire kit: device reference for build.py

`build.py` is a list of scenes. Each `line_scene(...)` is one voice line. Inside it you place devices.
Coordinates are pixels on a 1920×1080 frame. Times are seconds inside the scene. Always get times from `c("word")`, never by guessing.

## Frame rules (from MOTION.md, check every scene against them)
- **Title-safe box:** x 192–1728, y 108–972. Text starts at x 186–192.
- **Colours:** `color=""` is ink (#141414) on paper; `"np"` is newsprint, for type on dark photos or ink ground; `"grey"` is secondary; `"red"` is **losses only** (money lost, closures, debt, bankruptcy). One red thing per frame.
- **Sizes:** League Gothic headlines 110–420 px. Width ≈ 0.40 × size per character, so 30 characters at 150 px ≈ 1800 px, too wide. Break lines with `\n` or shrink.
- **Never:** text over a person's face, a stamp on a face, glow, gradients as decoration, three cards in a row.

## Scenes
| call | what it makes |
|---|---|
| `s, c = line_scene("first words", ground="paper", hold=0, punch=False)` | one scene for one voice line. `ground`: paper / ink. `hold`: extra silence after (s). `punch=True` cuts the music out under it (2–3 per video) |
| `chapter("ch1", "Title", [9 photo names])` | chapter card: a 3×3 tile flash, then the title |
| `end_card("This is Paper Empire", "Nokia", "teaser line")` | the last scene: animated crown, name, next video |
| `finish()` | the last line of build.py |

## Cues
- `c("word")`: the time that word is spoken. The transcriber writes numbers as digits and sometimes misspells names, so give alternatives: `c("fifty|50|$50")`, `c("icahn|icon")`. Run `python3 ../../kit/words.py` to see exactly what it heard.
- `c("two", 2)`: the second "two". `c("word", off=-0.3)`: 0.3 s earlier.
- A wrong cue stops the build with the transcript printed. Fix the word and run again.

## Devices (methods on `s`)
| call | use |
|---|---|
| `s.photos([("name", t, "50% 30%"), ...], rate=0.03)` | full-bleed photos cut at each t (the 3rd value is the focus point). A click on each cut |
| `s.tiles([9 names], t)` | 3×3 tile-flash reveal |
| `s.text("TEXT", x, y, size, color="", t=..., mode="wipe")` | headline. `mode`: wipe (left to right) or on (hard cut). Returns its id |
| `s.kicker("label", x, y, t, color="")` | small caps label above a headline |
| `s.el("html", "css", "classes", t)` | any positioned element, e.g. a label on a black backing: `s.el("text", "left:..;top:..;background:#141414;padding:14px 22px", "kick np", t)` |
| `s.count(x, y, size, t, to, fmt, color="", d=1.4)` | a number counting up. `fmt`: `INT`, `money("$"," million")`, or JS like `"v => '$' + v.toFixed(1) + 'B'"` |
| `s.stamp("TEXT", x, y, size, t, rot=-6, ink=False)` | a stamp with a thud. Red for losses; `ink=True` for neutral (ACQUIRED, SETTLED) |
| `s.strike(x, y, w, t, h=20)` | a red line ruled through a myth or a dead thing |
| `s.hrule(x, y, w, t, h=8)` | an ink rule |
| `s.dots(x, y, cols, rows, cell, t, d=0.8, total=None, shape="dot")` | an exact count of marks (stores, people). `shape="sq"` for ≤600 squares |
| `s.sheet(x, y, w, h, t, "bottom")` + `s.in_sheet(id, "TEXT", x, y, size, t=...)` | a newsprint sheet sliding over a photo, with type on it (deal tickets) |
| `s.quote(x, y, w, h, "LABEL", "quote", "attribution", t)` | a quote card. Only real, sourced quotes |
| `photo_card(s, "name", x, y, w, h, t, rot=-1.5)` | a real photo (phone, document, advert) on a paper card sliding into place |
| `portrait(s, "p_name", "Name", "Role", t, until=None)` | a person on the right, name at left. `until` hides it later |
| `s.source("Source: ...", light=False)` | the source line (bottom left). **Every number needs one.** `light=True` on dark ground |
| `s.flash(t)` | a 1-frame white flash at a hard turn |
| `s.click(t, "click"/"impact"/"pop"/"train", vol)` | an extra sound |
| `s.raw(html, css, js)` | anything custom (SVG charts). js helpers: `on(sel,t)`, `off(sel,t)`, `wipe(sel,t)`, `rule(sel,t)`, `push(sel,t,d)`, `shake(sel,t)` |

## Pace
- A new picture or a new element every 2–4 s. The cold open and chapter openings go faster (tiles, photo cuts every ~1 s).
- Reveal each thing on the word that names it, never all at once at the start of the line.
- Text that must be read stays on screen at least 0.5 s + 0.3 s per word.
