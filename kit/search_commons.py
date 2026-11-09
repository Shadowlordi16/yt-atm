# Search Wikimedia Commons images, save candidates JSON + numbered contact sheet. usage: commons.py slug "query" [n]
import sys, json, urllib.request, urllib.parse, subprocess, os, io
UA={'User-Agent':'PaperEmpireResearch/0.1 (documentary sourcing)'}
slug,q=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 12
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=n,prop='imageinfo',iiprop='url|extmetadata|size',iiurlwidth=500,format='json'))
d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
pages=sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',0))
out=[]; os.makedirs('thumbs',exist_ok=True); files=[]
for i,p in enumerate(pages):
    ii=p['imageinfo'][0]; m=ii.get('extmetadata',{})
    import re
    art=re.sub('<[^>]+>','',m.get('Artist',{}).get('value',''))[:80]
    rec=dict(i=i,title=p['title'],url=ii['url'],thumb=ii['thumburl'],w=ii['width'],h=ii['height'],lic=m.get('LicenseShortName',{}).get('value',''),artist=art)
    out.append(rec); f=f'thumbs/{slug}_{i}.jpg'
    try:
        open(f,'wb').write(urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=UA),timeout=30).read()); files.append(f)
    except Exception as e: print('thumb fail',i,e)
json.dump(out,open(f'{slug}.json','w'),indent=1)
if files:
    subprocess.run(['magick','montage',*[f'{f}[320x200]' for f in files],'-tile','6x','-geometry','320x200+4+4','-label','%t','-pointsize','14',f'sheet_{slug}.jpg'])
for r in out: print(r['i'],r['w'],'x',r['h'],r['lic'],'|',r['title'][5:70])
