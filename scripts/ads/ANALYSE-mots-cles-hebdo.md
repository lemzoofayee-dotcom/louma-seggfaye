# Analyse mots-clés Google Ads — Lundi 14/09/2026

> **Analyse cloud, aucune donnée neuve.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 4 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`) — **inchangés depuis le 24/08** (3e semaine consécutive sans nouveau pull Keyword Planner).
> Croisé avec : `ls blog/` (48 articles) et `ls produits/` (54 fiches).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**Troisième semaine sans donnée fraîche, toujours zéro trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) — mais bonne nouvelle côté exécution : les 4 pistes de contenu identifiées le 24/08 (jus de bouye, bissap blanc, jus de tamarin, poisson kong) ont **toutes été publiées le jour même**, et « beignet africain » a été retitré le 07/09. Le stock d'opportunités des CSV actuels est désormais **entièrement absorbé** ; la vraie priorité n'est plus l'écriture d'articles mais de **relancer un pull Keyword Planner en local** avant que cette routine ne tourne à vide une 4e semaine.

---

## 2. Déjà couvert (validation)

Tous les mots-clés à volume ≥ 300/mois des 4 CSV ont un article ou une fiche dédiée.

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide.html`, `recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7+ articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet.html` |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere.html` |
| cymbium | 5 400-6 600 | FAIBLE | `yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| épicerie africaine | 5 400 | FAIBLE | `produits-senegalais-france.html` (dans le `<title>` : « Épicerie africaine en ligne ») |
| fonio | 5 400 | MOYENNE | `fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `beignet-banane-senegalais.html` — **retitré le 07/09** (`<title>`/H1 ciblent désormais « beignet africain »), plus une simple mention en metadata |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` (publié 24/08) + fiche produit |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| pain de singe / bouye | 1 300-3 600 | MOYENNE/FAIBLE | `pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum.html` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` (publié 24/08) |
| netetou / nététou | 590-720 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html`, `netetu-mix.html` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| oseille de guinée (= bissap) | 390 | MOYENNE | `bissap-hibiscus-guide.html`, `bissap-blanc.html` (synonyme, pas un trou) |
| tamarin jus | 320-390 | MOYENNE | `jus-de-tamarin-dakhar.html` (publié 24/08) |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| poisson kong | 260-320 | FAIBLE | `poisson-kong.html` (publié 24/08) |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, juste un référencement plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) dans les 4 CSV actuels — inchangé depuis le 24/08, et les 4 pistes qui existaient à cette date ont depuis été publiées (voir §2).

Pistes secondaires hors critère strict, à garder en réserve :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique ; CPC réel (0,38-0,69 €) confirme l'intérêt commercial | Angle de niche « pâte d'arachide sénégalaise maison » (moins concurrentiel) — à lier à `tigadegue`/`guerte-noflay` — *graphie à confirmer avec Lamine* |
| graine de néré | 210 | FAIBLE | Sous le seuil de 300/mois | Déjà mentionné dans plusieurs articles néré/soumbala — pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **3 semaines sans donnée fraîche = le pull Keyword Planner doit être relancé.** Le CSV le plus récent date du 24/08 (`etude_mots_cles_v2.py` / `etude_passerelle_v3.py`). Le refresh token OAuth expire à 7 jours en mode « test » — tant que l'écran de consentement Google Cloud Console n'est pas passé de *Testing* à *In production*, cette routine cloud recycle les mêmes 60 mots-clés chaque semaine. Ce n'est plus un simple rappel : après 3 semaines, l'analyse cloud a fait le tour de ce qu'elle peut apporter sans nouvelles données.
- **Bonne nouvelle côté exécution : le backlog du 24/08 est vide.** Les 4 pistes de contenu de l'analyse du 24/08 (jus de bouye, bissap blanc, jus de tamarin/dakhar, poisson kong) ont toutes été publiées **le jour même**, et « beignet africain » a été retitré/H1 le 07/09. Le catalogue (48 articles blog + 54 fiches produits) absorbe désormais l'intégralité des mots-clés ≥300/mois en concurrence faible des CSV disponibles.
- **File d'attente PR nettoyée.** Aucun PR ouvert actuellement sur le repo — le problème d'empilement signalé les semaines précédentes (#3, #9, #11, #24) est résolu. Bon réflexe à garder : fermer/merger le PR hebdo avant d'en ouvrir un nouveau.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter » ne se cherche pas en géo France.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois. Normal, cette géo ne capture pas la diaspora — les articles `acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html` ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** (1,06-4,33 €). Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads, sauf éventuellement yeet.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Zéro donnée neuve depuis 3 semaines.** Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les CSV déjà commités (le plus récent date du 24/08). Un vrai rafraîchissement Keyword Planner nécessite une session locale (`etude_mots_cles.py` / `etude_mots_cles_v2.py` / `etude_passerelle_v3.py`).
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer cette semaine — le stock de trous est vide et le backlog précédent a déjà été livré. Action non-contenu prioritaire : **relancer un pull Keyword Planner en local** (et régler l'expiration du refresh token en passant l'app en mode « In production ») avant la prochaine analyse cloud, sinon celle-ci continuera de tourner en boucle sur les mêmes 60 mots-clés.

**Les 3 trous prioritaires de la semaine : aucun** — le catalogue couvre déjà l'intégralité des mots-clés ≥300 recherches/mois en concurrence faible des 4 CSV existants ; la seule piste de réserve reste « pâte d'arachide sénégalaise maison » (concurrence élevée, angle de niche, graphie à confirmer avec Lamine).
