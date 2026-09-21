"""Contrôle hebdo : le guide et la boutique ne doivent plus se concurrencer.

Trois vérifications, en une commande :
  1. chaque fiche produit du guide déclare bien la page boutique comme référence
     (canonical), et cette page répond 200 ;
  2. aucune page du site ne renvoie une erreur (sitemap complet) ;
  3. les requêtes où PLUSIEURS pages sortent en même temps (cannibalisation),
     d'après les vraies données Search Console.

Usage :  python3 scripts/seo/check_cannibalisation.py
         (ajouter --rapide pour sauter le contrôle du sitemap)
"""
import csv
import collections
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "LoumaBot/1.0 (verification interne)"}
RAPIDE = "--rapide" in sys.argv


def lire(url, timeout=25):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return getattr(e, "code", 0), ""


def code(url):
    return lire(url, timeout=20)[0]


erreurs = 0

# ── 1. Canoniques du guide ────────────────────────────────────────────────────
print("1/3 · Fiches du guide : la boutique est-elle déclarée comme référence ?")
_, sm = lire("https://guide.seggfaye.com/sitemap.xml")
fiches = sorted(set(re.findall(r"https://guide\.seggfaye\.com/produits/[a-z0-9-]+", sm)))
if not fiches:
    print("    ⚠️ sitemap du guide illisible — contrôle sauté")
else:
    def verifier(u):
        _, html = lire(u)
        m = re.search(r'rel="canonical" href="([^"]+)"', html)
        if not m:
            return u, "aucune canonique", 0
        cano = m.group(1)
        if "seggfaye.com/produits/" not in cano or "guide." in cano:
            return u, f"pointe vers {cano}", 0
        return u, cano, code(cano)

    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(verifier, fiches))
    mauvaises = [(u, c, s) for u, c, s in res if s != 200]
    if mauvaises:
        erreurs += 1
        print(f"    ❌ {len(mauvaises)} fiche(s) à corriger :")
        for u, c, s in mauvaises[:10]:
            print(f"       {u} → {c} ({s})")
    else:
        print(f"    ✅ {len(res)} fiches pointent vers une page boutique qui répond")

# ── 2. Sitemap de la boutique ────────────────────────────────────────────────
print("\n2/3 · Pages du site : tout répond-il ?")
if RAPIDE:
    print("    (sauté)")
else:
    _, sm2 = lire("https://seggfaye.com/sitemap.xml")
    urls = re.findall(r"<loc>([^<]+)</loc>", sm2)
    with ThreadPoolExecutor(10) as ex:
        codes = list(ex.map(code, urls))
    ko = [(u, c) for u, c in zip(urls, codes) if c != 200]
    if ko:
        erreurs += 1
        print(f"    ❌ {len(ko)} page(s) en erreur :")
        for u, c in ko[:10]:
            print(f"       {c}  {u}")
    else:
        print(f"    ✅ {len(urls)} pages, aucune erreur")

# ── 3. Cannibalisation (données Search Console) ──────────────────────────────
print("\n3/3 · Requêtes où plusieurs pages se font concurrence")
csv_path = os.path.join(BASE, "gsc-page-queries.csv")
if not os.path.exists(csv_path):
    print("    ⚠️ lancer d'abord : scripts/ads/.venv/bin/python scripts/seo/gsc_pull.py")
else:
    par_requete = collections.defaultdict(list)
    for r in csv.DictReader(open(csv_path)):
        par_requete[r["requete"]].append((r["page"], int(r["impressions"]), float(r["position"])))
    cas = []
    for q, v in par_requete.items():
        total = sum(i for _, i, _ in v)
        # concurrence réelle : au moins 2 pages bien placées et du volume
        proches = [x for x in v if x[2] <= 20]
        if total >= 50 and len(proches) >= 2:
            cas.append((total, q, sorted(proches, key=lambda x: x[2])))
    cas.sort(reverse=True)
    if cas:
        print(f"    ⚠️ {len(cas)} requête(s) à surveiller (les 8 plus grosses) :")
        for total, q, v in cas[:8]:
            print(f"       « {q} » — {total} impressions")
            for p, i, pos in v[:4]:
                print(f"           pos {pos:5.1f}  {i:4d} impr  {p.replace('https://', '')}")
    else:
        print("    ✅ aucune concurrence interne notable")

print("\n" + ("❌ À CORRIGER" if erreurs else "✅ RIEN À CORRIGER CÔTÉ TECHNIQUE"))
sys.exit(1 if erreurs else 0)
