# Données Search Console réelles (usage LOCAL)

Objectif : avoir les **vraies** données GSC (positions, CTR, impressions) au lieu d'estimations.

⚠️ **Le repo est PUBLIC** → les données de trafic (`gsc-data.md`, `gsc-queries.csv`) et le
jeton (`gsc_token.json`) sont **gitignorés** et **NE DOIVENT JAMAIS être commités**
(sinon les concurrents voient tes requêtes/positions). Elles restent sur le Mac de Lamine.

## Fichiers
- `get_gsc_token.py` — autorisation OAuth (à lancer **une seule fois**). Crée `gsc_token.json` (local, gitignoré).
- `gsc_pull.py` — récupère 90 j de données (propriété Domaine `sc-domain:seggfaye.com`) → `gsc-data.md` + `gsc-queries.csv` (locaux).

## Rafraîchir les données (local)
```bash
scripts/ads/.venv/bin/python scripts/seo/gsc_pull.py
```
Puis l'analyse SEO se fait **en local** (session avec Claude) à partir de `gsc-data.md`.

## Conséquence (repo public)
La routine SEO **cloud** ne peut PAS lire ces données (elles restent locales). Donc l'analyse de
positionnement se fait **en local** (on-demand avec Claude, ou via un launchd hebdo sur le Mac).
La routine cloud, si conservée, doit se limiter aux **idées de contenu** et **ne jamais présenter
d'estimations de position comme des faits** (elle n'a pas accès à GSC).
