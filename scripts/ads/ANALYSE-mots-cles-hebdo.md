# Analyse mots-clés Google Ads — Lundi 19/10/2026

> **Analyse cloud, aucune donnée neuve générée.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 5 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`, `mots_cles_elargie_v4.csv`).
> **Pas de nouveau CSV cette semaine.** `mots_cles_elargie_v4.csv` (ajouté le 30/09) reste la dernière étude — aucun pull local depuis. Rien à analyser de neuf côté données.
> Croisé avec : `ls blog/` (55 articles + `index.html`), `ls produits/` (55 fiches), et les pages racine pertinentes (`epicerie-africaine.html`, `poissons-prix.html`, `atlas-poissons-wolof.html`).
> **Nouveauté côté catalogue** : `blog/recette-thiebou-diagga.html` a été publié le 14/10 (thiebou djeun diagga, sans guedj ni yeet) — postérieur au rapport du 12/10. Vérifié ci-dessous : ça ne referme aucun trou (le sujet n'en était pas un) mais ça enrichit la couverture « recette thieboudienne / plat sénégalais ».
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**6e semaine consécutive sans trou strict** — aucune donnée neuve à croiser (toujours les mêmes 5 CSV, le dernier pull remonte au 30/09) et le catalogue (55 articles + 55 fiches) couvre toujours l'intégralité des mots-clés ≥300/mois en concurrence faible ; la seule nouveauté est un article de plus (`recette-thiebou-diagga.html`, 14/10) qui ne change pas le constat.

---

## 2. Déjà couvert (validation)

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `blog/pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `blog/riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `blog/bissap-hibiscus-guide.html`, `blog/recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html` |
| tilapia | 18 100 | FAIBLE | `produits/tilapia-rouge.html` |
| recette mafé | 9 900 | FAIBLE | `blog/recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7+ articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| yassa poulet | 8 100 | FAIBLE | `blog/recette-yassa-poulet.html` |
| néré | 6 600 | FAIBLE | `blog/quest-ce-que-le-nere.html` |
| cymbium | 5 400-6 600 | FAIBLE | `blog/yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| poisson capitaine | 5 400 | FAIBLE | `produits/diane-capitaine.html`, `produits/beurre-capitaine.html` |
| épicerie africaine | 5 400 | FAIBLE | `epicerie-africaine.html` (page racine) |
| fonio | 5 400 | MOYENNE | `blog/fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `blog/beignet-banane-senegalais.html` |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html`, `blog/plats-senegalais.html` |
| jus de bissap | 4 400 | FAIBLE | `blog/recette-jus-de-bissap.html` |
| pain de singe | 3 600 | FAIBLE | `blog/pain-de-singe-bouye-baobab.html` |
| soumbala | 1 600 | FAIBLE | `blog/guide-netetou-soumbala.html` |
| bissap blanc | 1 600 | MOYENNE | `blog/bissap-blanc.html` + fiche produit |
| thiébou yapp | 1 300 | FAIBLE | `blog/thiebou-yapp-riz-viande-senegalais.html` |
| bouye | 1 300 | FAIBLE | `blog/pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| niébé (Îles du Saloum) | 1 300 | FAIBLE | `blog/niebe-haricot-saloum.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `blog/thiere-couscous-mil-senegalais.html` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `blog/lakh-bouillie-mil-lait-caille.html`, `blog/fonde-araw-bouillie-mil-senegalais.html` |
| poisson braisé | 1 000 | FAIBLE | `blog/poisson-braise.html` |
| yeet | 1 000 | FAIBLE | `blog/yeet-cymbium-maggi-africain.html`, `blog/guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `blog/ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `blog/domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `blog/recette-jus-de-bouye.html` |
| netetou / nététou | 390-720 | FAIBLE | `blog/acheter-netetou-france.html`, `blog/guide-netetou-soumbala.html`, fiche `netetu-mix` |
| soupoukandja | 590-720 | FAIBLE | `blog/recette-soupoukandja.html` |
| thiof | 590 | FAIBLE | `produits/thiof-decoupe.html` |
| couscous de mil | 590 | FAIBLE | `blog/thiere-couscous-mil-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `blog/recette-thieboudienne-authentique.html` + `blog/recette-thiebou-diagga.html` (nouveau, 14/10) |
| ngalakh | 590 | FAIBLE | `blog/ngalakh-dessert-senegalais.html` |
| poisson africain | 480 | FAIBLE | `poissons-prix.html` (page racine) |
| dessert sénégalais | 480 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html`, `blog/ngalakh-dessert-senegalais.html` |
| oseille de guinée (= bissap) | 390 | FAIBLE | `blog/bissap-hibiscus-guide.html` (synonyme) |
| beignets sénégalais | 390 | FAIBLE | `blog/beignet-banane-senegalais.html` |
| sombi | 390 | FAIBLE | `blog/riz-au-lait-senegalais-sombi.html` |
| mbakhal(ou) saloum | 320 | FAIBLE | `blog/recette-mbakhalou-saloum.html` |

*Concurrence ÉLEVÉE mais déjà couvertes malgré tout (pas des trous, référencement juste plus dur) : pâte d'arachide (4 400), kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000), bissap rouge (390).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article/fiche) dans les 5 CSV disponibles. 6e semaine d'affilée — constat inchangé faute de données neuves.

Pistes sous le seuil, à garder en réserve (aucune n'est urgente) :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Angle si jamais / produit à lier |
|---|---:|---|---|---|
| buffet africain | 90 | FAIBLE | Sous le seuil de 300/mois | Angle « coffret buffet africain pour les fêtes » lié à `produits/pack-saloum.html` — *à valider avec Lamine avant tout nom de plat précis* |
| sardinelle | 260 | FAIBLE | Sous le seuil, déjà couvert quand même | `blog/kethiakh-sardinelle-fumee-senegal.html` — pas besoin de nouvel article |
| poisson fumé africain | 140 | FAIBLE | Sous le seuil, déjà couvert quand même | Articles guedj fumé existants — pas besoin de nouvel article |
| épicerie fine africaine | 40 | FAIBLE | Sous le seuil | Déjà proche d'`epicerie-africaine.html` — pas de nouvel article nécessaire |
| graine de néré | 170 | FAIBLE | Sous le seuil, déjà mentionné dans les articles néré/soumbala | Pas besoin d'article dédié |

Aucune de ces pistes ne justifie une création cette semaine.

---

## 4. Insights stratégiques

- **Rien de neuf côté données depuis trois semaines maintenant** (dernier pull : `mots_cles_elargie_v4.csv`, 30/09). Les deux pistes locales proposées la semaine dernière restent d'actualité et n'ont pas été relancées : (1) un pull Keyword Planner en géo USA/Canada pour vraiment valider le cluster diaspora « acheter » (structurellement à 0 en géo France) ; (2) un repull saisonnier des requêtes « recette tabaski »/« recette korité »/« recette ramadan africaine » (10/mois actuellement) après la prochaine fête religieuse.
- **Le nouvel article `recette-thiebou-diagga.html` (14/10) renforce un mot-clé déjà couvert** (« recette thieboudienne », 590/mois, FAIBLE) plutôt que d'en ouvrir un nouveau — bon réflexe éditorial (variante sans guedj/yeet pour élargir l'audience), mais ça ne change pas le verdict des trous.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter »/diaspora reste à 0 en géo France, c'est normal.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois dans cette géo. Les articles diaspora (`acheter-guedj-amerique-nord.html`, `acheter-guedj-europe.html`) ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** dans les CSV disponibles. Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console** — elle recoupe uniquement les 5 CSV déjà commités dans `scripts/ads/`.
- **Aucune donnée neuve cette semaine** : les CSV analysés sont identiques à ceux du rapport du 12/10. Ce verdict ne vaut que pour ces mêmes mots-clés testés il y a 3 semaines.
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer cette semaine. Priorité pour la prochaine session locale : relancer un pull Keyword Planner (geo USA/Canada pour le cluster diaspora, et/ou nouvelles seeds) — l'étude cloud ne peut rien analyser de neuf tant qu'aucun CSV n'est ajouté.

**Les 3 trous prioritaires de la semaine : aucun** — 6e semaine sans donnée neuve à croiser, le catalogue (55 articles + 55 fiches) couvre toujours tous les mots-clés ≥300/mois en concurrence faible ; seule piste de réserve sous le seuil : « coffret buffet africain pour les fêtes » (90/mois, cluster fêtes encore jeune).
