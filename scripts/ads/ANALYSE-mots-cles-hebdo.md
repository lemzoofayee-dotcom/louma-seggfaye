# Analyse mots-clés Google Ads — Lundi 31/08/2026

> **Analyse cloud, aucune donnée neuve.** Pas d'accès à l'API Google Ads ni à Search Console depuis le cloud.
> Source : les 4 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`).
> Croisé avec : `ls blog/` (39 articles) et `ls produits/` (55 fiches).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**Tous les trous identifiés la semaine du 24/08 ont été comblés** (thiébou yapp, domoda, ngalakh, jus de bouye, jus de tamarin/dakhar, poisson kong, bissap blanc, beignet africain) — aucun nouveau trou « volume ≥ 300 + concurrence FAIBLE + zéro article » ne ressort des CSV actuels.

---

## 2. Déjà couvert (validation)

### Comblé depuis la dernière analyse (bravo)

| Mot-clé | Vol./mois | Concurrence | Article publié |
|---|---:|---|---|
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` (+ fiche produit) |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| tamarin jus | 320-390 | MOYENNE | `jus-de-tamarin-dakhar.html` |
| poisson kong | 260-320 | FAIBLE | `poisson-kong.html` |
| beignet africain | 1 900 | FAIBLE | mot-clé ajouté dans les métadonnées de `beignet-banane-senegalais.html` |

### Socle historique toujours bien couvert

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide.html`, `recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7 articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere.html` |
| yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet.html` |
| cymbium | 5 400-6 600 | FAIBLE | `yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| épicerie africaine | 5 400 | FAIBLE | `produits-senegalais-france.html` |
| fonio | 5 400 | MOYENNE | `fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet banane | 4 400 | FAIBLE | `beignet-banane-senegalais.html` |
| thiakry | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html` |
| plat sénégalais | 4 400 | FAIBLE | `plats-senegalais.html` |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| pain de singe / bouye | 1 300-3 600 | MOYENNE/FAIBLE | `pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| lakh | 1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum.html` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| netetou / nététou | 590-720 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, la barrière SEO est haute mais le contenu existe) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun.** En croisant les 4 études avec `blog/` et `produits/`, plus aucun mot-clé à volume ≥ 300/mois et concurrence FAIBLE n'est sans article dédié. Le sprint de contenu de la semaine du 24/08 a vidé le stock de trous identifiés.

Deux pistes secondaires, hors critère strict (volume < 300 ou concurrence pas FAIBLE), à garder en réserve plutôt qu'à traiter en urgence :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour un article générique — CPC réel (0,38-0,69 €) confirme l'intérêt commercial | Angle de niche moins concurrentiel : « pâte d'arachide sénégalaise maison » plutôt que le terme générique — à lier à `tigadegue`/`guerte-noflay` |
| graine de néré | 210 | FAIBLE | Volume sous le seuil de 300 | Déjà mentionné dans 5 articles (`quest-ce-que-le-nere`, `dawadawa-netetou-african-locust-bean`…) — pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **La stratégie de comblement fonctionne.** Les 8 trous détectés la semaine dernière sont tous publiés — bon rythme, à maintenir plutôt qu'à accélérer artificiellement (créer un article sans mot-clé qui le justifie serait du remplissage).
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : c'est l'homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — le trafic sur `fonio-cereale-sans-gluten.html` doit rester 100 % organique.
- **Le préfixe « acheter » ne se cherche pas en géo France.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois. Normal : cette géo ne capture pas la diaspora. Les articles `acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html` ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** (1,06-4,33 €). Le reste du catalogue est quasi à 0 € de CPC = levier SEO organique, pas budget Ads, sauf éventuellement yeet.
- **Nettoyage process** : les études v2 (24/07) et 24/08 ont bien été mergées sur `main` (commits `955956b`, `b67d465`) — pas de PR ads en attente à traiter avant celle-ci.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Zéro donnée neuve cette semaine.** Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les CSV déjà commités (le plus récent date du 24/08). Un vrai rafraîchissement Keyword Planner nécessite une session locale avec `gsc_pull.py` / `etude_mots_cles.py`.
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer d'urgent cette semaine. Si Lamine veut occuper du terrain supplémentaire malgré l'absence de trou strict, la seule piste avec un vrai volume est **pâte d'arachide** — mais via un angle de niche (recette maison) plutôt que le terme générique bloqué par la concurrence ÉLEVÉE. Sinon : attendre la prochaine étude Keyword Planner fraîche (locale) avant de relancer un sprint de contenu.
