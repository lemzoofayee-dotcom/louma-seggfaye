"""6/6 · Liens internes : aucune URL accentuée, aucune cible manquante.

Pourquoi ce contrôle existe : le 17/09/2026, une passe d'accentuation a accentué les
URLs dans les JSON-LD / canonical / og:image → 18 pages en 404 dans Search Console
et 2 images de partage cassées. Ce script rend l'erreur impossible à republier.
"""
import glob
import os
import re
import sys
import unicodedata

PAGES = (glob.glob('*.html') + glob.glob('blog/*.html') + glob.glob('produits/*.html')
         + glob.glob('categories/*.html') + glob.glob('saloum/*.html') + glob.glob('*.xml'))
URL = re.compile(r'"(?:https://seggfaye\.com)?(/[^"#?\s]*\.(?:html|jpg|jpeg|png|webp|xml|css|js))(?:#[^"]*)?"')

accentuees, manquantes = [], []
for f in PAGES:
    texte = open(f, encoding='utf-8', errors='ignore').read()
    for chemin in set(URL.findall(texte)):
        if any(unicodedata.category(c) == 'Mn' for c in unicodedata.normalize('NFD', chemin)):
            accentuees.append((f, chemin))
        elif not os.path.exists(chemin.lstrip('/')):
            manquantes.append((f, chemin))

if accentuees:
    print(f"    ❌ {len(accentuees)} URL(s) ACCENTUÉE(S) — elles feront des 404 :")
    for f, u in accentuees[:10]:
        print(f"       {u}   (dans {f})")
    print("       → une URL ne s'accentue JAMAIS, même si le mot s'écrit avec un accent.")
if manquantes:
    print(f"    ❌ {len(manquantes)} lien(s) vers un fichier qui n'existe pas :")
    for f, u in manquantes[:10]:
        print(f"       {u}   (dans {f})")
if not accentuees and not manquantes:
    print(f"    ✅ liens internes OK (aucune URL accentuée, aucune cible manquante)")

sys.exit(1 if (accentuees or manquantes) else 0)
