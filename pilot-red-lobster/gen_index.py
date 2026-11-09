# Lays out the 12 scenes back to back, places each voice line 0.25 s into its scene (0.3 s in s01).
import subprocess
def dur(f): return round(float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)-0.01,3)
scenes=[("s01",6.3),("s02",6.8),("s03",5.6),("s04",9.1),("s05",8.4),("s06",7.0),("s07",5.9),("s08",10.6),("s09",7.8),("s10",8.4),("s11",5.9),("s12",4.2)]
starts={}; t=0
for s,d in scenes: starts[s]=round(t,3); t+=d
total=round(t,3)
hosts="\n".join(f'      <div id="{s}" data-composition-id="{s}" data-composition-src="compositions/{s}.html" data-start="{starts[s]}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>' for s,d in scenes)
vo="\n".join(f'      <audio id="vo-{s}" class="clip" src="assets/vo/{s}.wav" data-start="{round(starts[s]+(0.3 if s=="s01" else 0.25),3)}" data-duration="{dur(f'assets/vo/{s}.wav')}" data-track-index="2" data-volume="1"></audio>' for s,_ in scenes if s!="s12")
# sfx: peak lands one frame after the picture
sfx=[("sfx-20","hit.wav",starts["s01"]+0.3+3.52+0.033-0.214,0.5),
     ("sfx-meritless","boom.mp3",starts["s09"]+0.25+1.36+0.033-0.124,0.45),
     ("sfx-ch11","boom.mp3",starts["s10"]+0.25+7.04+0.033-0.124,0.8)]
sfxs="\n".join(f'      <audio id="{i}" class="clip" src="assets/sfx/{f}" data-start="{round(st,3)}" data-duration="{dur('assets/sfx/'+f)}" data-track-index="4" data-volume="{v}"></audio>' for i,f,st,v in sfx)
html=f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #E9E6DF; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080">
{hosts}
{vo}
      <audio id="music-bed" class="clip" src="assets/music/bed.wav" data-start="0" data-duration="{total}" data-track-index="3" data-volume="0.16" data-fade-in="0.4" data-fade-out="1.5"></audio>
{sfxs}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
open("index.html","w").write(html); print("total",total, starts)
