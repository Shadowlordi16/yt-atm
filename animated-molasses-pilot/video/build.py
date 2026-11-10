import sys, os
sys.path.insert(0, os.path.abspath('../../kit'))
from build_lib import *

INK='#141414'; PAPER='#E9E6DF'; RED='#D7261E'; GREY='#6B6963'; BROWN='#4b2b1c'

def street(s, wave=False, t=0.2):
    html=f'''<svg id="{s.sid}-art" viewBox="0 0 1920 1080" style="position:absolute;inset:0;width:1920px;height:1080px;background:{PAPER}">
      <rect x="0" y="720" width="1920" height="360" fill="#c7c1b5"/><path d="M0 800 H1920" stroke="#141414" stroke-width="8"/><path d="M0 890 H1920" stroke="#6B6963" stroke-width="4" stroke-dasharray="26 18"/>
      <rect x="120" y="420" width="420" height="300" fill="#8d8b84" stroke="#141414" stroke-width="8"/><rect x="650" y="360" width="360" height="360" fill="#aaa79f" stroke="#141414" stroke-width="8"/><rect x="1120" y="460" width="520" height="260" fill="#95928b" stroke="#141414" stroke-width="8"/>
      <path d="M0 335 H1920" stroke="#141414" stroke-width="12"/><path d="M180 335 V185 M360 335 V185 M540 335 V185 M720 335 V185 M900 335 V185 M1080 335 V185 M1260 335 V185 M1440 335 V185 M1620 335 V185 M1800 335 V185" stroke="#141414" stroke-width="9"/><path d="M0 180 H1920" stroke="#141414" stroke-width="12"/>
      {('<path id="wave" d="M0 760 C280 690 370 560 610 610 C850 660 990 420 1210 470 C1450 525 1570 300 1920 380 L1920 1080 L0 1080 Z" fill="#4b2b1c" stroke="#141414" stroke-width="12"/>' if wave else '')}
    </svg>'''
    s.raw(html, js=f"on('#{s.sid}-art', {t:.3f});")

def tank(s, t=0.2, broken=False):
    extra = '<path d="M1100 290 L1320 250 L1480 330 L1390 420 L1180 390 Z" fill="#4b2b1c" stroke="#141414" stroke-width="12"/>' if broken else '<ellipse cx="1320" cy="260" rx="170" ry="42" fill="#4b2b1c" stroke="#141414" stroke-width="12"/><rect x="1150" y="260" width="340" height="360" fill="#4b2b1c" stroke="#141414" stroke-width="12"/><ellipse cx="1320" cy="620" rx="170" ry="42" fill="#4b2b1c" stroke="#141414" stroke-width="12"/>'
    s.raw(f'''<svg id="{s.sid}-tank" viewBox="0 0 1920 1080" style="position:absolute;inset:0;width:1920px;height:1080px;background:{PAPER}"><rect x="0" y="740" width="1920" height="340" fill="#c7c1b5"/><path d="M0 740 H1920" stroke="#141414" stroke-width="10"/><path d="M300 740 V300 H930 V740" fill="#9b9991" stroke="#141414" stroke-width="10"/><path d="M360 740 V350 H870 V740" fill="#aaa79f" stroke="#141414" stroke-width="6"/>{extra}</svg>''', js=f"on('#{s.sid}-tank', {t:.3f});")

s,c=line_scene('On January fifteenth', 'paper'); street(s, False, 0.05); s.kicker('BOSTON · 1919',192,150,c('January')); s.text('A WAVE OF\nMOLASSES',192,220,230,t=c('wall')); s.source('Source: City of Boston; WBUR')
s,c=line_scene('It was about twenty-five'); street(s, True, 0.05); s.count(150,120,180,c('25'),25,INT,d=1.1); s.kicker('FEET HIGH',160,320,c('feet')); s.count(650,120,180,c('35'),35,INT,d=1.1); s.kicker('MILES PER HOUR',660,320,c('miles')); s.count(1250,120,180,c('2 million|2'),2,"v => Math.round(v) + ' MILLION'",d=1.1); s.kicker('GALLONS',1260,320,c('gallons')); s.source('Source: WBUR; U.S. Geological Survey')
s,c=line_scene('Molasses sounds slow','ink',punch=True); s.text('21 DEAD',180,280,260,color='np',t=c('21')); s.text('150 INJURED',180,620,200,color='np',t=c('150')); s.stamp('DISASTER',1230,500,110,c('killed'),rot=-5); s.source('Source: City of Boston; WBUR',light=True)
s,c=line_scene('This is the story','ink',hold=0.4); s.text('THE MOLASSES\nFLOOD',190,300,260,color='np',t=c('story')); s.hrule(190,900,1540,c('accident')); s.el('A preventable failure', 'left:190px;top:915px;font:700 44px Inter;color:#E9E6DF', 'np', c('accident'))
s,c=line_scene('The tank stood fifty'); tank(s,c('tank')); s.kicker('NORTH END · BOSTON HARBOR',192,130,c('tank')); s.text('50 FEET HIGH\n90 FEET WIDE',192,260,190,t=c('50')); s.source('Source: Massachusetts Secretary of State; WBUR')
s,c=line_scene('It belonged to the Purity'); tank(s,0.05); s.text('PURITY\nDISTILLING',192,260,220,t=c('purity')); s.kicker('MOLASSES → INDUSTRIAL ALCOHOL',192,760,c('industrial')); s.source('Source: Massachusetts Secretary of State')
s,c=line_scene('Neighbors heard'); tank(s,0.05); s.raw(f'<path d="M1120 410 q40 -25 80 0 t80 0 t80 0" fill="none" stroke="{RED}" stroke-width="12"/>'); s.text('LEAKING',1120,760,180,color='red',t=c('leak')); s.source('Source: WBUR; Massachusetts Secretary of State')
s,c=line_scene('Then the temperature climbed'); tank(s,0.05); s.count(180,180,230,c('zero'),0,"v => '0°'",d=0.8); s.count(700,180,230,c('40'),40,"v => Math.round(v) + '°'",d=0.9); s.kicker('WARM MOLASSES MEETS COLD MOLASSES',190,540,c('fresh')); s.source('Source: WBUR; Massachusetts Secretary of State')
s,c=line_scene('At about twelve forty-five'); street(s,True,0.05); s.raw(f'<path d="M1100 400 L1200 470 L1320 360 L1450 510" fill="none" stroke="{RED}" stroke-width="20"/>'); s.stamp('RUPTURE',1180,600,105,c('steel'),rot=-7); s.source('Source: City of Boston; U.S. Geological Survey')
s,c=line_scene('The rescue took four days'); street(s,True,0.05); s.text('FOUR DAYS',170,180,260,color='red',t=c('four')); s.kicker('RESCUE THROUGH THE WRECKAGE',180,520,c('rescue')); s.source('Source: WBUR; Massachusetts Secretary of State')
s,c=line_scene('The company blamed'); s.raw(f'<div style="position:absolute;inset:0;background:{PAPER}"></div>'); s.text('SABOTAGE',190,260,260,color='red',t=c('sabotage')); s.stamp('COURT CASE',1120,650,110,c('court'),rot=-4,ink=True); s.source('Source: Massachusetts Secretary of State')
s,c=line_scene('The flood helped'); s.raw(f'<svg viewBox="0 0 1920 1080" style="position:absolute;inset:0;width:1920px;height:1080px;background:{PAPER}"><rect x="900" y="230" width="700" height="540" fill="#d2cec4" stroke="#141414" stroke-width="10"/><path d="M980 650 L1180 420 L1320 560 L1510 300" fill="none" stroke="#141414" stroke-width="12"/><circle cx="1180" cy="420" r="18" fill="#141414"/><circle cx="1320" cy="560" r="18" fill="#141414"/><circle cx="1510" cy="300" r="18" fill="#141414"/></svg>'''); s.text('SIGNED\nCALCULATIONS',170,250,220,t=c('signed')); s.kicker('LICENSED ENGINEERS',175,760,c('licensed')); s.source('Source: Massachusetts Secretary of State; AIChE')
s,c=line_scene('A disaster that looked'); s.raw(f'<div style="position:absolute;inset:0;background:{PAPER}"></div>'); s.text('IF THE\nSTRUCTURE IS WRONG,',150,220,170,t=c('disaster')); s.text('THE MATERIAL\nDOES NOT MATTER.',150,600,170,t=c('material')); s.hrule(150,950,1500,c('matter')); s.source('Source: Massachusetts Secretary of State')
finish()
