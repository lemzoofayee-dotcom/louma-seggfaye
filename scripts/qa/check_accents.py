#!/usr/bin/env python3
"""Repère les mots français écrits sans accent dans le TEXTE VISIBLE.
Le dictionnaire est bâti à partir des pages du site elles-mêmes : on ne
corrige jamais vers une graphie étrangère au site. Les mots ambigus
(participe vs présent) et les graphies wolof sont exclus."""
import re, glob, collections, unicodedata, sys
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
def visible(h):
    """Texte lu par un humain + texte des donnees structurees JSON-LD,
    que Google lit aussi (angle mort repere le 17/09/2026)."""
    ld = ' '.join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S))
    h = re.sub(r'<(script|style).*?</\1>', '', h, flags=re.S)
    return ld + ' ' + ''.join(p for p in re.split(r'(<[^>]+>)', h) if not p.startswith('<'))

pages = glob.glob('*.html')+glob.glob('blog/*.html')+glob.glob('produits/*.html')+glob.glob('categories/*.html')
acc = collections.Counter()
for f in pages:
    for m in re.findall(r"\b[A-Za-zÀ-ÿ']{4,}\b", visible(open(f, encoding='utf-8', errors='ignore').read())):
        if re.search(r'[àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]', m): acc[m.lower()] += 1
cand = collections.defaultdict(collections.Counter)
for w, n in acc.items(): cand[strip(w)][w] += n

# graphies wolof / produits : intouchables (validées par Lamine)
WOLOF = {'netetou','netetu','soumbala','nere','thiere','thiakry','guedj','guej','yeet','yet','bissap',
 'bouye','diwnior','diwtir','kethiakh','sompate','thiof','yakh','kong','pagne','cipakh','niebe','mafe',
 'seche','seches','sechee','sechees','prepare','melange','cote','cotes','sale','ferme','marche','pate',
 # graphies wolof : seul Lamine tranche
 'thieboudienne','thiebou','dieye','diargne','sompatt','yekem','keciax','ciakri','yoxos','tuffa',
 # mots francais valides tels quels : ne JAMAIS accentuer automatiquement
 'jeune','granules','tache','mure','cure','tire','acre','are','cotes','entre','eleve','reste','age'}
dico = {}
for nu, formes in cand.items():
    if nu in WOLOF or len(nu) < 4: continue
    top = formes.most_common()
    if len(top) > 1 and not (top[0][1] >= 5*top[1][1] and top[0][1] >= 8): continue
    ac = top[0][0]
    if top[0][1] < 3: continue
    # on n'automatise QUE si l'accent ne porte pas sur la dernière lettre (sinon ambiguïté participe/présent)
    nfc = unicodedata.normalize('NFC', ac)
    pos = [i for i, c in enumerate(nfc) if unicodedata.normalize('NFD', c) != c]
    if pos and pos[-1] == len(nfc)-1: continue
    dico[nu] = ac
if not dico: print("    ✅ rien à signaler"); sys.exit(0)
pat = re.compile(r"\b(" + "|".join(sorted(map(re.escape, dico), key=len, reverse=True)) + r")\b", re.I)
pb = []
for f in pages:
    n = len(pat.findall(visible(open(f, encoding='utf-8', errors='ignore').read())))
    if n: pb.append((n, f))
pb.sort(reverse=True)
for n, f in pb[:12]: print(f"    ❌ /{f} — {n} mot(s) sans accent")
if not pb: print(f"    ✅ aucun mot sans accent ({len(dico)} mots surveillés)")
sys.exit(1 if pb else 0)
