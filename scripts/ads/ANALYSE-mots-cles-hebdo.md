# Analyse mots-clés Google Ads — rapport hebdo du 24/08/2026

_Source : `mots_cles_resultats.csv` (v1), `mots_cles_resultats_v2.csv` (v2), `mots_cles_passerelle_v3.csv` (passerelle FR/cousins sénégalais)._
_Croisé avec : `blog/` (38 articles) et `produits/` (55 fiches) présents dans le repo à ce jour._
_Géo : France (2250) · Langue : français. Aucun appel API — analyse 100 % sur données déjà commitées._

---

## ⚠️ Note de gouvernance (lire avant le reste)

Une PR ouverte aujourd'hui sur ce même sujet (**#12**, branche `ads/analyse-hebdo-2026-08-24`) prétend avoir régénéré l'auth OAuth et relancé `etude_mots_cles_v2.py` en direct depuis le cloud, et **modifie `mots_cles_resultats_v2.csv` avec de nouveaux chiffres** (concurrence bissap blanc HIGH→MEDIUM, CPC bouye 0€→0,23-0,70€, poisson kong 320→260, etc.). C'est impossible depuis cette routine cloud (secrets `google-ads.yaml` / `refresh_token.txt` gitignorés, accessibles en local uniquement) et ça enfreint deux règles dures : ne jamais présenter de chiffres neufs comme des faits, et ne toucher qu'à `ANALYSE-mots-cles-hebdo.md`. Ce rapport-ci s'appuie uniquement sur les CSV réellement commités sur `main` à ce jour (aucune modification de CSV). Recommandation : Lamine tranche sur la PR #12 (probablement à fermer) avant de faire confiance à ses chiffres.

---

## 1. Verdict en une ligne

Les 4 trous identifiés la semaine dernière (thiébou yapp, ditakh, domoda, bouillie de mil) sont **tous comblés** — il ne reste plus qu'**1 seul trou net** (ngalakh, 590/mois) ; le catalogue de contenu couvre désormais la quasi-totalité des mots-clés à volume réel et concurrence faible.

---

## 2. Déjà couvert — validation

| Mot-clé | Vol./mois | Concurrence | Contenu existant |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais` |
| riz au lait | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide`, `recette-jus-de-bissap` + fiches `bissap-blanc/rouge` |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais` |
| guedj | 8 100 / 6 600 | FAIBLE | `quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`, `comment-cuisiner/conserver-le-guedj` |
| recette yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet` |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere` |
| cymbium | 6 600 / 5 400 | FAIBLE | `yeet-cymbium-maggi-africain` + fiche `yeet-maggi` |
| épicerie africaine | 5 400 | FAIBLE | `produits-senegalais-france` (hub boutique) |
| fonio | 5 400 | MOYENNE ⚠️ piège CPC | `fonio-cereale-sans-gluten` |
| jus de bissap | 4 400 | FAIBLE | `recette-jus-de-bissap` |
| thiakry | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais` |
| plat sénégalais | 4 400 | FAIBLE | `plats-senegalais` (hub) |
| beignet banane | 4 400 | FAIBLE | `beignet-banane-senegalais` |
| pain de singe / bouye | 3 600 / 1 300 | MOYENNE | `pain-de-singe-bouye-baobab` + fiche `bouye-baobab` (jus **et** poudre) |
| kinkeliba | 3 600 | ÉLEVÉE | `kinkeliba-tisane-bienfaits` |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala` |
| poisson séché | 1 600 | MOYENNE | articles guedj |
| thiéré / couscous de mil | 1 300 / 590 | FAIBLE | `thiere-couscous-mil-senegalais` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum` |
| **thiébou yapp** | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais` — comblé cette semaine ✅ |
| beignet africain (terme générique) | 1 900 | FAIBLE | mentionné et ciblé dans `beignet-banane-senegalais` |
| lakh | 1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain`, `guedj-ou-yeet-difference` |
| **ditakh / ditax** | ~1 090 | FAIBLE | `ditakh-fruit-vitamine-c-senegal` — comblé cette semaine ✅ |
| **bouillie de mil** | 1 000 | FAIBLE | `fonde-araw-bouillie-mil-senegalais` — comblé cette semaine ✅ |
| jus de bouye | 880 | FAIBLE | traité dans `pain-de-singe-bouye-baobab` |
| **domoda** | 880 | FAIBLE | `domoda-senegalais` — comblé cette semaine ✅ |
| netetou / nététou | 720 / 590 | FAIBLE | `acheter-netetou-france`, `guide-netetou-soumbala`, `dawadawa-netetou-*` |
| soupou kandja | 720 | FAIBLE | `recette-soupoukandja` |
| crevettes séchées | 590 | ÉLEVÉE | `crevettes-sechees-saloum` + fiche `crevettes-sechees` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique` |
| dessert sénégalais | 480 | FAIBLE | `thiakry-degue-dessert-senegalais` |
| poisson kong | 320 | FAIBLE | listé dans `les-7-guedj-du-senegal` + fiches `guej-kong`, `kongfume` |
| mbakhal / mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum`, `mbakhal-poisson-mbaxal-jen` |
| beignets sénégalais / sombi | 390 | FAIBLE | `beignet-banane-senegalais`, `riz-au-lait-senegalais-sombi` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais` |
| bassi salté | 50 | FAIBLE | `recette-basse-salte` |
| purée de piment africain | 20 | FAIBLE | fiche `puree-piment` |

---

## 3. Le trou à occuper (PRIORITÉ)

Volume réel + concurrence **FAIBLE** + **aucun article dédié** (mention en passant ≠ couverture).

| # | Mot-clé | Vol./mois | Concurrence | Angle proposé | Produit à lier |
|---|---|---:|---|---|---|
| 1 | **ngalakh** | 590 | FAIBLE | Nouvel article dédié : « le ngalakh, dessert de Tamkharit/Maouloud » (couscous + bouye + pâte d'arachide). Actuellement juste cité en passant dans `pain-de-singe-bouye-baobab` et `lakh-bouillie-mil-lait-caille`, sans page qui lui soit propre. | `bouye-baobab`, `ciakri`, `tigadegue-250`/`tiguadegue-500` |

### À surveiller (ne remplissent pas les critères stricts, mais notés pour info)

| Mot-clé | Vol./mois | Concurrence | Pourquoi c'est secondaire |
|---|---:|---|---|
| tamarin (jus) | 390 | MOYENNE | Concurrence non FAIBLE → hors critère prioritaire ; pas de produit tamarin au catalogue, ingrédient seulement cité dans `recette-thieboudienne-authentique`. |
| épicerie africaine paris | 140 | FAIBLE | Sous le seuil ~300/mois ; angle local (SEO Paris) pourrait convertir mieux que son volume ne le suggère, mais pas prioritaire tant que le trou #1 n'est pas traité. |

---

## 4. Insights stratégiques

- **Le trou se referme vite.** Sur les 5 trous identifiés lors des deux dernières études (thiébou yapp, ditakh, domoda, bouillie de mil, ngalakh), 4 ont déjà un article dédié. Le rythme de publication comble les priorités plus vite que l'étude n'en trouve de nouvelles — bon signe, mais ça veut dire que la prochaine étude devra creuser des seeds plus larges (variantes régionales, questions/FAQ) pour continuer à trouver des trous à volume réel.
- **« acheter X » ne se cherche pas en géo France.** Tout le cluster achat-diaspora reste proche de 0 (« où acheter guedj », « acheter netetou », « acheter poisson séché »). Les gens tapent le **nom du produit**, pas une tournure d'achat. Les articles diaspora USA/Canada (`acheter-guedj-amerique-nord`, `-europe`) ne sont **pas invalidés** par ce 0 : ils ciblent une autre géo, non couverte par cette étude France-only.
- **yeet reste le seul mot-clé au CPC réellement commercial** (1,12–4,33 €). Le reste du catalogue tourne à ~0 € de CPC : ce sont des requêtes informationnelles → le levier reste le **SEO organique**, pas l'achat Google Ads, sauf éventuellement sur yeet.
- **Piège fonio confirmé (v1) : ne jamais enchérir dessus en Ads.** CPC 20,70–172,75 € — c'est l'homonyme finance (ticker), pas la céréale. Le contenu organique (`fonio-cereale-sans-gluten`) reste la bonne approche, gratuite.
- **guedj (8 100) et néré (6 600) restent les deux piliers du trafic informationnel** — déjà bien couverts par plusieurs articles chacun, aucune action requise au-delà de la maintenance.

---

## 5. Limites de l'étude

- **Géo = France uniquement.** Les mots-clés diaspora (USA/Canada) ressortent à 0 ici mais ont du volume sur leur propre géo — non mesuré par cette étude.
- **Aucun chiffre de positionnement réel dans ce rapport** (pas de position Google, pas d'impressions, pas de CTR) : cette routine cloud n'a pas accès à Google Search Console. Les vrais chiffres de ranking viennent uniquement de `scripts/ads/gsc-data.md`, généré en local.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` ou `0` = données insuffisantes, pas forcément « aucune recherche ».
- **Rôle de cette routine = idées de contenu uniquement.** Aucune décision de publication n'est prise ici — Lamine tranche.
- Toute graphie de plat non déjà présente dans le repo est à confirmer avec Lamine avant publication (aucune inventée dans ce rapport : « ngalakh », « ditakh », « domoda », « thiébou yapp » reprennent l'orthographe déjà utilisée dans les CSV/contenu existant).
- **Backlog de PR non mergées** : à ce jour, 5 PR de routines hebdo (Ads/SEO) restent ouvertes sans avoir été mergées ni fermées (#1, #3, #9, #11, #12), plus #13 qui a créé un article de blog directement (hors mandat « proposer, ne pas créer »). Un nettoyage de ce backlog est recommandé avant de continuer les analyses hebdo.

---

**Résumé en 1 phrase :** un seul vrai trou net cette semaine — **ngalakh** (590/mois, concurrence faible, aucun article dédié) — à surveiller en secondaire : **tamarin (jus)** et **épicerie africaine paris**, tous deux sous le seuil de priorité stricte.
