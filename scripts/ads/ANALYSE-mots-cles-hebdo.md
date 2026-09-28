# Analyse mots-clés Google Ads — Lundi 28/09/2026

> **Analyse cloud, aucune donnée neuve générée.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 4 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`).
> **Nouveauté cette semaine** : `mots_cles_resultats_v2.csv` a été rafraîchi en local le 23/09 (commit `723eb13`) — 6 volumes ont bougé, dont **netetou 720 → 390**. Les 3 autres CSV sont inchangés depuis le 24/08.
> Croisé avec : `ls blog/` (48 articles) et `ls produits/` (54 fiches).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**4e semaine consécutive sans trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) : le pull du 23/09 n'a fait bouger que des chiffres sur des mots-clés déjà couverts (aucun mot-clé ajouté ou retiré) — le catalogue (48 articles + 54 fiches) absorbe toujours l'intégralité du stock. Le vrai sujet de la semaine reste le même qu'il y a 15 jours : **relancer un pull Keyword Planner avec des seeds élargies** (nouveaux clusters, pas juste un refresh des 60 mots-clés existants), sinon cette routine cloud continuera de confirmer un statu quo sans rien apporter de neuf.

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
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `beignet-banane-senegalais.html` (title/H1 ciblent « beignet africain ») |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` + fiche produit |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| pain de singe / bouye / poudre de baobab | 1 300-3 600 | MOYENNE/FAIBLE/ÉLEVÉE | `pain-de-singe-bouye-baobab.html` (couvre aussi « poudre de baobab ») + fiche `bouye-baobab` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum.html` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` |
| dessert sénégalais | 480 | FAIBLE | `thiakry-degue-dessert-senegalais.html` (title explicite), `ngalakh-dessert-senegalais.html` |
| netetou / nététou | **390** (↓ de 720) / 590 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html`, fiche `netetu-mix` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| bissap rouge | 390 | ÉLEVÉE | fiche `bissap-rouge`, `bissap-hibiscus-guide.html` |
| oseille de guinée (= bissap) | 390 | FAIBLE | `bissap-hibiscus-guide.html`, `bissap-blanc.html` (synonyme, pas un trou) |
| beignets sénégalais | 390 | FAIBLE | `beignet-banane-senegalais.html` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| poisson kong | 260 (sous le seuil, déjà couvert) | FAIBLE | `poisson-kong.html` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, juste un référencement plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000), bissap rouge (390).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) dans les 4 CSV actuels — 4e semaine d'affilée. Le pull du 23/09 n'a introduit aucun nouveau mot-clé (seulement des valeurs actualisées sur les 60 termes déjà connus), donc rien n'est passé sous le radar cette semaine.

Pistes secondaires hors critère strict, à garder en réserve (inchangées) :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique ; CPC réel (0,38-0,69 €) confirme l'intérêt commercial | Angle de niche « pâte d'arachide sénégalaise maison » — à lier à `tigadegue`/`guerte-noflay` — *graphie à confirmer avec Lamine* |
| graine de néré | 170 (↓ de 210) | FAIBLE | Sous le seuil de 300/mois, et en baisse | Déjà mentionné dans les articles néré/soumbala — pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **4 semaines sans nouveau mot-clé = il est temps d'élargir les seeds, pas juste de repulled les mêmes 60 termes.** Le pull du 23/09 (`723eb13`) a mis à jour des volumes (netetou 720→390, tamarin jus 320→210, acheter bissap 140→110, graine de néré 210→170, cymbium glans 30→40) mais **aucun mot-clé nouveau**. Le refresh token OAuth en mode « test » Google Cloud Console expire à 7 jours — si l'app n'est toujours pas passée en « In production », chaque pull local doit être relancé manuellement, ce qui explique le rythme irrégulier. Prochaine étape utile : lancer une étude avec de nouvelles seeds (ex. sous-clusters « recettes fêtes », « cadeaux gourmands diaspora », « conservation/DLC produits séchés ») plutôt que de repulled les mêmes clusters.
- **netetou reste au-dessus du seuil malgré la baisse (720 → 390/mois).** Pas d'impact sur la couverture — déjà bien traité par `acheter-netetou-france.html` et `guide-netetou-soumbala.html`. À surveiller si la tendance baissière se poursuit.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter » ne se cherche pas en géo France.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois. Normal, cette géo ne capture pas la diaspora — les articles `acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html` ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** dans les CSV disponibles (le v2 courant l'affiche à 0 € mais le v1 et les pulls précédents le situent entre 1,06-4,33 €, volatilité probable liée au faible volume de données Keyword Planner). Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Un seul CSV rafraîchi depuis 4 semaines**, et seulement sur des valeurs, pas de nouveaux mots-clés. Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les CSV déjà commités. Un vrai élargissement (nouvelles seeds) nécessite une session locale (`etude_mots_cles.py` / `etude_mots_cles_v2.py` / `etude_passerelle_v3.py`).
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer cette semaine — le stock de trous reste vide et aucun mot-clé nouveau n'est apparu dans le pull du 23/09. Action non-contenu prioritaire, inchangée depuis 2 semaines : **lancer un pull Keyword Planner avec des seeds élargies** (nouveaux sous-thèmes, pas un simple refresh) et régler l'expiration du refresh token (mode « In production » sur Google Cloud Console) avant la prochaine analyse cloud.

**Les 3 trous prioritaires de la semaine : aucun** — le catalogue couvre déjà l'intégralité des mots-clés ≥300 recherches/mois en concurrence faible des 4 CSV existants (dont netetou, désormais à 390/mois) ; la seule piste de réserve reste « pâte d'arachide sénégalaise maison » (concurrence élevée, angle de niche, graphie à confirmer avec Lamine).
