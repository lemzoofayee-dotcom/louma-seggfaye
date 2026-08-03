# Analyse hebdomadaire mots-clés Google Ads — 2026-08-03

> Analyse générée en environnement cloud, à partir des seuls CSV déjà commités (`mots_cles_resultats.csv` v1, `mots_cles_passerelle_v3.csv`). Aucun appel API Google Ads, aucun chiffre neuf généré.

## a) Verdict

Le cluster « France pure » (`mots_cles_resultats.csv`) est **déjà couvert à 100 %** sur les mots-clés à volume ≥300 en concurrence FAIBLE — le vrai gisement de la semaine est côté **passerelle FR/desserts** (`mots_cles_passerelle_v3.csv`) : 3 trous nets (beignet africain, lakh, bouillie de mil) + 1 quasi-trou (ngalakh, déjà esquissé mais pas en article dédié).

## b) Déjà couvert (validation) — mots-clés ≥300/mois

| Mot-clé | Volume | Concurrence | Couvert par |
|---|---|---|---|
| bissap | 60 500 | LOW | `blog/bissap-hibiscus-guide.html`, `produits/bissap-blanc.html`, `produits/bissap-rouge.html` |
| pain perdu | 90 500 | LOW | `blog/pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait | 74 000 | LOW | `blog/riz-au-lait-senegalais-sombi.html` |
| dégué | 12 100 | LOW | `blog/thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | LOW | `blog/recette-mafe-senegalais.html` |
| guedj | 8 100 | LOW | `blog/quest-ce-que-le-guedj.html`, `blog/les-7-guedj-du-senegal.html` + fiches `guej-*.html` |
| recette yassa poulet | 8 100 | LOW | `blog/recette-yassa-poulet.html` |
| cymbium | 6 600 | LOW | `blog/yeet-cymbium-maggi-africain.html`, `blog/guedj-ou-yeet-difference.html` |
| épicerie africaine | 5 400 | LOW | `blog/produits-senegalais-france.html` (title exact : « Épicerie africaine en ligne ») |
| jus de bissap | 4 400 | LOW | `blog/recette-jus-de-bissap.html` |
| thiakry | 4 400 | LOW | `blog/thiakry-degue-dessert-senegalais.html` |
| plat sénégalais | 4 400 | LOW | `blog/plats-senegalais.html` |
| beignet banane | 4 400 | LOW | `blog/beignet-banane-senegalais.html` |
| soumbala | 1 600 | LOW | `blog/guide-netetou-soumbala.html` |
| thiéré | 1 300 | LOW | `produits/thiere-champion.html` (fiche dédiée, couscous de mil) |
| niébé | 1 300 | LOW | `produits/niebe-saloum.html` (fiche dédiée) |
| lakh (tag interne) | — | — | déjà taggé « 🍽️ Lakh » sur 2 fiches produits (voir trous) mais **sans page dédiée** |
| yeet | 1 000 | LOW | `blog/yeet-cymbium-maggi-africain.html` — seul CPC réellement commercial (1,45–4,33€) |
| netetou | 720 | LOW | `blog/guide-netetou-soumbala.html`, `blog/acheter-netetou-france.html` |
| soupoukandja | 720 | LOW | `blog/recette-soupoukandja.html` |
| couscous de mil | 590 | LOW | `produits/thiere-champion.html` |
| nététou | 590 | LOW | (variante orthographique, idem netetou) |
| recette thieboudienne | 590 | LOW | `blog/recette-thieboudienne-authentique.html` |
| beignets sénégalais | 390 | LOW | `blog/beignet-banane-senegalais.html` (variante plurielle proche) |
| sombi | 390 | LOW | `blog/riz-au-lait-senegalais-sombi.html` |
| mbakhal saloum | 320 | LOW | `blog/recette-mbakhalou-saloum.html` |
| dessert sénégalais | 480 | LOW | `blog/thiakry-degue-dessert-senegalais.html` (h1 cible déjà ce terme générique) |

## c) Trous priorisés — action à valider par Lamine

| Mot-clé | Volume | Concurrence | Angle d'article proposé | Produit(s) à lier |
|---|---|---|---|---|
| **beignet africain** | 1 900 | LOW | Article hub « Les beignets africains/sénégalais : les incontournables » (référence générique, alors que le site ne couvre que le beignet banane spécifiquement) | `produits/pastels.html` (chausson frit), lien vers `blog/beignet-banane-senegalais.html` |
| **lakh** | 1 300 | LOW | Article recette/découverte « Le lakh, la bouillie-dessert au mil et lait caillé » — **graphie déjà validée sur le site** (tag « 🍽️ Lakh » présent sur `produits/arraw-dugup.html` et `produits/lem-miel.html`, pointant vers un guide externe `guide.seggfaye.com/plats/lakh` qui n'a pas d'équivalent sur le blog principal) | `produits/arraw-dugup.html`, `produits/lem-miel.html` |
| **bouillie de mil** | 1 000 | LOW | Article « Bouillie de mil (fondé) : le petit-déjeuner traditionnel sénégalais » — même logique que ci-dessus : tag « 🍽️ Fonde » déjà présent sur `produits/lem-miel.html` sans page dédiée | `produits/sankal-duggup.html`, `produits/lem-miel.html` |

**Quasi-trou à surveiller (hors tableau principal, coverage partielle) :**
- **ngalakh** (590/mois, LOW) — déjà traité en sous-section (`<h3>Le ngalakh</h3>`) dans `blog/pain-de-singe-bouye-baobab.html`, mais ce n'est pas une page dédiée qui cible le mot-clé en H1/meta. Option basse priorité : soit muscler cette section, soit la détacher en article autonome si le volume justifie l'effort — à arbitrer par Lamine, pas urgent vu la coexistence avec lakh/bouillie de mil qui sont des trous plus francs.

## d) Insights stratégiques

- **Le cluster France pur est saturé positivement** : sur `mots_cles_resultats.csv`, aucun mot-clé ≥300/mois en concurrence FAIBLE n'est sans contenu. Le SEO organique sur ce périmètre est à maintenir (suivi de positions), pas à combler.
- **La stratégie « passerelle » fonctionne mais s'arrête à mi-chemin** : les 2 têtes de gondole (pain perdu 90,5k, riz au lait 74k) et les gros cousins sénégalais (dégué 12,1k, beignet banane 4,4k) sont bien couverts. Les 3 trous identifiés sont exactement les cousins de second rang du même cluster — logique de compléter la série pendant que le format marche.
- **Piège fonio confirmé** : CPC 20,70–172,75€ (homonyme finance/nutrition anglophone). Ne jamais enchérir sur « fonio » en Ads — le contenu existant (`blog/fonio-cereale-sans-gluten.html`) doit rester 100% organique.
- **Les requêtes à CPC ~0€** (guedj, thiakry, plat sénégalais, soumbala, etc.) sont purement informationnelles → à traiter en SEO organique, pas en budget Ads. Seul **yeet** (1,45–4,33€) a un vrai signal d'intention d'achat/Ads.
- **Le cluster diaspora « acheter guedj » à volume 0** dans cette étude (géo France) est normal et attendu — ce n'est pas un échec de `blog/acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html`, ces articles ciblent une autre géo non couverte par cette étude.
- **Signal intéressant côté fiches produits** : plusieurs fiches (`arraw-dugup.html`, `lem-miel.html`, `guerte-noflay.html`...) taggent déjà des plats (lakh, fonde, ceebu-yapp, thiou, dibi, domoda, ndambe...) vers un guide externe `guide.seggfaye.com/plats/*`. Ça confirme que ces noms de plats sont déjà « pré-validés » côté marque — bonne base pour prioriser les prochains articles sans repartir de zéro sur les graphies.

## e) Limites

- Analyse basée uniquement sur 2 fichiers CSV commités (v1 France + passerelle v3). Pas d'accès aux scripts `.py` ni à l'API Google Ads en cloud — aucune donnée nouvelle générée, aucune vérification de fraîcheur des volumes.
- Long tail à volume <300/mois (fonio grains, cymbium olla, kethiakh, etc.) et lignes à volume 0 exclues du tableau des trous par choix de seuil, mais restent listées dans les CSV sources si besoin de détail.
- Coverage jugée sur la présence d'un article/fiche dédié ; pas de vérification du positionnement Google réel (rankings) — validation purement structurelle (contenu existe / n'existe pas).
- Les graphies « lakh » et « fondé/bouillie de mil » s'appuient sur un usage déjà présent ailleurs sur le site (tags produits) ; elles restent à reconfirmer avec Lamine avant publication d'un article, comme toute graphie de plat.

**Résumé : les 3 trous prioritaires de la semaine sont « beignet africain » (1 900/mois), « lakh » (1 300/mois) et « bouillie de mil » (1 000/mois), tous en concurrence FAIBLE et sans article dédié, alors que le cluster France pur est déjà entièrement couvert.**
