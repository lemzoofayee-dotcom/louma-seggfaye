"""Prévient Bing (et Yandex, Seznam, Naver) via IndexNow que des pages ont changé.
ChatGPT Search et Copilot s'appuient sur l'index de Bing.
Usage :
  python3 scripts/seo/indexnow.py                 -> toutes les URL du sitemap
  python3 scripts/seo/indexnow.py page1.html ...  -> seulement ces pages
À lancer APRÈS la mise en ligne (la clé doit répondre sur le site)."""
import json, re, sys, urllib.request, pathlib
CLE = "4705bc60eb4dc7b2a6deff8dafe856f0"
HOTE = "seggfaye.com"
racine = pathlib.Path(__file__).resolve().parents[2]
if len(sys.argv) > 1:
    urls = [f"https://{HOTE}/" + a.lstrip("/") for a in sys.argv[1:]]
else:
    urls = re.findall(r"<loc>([^<]+)</loc>", (racine / "sitemap.xml").read_text(encoding="utf-8"))
corps = json.dumps({"host": HOTE, "key": CLE, "keyLocation": f"https://{HOTE}/{CLE}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=corps, headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req) as r:
    print(r.status, f"— {len(urls)} URL envoyées à IndexNow")
