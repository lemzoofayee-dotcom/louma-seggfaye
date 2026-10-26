# Analyse mots-clés Google Ads — Lundi 26/10/2026

> **Analyse cloud, aucune donnée neuve générée.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 6 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`, `mots_cles_elargie_v4.csv`, et **nouveau** : `mots_cles_fetes_v5.csv`).
> **Nouveauté cette semaine** : `mots_cles_fetes_v5.csv` a été ajouté en local le 19/10 (commit `16efe25`) — une étude « fin d'année » ciblée : 3 nouveaux clusters `noel-reveillon`, `cadeaux-colis`, `achat-en-ligne`. Les 5 autres CSV sont inchangés depuis le 30/09.
> Croisé avec : `ls blog/` (58 articles, +9 depuis le 12/10), `ls produits/` (55 fiches, +1), et les pages racine/catégories pertinentes (`epicerie-africaine.html`, `poissons-prix.html`, `atlas-poissons-wolof.html`, `categories/poissons-frais.html`).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**6e semaine consécutive sans trou strict** : la nouvelle étude « fin d'année » (v5) ne fait remonter qu'un seul mot-clé au-dessus du seuil — « pastels sénégalais » (390/mois, FAIBLE) — et il est déjà doublement couvert (article + fiche produit). Tout le reste du cluster Noël/réveillon/cadeaux est en volumes quasi nuls en géo France (0-20/mois), ce qui est normal pour une recherche pullée en octobre sur une saisonnalité de décembre — à repuller plus près des fêtes.

---

## 2. Déjà couvert (validation)

### Nouveau mot-clé testé (v5) au-dessus du seuil

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pastels sénégalais | 390 | FAIBLE | `blog/recette-pastels-senegalais.html` + `produits/pastels.html` |

*Reste du cluster v5 sous le seuil de 300/mois mais déjà thématiquement couvert ou sans action requise : « épicerie africaine en ligne » (140, ÉLEVÉE — déjà vu en v1, concurrence trop forte de toute façon), « repas de noël africain » (20, FAIBLE — doublon du cluster `fetes` de la v4, déjà noté en réserve), « recette réveillon poisson » (10) proche de `blog/poisson-braise.html` et `blog/recette-thieboudienne-authentique.html`, « acheter crevettes séchées » (10) et « livraison produits africains » (10) relèvent du cluster diaspora déjà analysé (§4). Le reste des lignes v5 est à 0/mois en géo France.*

### Mots-clés des CSV v1 à v4 (rappel, inchangés depuis le 30/09)

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| tilapia | 18 100 | FAIBLE | `produits/tilapia-rouge.html`, `categories/poissons-frais.html` |
| pain perdu | 90 500 | FAIBLE | `blog/pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `blog/riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `blog/bissap-hibiscus-guide.html`, `recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | FAIBLE | `blog/recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7+ articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| yassa poulet | 8 100 | FAIBLE | `blog/recette-yassa-poulet.html` |
| néré | 6 600 | FAIBLE | `blog/quest-ce-que-le-nere.html` |
| cymbium | 5 400-6 600 | FAIBLE | `blog/yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| poisson capitaine | 5 400 | FAIBLE | `produits/diane-capitaine.html`, `produits/beurre-capitaine.html` |
| épicerie africaine | 5 400 | FAIBLE | `epicerie-africaine.html` (page racine) |
| fonio | 5 400 | MOYENNE | `blog/fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `blog/beignet-banane-senegalais.html` |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| pain de singe / bouye / poudre de baobab | 1 300-3 600 | MOYENNE/FAIBLE/ÉLEVÉE | `blog/pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| bissap blanc | 1 600 | MOYENNE | `blog/bissap-blanc.html` + fiche produit |
| soumbala | 1 600 | FAIBLE | `blog/guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `blog/thiebou-yapp-riz-viande-senegalais.html` |
| niébé (des Îles du Saloum) | 1 300 | FAIBLE | `blog/niebe-haricot-saloum.html` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `blog/lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| yeet | 1 000 | FAIBLE | `blog/yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `blog/ditakh-fruit-vitamine-c-senegal.html` |
| poisson braisé | 1 000 | FAIBLE | `blog/poisson-braise.html` |
| domoda | 880 | FAIBLE | `blog/domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `blog/recette-jus-de-bouye.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `blog/thiere-couscous-mil-senegalais.html` |
| thiof | 590 | FAIBLE | `produits/thiof-decoupe.html` |
| dessert sénégalais | 480 | FAIBLE | `blog/thiakry-degue-dessert-senegalais.html`, `ngalakh-dessert-senegalais.html` |
| poisson africain | 480 | FAIBLE | `poissons-prix.html` (page racine) |
| netetou / nététou | 390 / 590 | FAIBLE | `blog/acheter-netetou-france.html`, `guide-netetou-soumbala.html`, fiche `netetu-mix` |
| soupou kandja | 590-720 | FAIBLE | `blog/recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `blog/ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `blog/recette-thieboudienne-authentique.html` |
| oseille de guinée (= bissap) | 390 | FAIBLE | `blog/bissap-hibiscus-guide.html` (synonyme, pas un trou) |
| beignets sénégalais | 390 | FAIBLE | `blog/beignet-banane-senegalais.html` |
| mbakhalou saloum | 320 | FAIBLE | `blog/recette-mbakhalou-saloum.html` |
| sardinelle / poisson kong / poisson fumé africain | 140-320 (sous le seuil) | FAIBLE | `blog/kethiakh-sardinelle-fumee-senegal.html`, `blog/poisson-kong.html` |
| caldou | 140 | FAIBLE | `blog/recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, référencement juste plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000), bissap rouge (390), pâte d'arachide (4 400).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article/fiche) dans les 6 CSV actuels, cluster fin d'année (v5) inclus. 6e semaine d'affilée.

Pistes secondaires hors critère strict, à garder en réserve :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique | Angle de niche « pâte d'arachide sénégalaise maison » lié à `tigadegue`/`guerte-noflay` — *graphie à confirmer avec Lamine* |
| buffet africain | 90 | FAIBLE | Sous le seuil de 300/mois | Angle « coffret buffet africain pour les fêtes » lié à `produits/pack-saloum.html` |
| repas de noël africain | 20 | FAIBLE | Sous le seuil, mais confirmé deux fois (v4 et v5) → cluster réel même si petit en France | Repuller en novembre/décembre pour voir si le volume monte en saison avant de décider d'un article |
| épicerie fine africaine | 40 | FAIBLE | Sous le seuil | Déjà proche d'`epicerie-africaine.html` — pas de nouvel article nécessaire |
| graine de néré | 170 | FAIBLE | Sous le seuil, déjà mentionné dans les articles néré/soumbala | Pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **L'étude « fin d'année » (v5) valide le catalogue plutôt que de révéler un trou.** Son seul mot-clé au-dessus du seuil — « pastels sénégalais » (390/mois, FAIBLE) — a déjà et un article (`recette-pastels-senegalais.html`) et une fiche produit (`produits/pastels.html`), ce qui est un bon signal de maillage interne (contenu éditorial + fiche e-commerce sur le même terme).
- **Les volumes Noël/réveillon/cadeaux sont quasi nuls parce que la donnée a été pullée le 19/10, trop tôt dans la saison.** « repas de noël africain » (20), « recette réveillon poisson » (10), « plat africain pour le nouvel an » (0) : ces requêtes montent typiquement en novembre-décembre. Ne pas conclure que ce cluster est sans intérêt sur la seule base de ce pull — à repuller en local mi-novembre pour une vraie lecture.
- **Le cluster `cadeaux-colis` reproduit le même schéma que le cluster diaspora `achat-en-ligne/acheter` déjà vu en v1-v4 : 0/mois en géo France.** « coffret épices africaines », « panier garni africain », « idée cadeau sénégal », « colis alimentaire sénégal » sont tous à 0. Ce n'est pas un échec de contenu, c'est une limite de géo (voir §5) — ces intentions existent probablement côté diaspora (USA/Canada/Europe), pas en France métropolitaine.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **yeet reste le seul mot-clé au CPC réellement commercial** dans les CSV disponibles. Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads.
- **Le catalogue a grossi depuis la dernière analyse chiffrée (12/10) : +9 articles blog, +1 fiche produit** (dont `niankatang-riz-casamance.html`, validé par Lamine le 23/10) — aucun des nouveaux mots-clés testés cette semaine ne nécessitait ce contenu, mais ça confirme que le rythme de publication suit bien la demande SEO identifiée précédemment.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console** — elle recoupe uniquement les 6 CSV déjà commités dans `scripts/ads/`.
- **Géo = France uniquement.** Le cluster diaspora/cadeaux (achat USA/Canada/Europe) ressort à 0 ici, c'est attendu — voir §4. Les articles diaspora (`acheter-guedj-amerique-nord.html`, `acheter-guedj-europe.html`) ne sont pas invalidés par ces 0.
- **Saisonnalité : la v5 a été pullée le 19/10, trop en amont de Noël.** Les volumes « fin d'année » affichés ici sous-estiment probablement la vraie demande de décembre — ne pas en tirer de conclusion négative, repuller plus près de la saison.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer cette semaine. Deux pistes non-contenu pour la prochaine étude locale : (1) repuller le cluster Noël/réveillon/cadeaux mi-novembre pour capter la vraie saisonnalité de fin d'année avant de décider d'un article dédié ; (2) tester une géo USA/Canada/Europe pour valider le cluster `cadeaux-colis`/diaspora qui est structurellement à 0 en France.

**Les 3 trous prioritaires de la semaine : aucun** — la nouvelle étude fin d'année (v5 : Noël/réveillon, cadeaux-colis, achat en ligne) ne fait remonter qu'un seul mot-clé au-dessus du seuil (« pastels sénégalais », 390/mois), déjà couvert par un article et une fiche produit ; le reste du cluster fin d'année est en volumes trop faibles en France à ce stade de l'année pour en tirer une décision de contenu.
