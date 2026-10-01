"""Met à jour les <lastmod> du sitemap avec la date du dernier commit de chaque page.
Usage : python3 scripts/seo/maj_lastmod.py   (à lancer avant un commit qui touche des pages)"""
import re, subprocess, pathlib
racine = pathlib.Path(__file__).resolve().parents[2]
sitemap = racine / "sitemap.xml"
s = sitemap.read_text(encoding="utf-8")

def fichier(url):
    chemin = url.replace("https://seggfaye.com/", "")
    if chemin == "" or chemin.endswith("/"):
        chemin += "index.html"
    return racine / chemin

def date_git(f):
    r = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(f)], cwd=racine, capture_output=True, text=True)
    return r.stdout.strip()

n = 0
def remplace(m):
    global n
    loc, ancien = m.group(1), m.group(2)
    f = fichier(loc)
    d = date_git(f) if f.exists() else ""
    if d and d != ancien:
        n += 1
        return m.group(0).replace(f"<lastmod>{ancien}</lastmod>", f"<lastmod>{d}</lastmod>")
    return m.group(0)

s = re.sub(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", remplace, s)
sitemap.write_text(s, encoding="utf-8")
print(f"{n} dates mises à jour")
