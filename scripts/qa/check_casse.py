#!/usr/bin/env python3
"""Piège Vercel : Linux est sensible à la casse. Une image en .JPG appelée
alors que le fichier est .jpg casse le déploiement. On ignore les liens
externes et les dossiers de travail (.claude, node_modules)."""
import re, os, sys
IGNORE = {'node_modules', '.git', '.venv', '.claude', '.next', 'dist'}
pb = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in IGNORE]
    for fn in files:
        if not fn.endswith(('.html', '.js')): continue
        p = os.path.join(root, fn)
        try: h = open(p, encoding='utf-8', errors='ignore').read()
        except Exception: continue
        for m in re.finditer(r'(?:src|href)="([^"]+\.(?:JPG|JPEG|PNG|WEBP|SVG))"', h):
            if not m.group(1).startswith('http'): pb.append((p, m.group(1)))
for p, u in pb[:15]: print(f"    ❌ {p} → {u}")
if not pb: print("    ✅ aucune extension en majuscules")
sys.exit(1 if pb else 0)
