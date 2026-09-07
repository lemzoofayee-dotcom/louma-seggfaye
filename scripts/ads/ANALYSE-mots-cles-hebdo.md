# Analyse mots-clés Google Ads — Lundi 07/09/2026

> **Analyse cloud, aucune donnée neuve.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 4 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`) — **inchangés depuis le 24/08** (aucun commit sur `scripts/ads/*.csv` depuis 2 semaines).
> Croisé avec : `ls blog/` (45 articles) et `ls produits/` (53 fiches).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**Deuxième semaine sans donnée fraîche et toujours aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) — le catalogue de contenu couvre l'intégralité des CSV actuels ; la vraie priorité n'est plus l'écriture d'articles mais de **relancer un pull Keyword Planner en local** et de **merger/fermer le PR #24** (identique, ouvert depuis le 31/08) pour ne pas empiler deux PR sur le même sujet.

---

## 2. Déjà couvert (validation)

Tous les mots-clés à volume ≥ 300/mois des 4 CSV ont un article ou une fiche dédiée. Rien n'a bougé depuis le 31/08 côté contenu ads-pertinent (les 5 commits de la quinzaine sont des retouches de titres/meta sur des fiches produits, pas de nouveaux articles).

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide.html`, `recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7 articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet.html` |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere.html` |
| cymbium | 5 400-6 600 | FAIBLE | `yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| épicerie africaine | 5 400 | FAIBLE | `produits-senegalais-france.html` (le terme est dans le `<title>`) |
| fonio | 5 400 | MOYENNE | `fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet banane / africain | 4 400 / 1 900 | FAIBLE | `beignet-banane-senegalais.html` (« beignet africain », « beignets senegalais » présents dans les keywords JSON-LD, pas encore dans le titre — reste une piste d'optimisation légère, pas un trou) |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` + fiche produit |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| pain de singe / bouye | 1 300-3 600 | MOYENNE/FAIBLE | `pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum.html` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` |
| netetou / nététou | 590-720 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| tamarin jus | 320-390 | MOYENNE | `jus-de-tamarin-dakhar.html` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| poisson kong | 260-320 | FAIBLE | `poisson-kong.html` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, juste un référencement plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) dans les 4 CSV actuels — inchangé depuis le 31/08.

Pistes secondaires hors critère strict, à garder en réserve :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique ; CPC réel (0,38-0,69 €) confirme l'intérêt commercial | Angle de niche « pâte d'arachide sénégalaise maison » (moins concurrentiel) — à lier à `tigadegue`/`guerte-noflay` |
| beignet africain / beignets sénégalais | 1 900 / 390 | FAIBLE | Déjà dans les keywords JSON-LD de `beignet-banane-senegalais.html`, mais pas dans le `<title>`/H1 → capte le terme faiblement | Retitrer/ajouter un H2 « beignet africain » à l'article existant plutôt que créer une nouvelle page (éviter la cannibalisation) — *graphie à confirmer avec Lamine si variante autre que « beignet banane »* |
| graine de néré | 210 | FAIBLE | Sous le seuil de 300/mois | Déjà mentionné dans 5 articles — pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **Deux semaines sans donnée fraîche = rendement décroissant sur l'analyse cloud.** Le pull Keyword Planner date du 24/08 (`etude_mots_cles_v2.py`, refresh token OAuth à 7 jours en mode « test »). Recommandation : passer l'écran de consentement Google Cloud Console de *Testing* à *In production* pour arrêter de perdre le refresh token chaque semaine, sinon cette routine tourne à vide sur les mêmes 4 CSV.
- **PR à nettoyer avant celui-ci.** Le PR **#24** (`ads/analyse-hebdo-2026-08-31`, ouvert depuis le 31/08) porte exactement le même fichier (`scripts/ads/ANALYSE-mots-cles-hebdo.md`) avec une conclusion quasi identique (zéro trou strict). Merger l'un des deux et fermer l'autre pour éviter d'empiler des PR ads redondants — le même écueil avait déjà été signalé le 24/08 (#11, #9, #3).
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter » ne se cherche pas en géo France.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois. Normal, cette géo ne capture pas la diaspora — les articles `acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html` ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** (1,06-4,33 €). Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads, sauf éventuellement yeet.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Zéro donnée neuve depuis 2 semaines.** Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les CSV déjà commités (le plus récent date du 24/08). Un vrai rafraîchissement Keyword Planner nécessite une session locale (`etude_mots_cles.py` / `etude_mots_cles_v2.py` / `etude_passerelle_v3.py`).
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer d'urgent cette semaine — le stock de trous est vide pour la 2e semaine consécutive. Deux actions non-contenu prioritaires : **(1)** merger ou fermer le PR #24 pour ne garder qu'une seule analyse ads en attente, **(2)** relancer un pull Keyword Planner en local (et fixer l'expiration du refresh token) avant la prochaine analyse cloud, sinon celle-ci tournera en boucle sur les mêmes chiffres.

**Les 3 trous prioritaires de la semaine : aucun** — le seul mot-clé à surveiller est « beignet africain » (1 900/mois, FAIBLE), déjà partiellement capté en metadata mais pas encore en titre.
