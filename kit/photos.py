"""Stage 4: download + treat every photo listed in photos.json (fast: cached 1920/960 px, 4 at a time).
photos.json = {"name": "File:Exact Commons title.jpg", ...}   names become assets/img/<name>.jpg
  - a name starting with "p_" is a portrait (keeps its aspect, for portrait())
  - a name starting with "logo_" stays a flat .png mark
usage (in the video folder): python3 ../kit/photos.py
Find titles first:  python3 ../kit/search_commons.py <slug> "search words" 10   (writes sheet_<slug>.jpg to look at)"""
import json, os, subprocess, sys
KIT = os.path.dirname(os.path.abspath(__file__))
want = json.load(open("photos.json"))
want = {k: v for k, v in want.items() if not k.startswith("_")}
need = {n: t for n, t in want.items() if not os.path.exists(f"raw/{n}.src")}
if need:
    r = subprocess.run([sys.executable, f"{KIT}/fetch_commons.py", "raw/_dl", *need.values()], capture_output=True, text=True)
    print(r.stdout.strip())
    for n, t in need.items():
        p = f"raw/_dl/{t[5:].replace(' ', '_')}"
        if os.path.exists(p) and os.path.getsize(p) > 5000:
            os.replace(p, f"raw/{n}.src")
# credits for the video description
meta = subprocess.run([sys.executable, "-c", f"""
import json,urllib.request,urllib.parse,re
t={json.dumps(list(want.values()))}
q='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',titles='|'.join(t[:50]),prop='imageinfo',iiprop='extmetadata',format='json'))
p=json.load(urllib.request.urlopen(urllib.request.Request(q,headers={{'User-Agent':'PaperEmpireResearch/0.2'}}),timeout=30))['query']['pages'].values()
out={{}}
for x in p:
    m=x.get('imageinfo',[{{}}])[0].get('extmetadata',{{}})
    out[x['title']]=dict(artist=re.sub('<[^>]+>','',m.get('Artist',{{}}).get('value',''))[:90],lic=m.get('LicenseShortName',{{}}).get('value',''))
print(json.dumps(out))"""], capture_output=True, text=True).stdout
try:
    lic = json.loads(meta)
    with open("CREDITS.md", "w") as f:
        f.write("# Photo credits (paste into the video description)\n\n")
        for n, t in want.items():
            m = lic.get(t, {})
            f.write(f"- {t[5:]} by {m.get('artist','?')}, {m.get('lic','?')}, via Wikimedia Commons\n")
except Exception as e:
    print("credits lookup failed:", e)
os.makedirs("video/assets/img", exist_ok=True)
missing = []
for n in want:
    src = f"raw/{n}.src"
    if not os.path.exists(src): missing.append(n); continue
    if n.startswith("logo_"):
        subprocess.run(["magick", src, "-colorspace", "gray", f"video/assets/img/{n}.png"]); continue
    vf = ("scale=1600:-2,hue=s=0,eq=contrast=1.2,vignette=PI/6,noise=alls=5:allf=t" if n.startswith("p_") else
          "scale=2304:1296:force_original_aspect_ratio=increase,crop=2304:1296,hue=s=0,eq=contrast=1.25:brightness=-0.02,vignette=PI/5,noise=alls=6:allf=t")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", vf, "-q:v", "3", f"video/assets/img/{n}.jpg"])
print(f"{len(want) - len(missing)}/{len(want)} photos ready in video/assets/img" + (f" · MISSING: {missing}" if missing else ""))
