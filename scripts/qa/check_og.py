#!/usr/bin/env python3
"""Vérifie que chaque page a une og:image et que le fichier existe vraiment.
Tolère les deux ordres d'attributs (content= avant ou après property=)."""
import re, glob, os, sys
pages = glob.glob('*.html')+glob.glob('blog/*.html')+glob.glob('produits/*.html')+glob.glob('categories/*.html')
IGNORE = ('google', 'conditions-de-vente')
pb = []
for f in pages:
    if any(k in f for k in IGNORE): continue
    h = open(f, encoding='utf-8', errors='ignore').read()
    m = (re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"', h)
         or re.search(r'<meta[^>]*content="([^"]+)"[^>]*property="og:image"', h))
    if not m:
        pb.append((f, "aucune og:image")); continue
    u = m.group(1)
    if u.startswith('https://seggfaye.com'):
        loc = '.' + u.replace('https://seggfaye.com', '')
        if not os.path.exists(loc):
            pb.append((f, f"fichier introuvable : {u.split('/')[-1]}"))
for f, d in pb: print(f"    ❌ /{f} — {d}")
if not pb: print("    ✅ toutes les pages ont une image de partage valide")
sys.exit(1 if pb else 0)
