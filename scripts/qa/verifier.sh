#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────
#  VÉRIFICATION COMPLÈTE DU SITE — Louma by Seggfaye
#  Usage :  ./scripts/qa/verifier.sh
#  Objectif : zéro erreur avant chaque mise en ligne.
# ──────────────────────────────────────────────────────────────
set -uo pipefail
cd "$(dirname "$0")/../.."
PAGES=('*.html' 'blog/*.html' 'produits/*.html' 'categories/*.html')
ERR=0

echo "┌────────────────────────────────────────────────┐"
echo "│  VÉRIFICATION DU SITE                          │"
echo "└────────────────────────────────────────────────┘"

echo ""
echo "1/5 · Liens et images (lychee)"
if command -v lychee >/dev/null; then
  OUT=$(lychee --offline --include-fragments --no-progress \
        --exclude-path node_modules --exclude-path .git --exclude-path .claude \
        --root-dir "$(pwd)" "${PAGES[@]}" 2>&1)
  REST=$(echo "$OUT" | grep ERROR | grep -v "#produits")   # /#produits : ancre reelle, lychee la resout mal
  echo "$OUT" | tail -1 | sed 's/^/    /'
  if [ -n "$REST" ]; then echo "$REST" | sed 's/^/    /'; ERR=1; else echo "    ✅ aucun lien casse"; fi
else
  echo "    ⚠️ lychee absent — brew install lychee"
fi

echo ""
echo "2/5 · Validité HTML (html-validate)"
if npx --yes html-validate "${PAGES[@]}" >/tmp/hv.txt 2>&1; then
  echo "    ✅ aucune erreur"
else
  grep -E "error" /tmp/hv.txt | grep -v "More information" | sed 's/^/    /' | head -20; ERR=1
fi

echo ""
echo "3/5 · Piège Vercel : extensions en MAJUSCULES"
python3 scripts/qa/check_casse.py || ERR=1

echo ""
echo "4/5 · Images de partage (og:image)"
python3 scripts/qa/check_og.py || ERR=1

echo ""
echo "5/5 · Accents français manquants"
python3 scripts/qa/check_accents.py || ERR=1

echo ""
if [ "$ERR" -eq 0 ]; then echo "✅ TOUT EST PROPRE — bon pour la mise en ligne"; else echo "❌ CORRIGER AVANT DE PUBLIER"; fi
exit $ERR
