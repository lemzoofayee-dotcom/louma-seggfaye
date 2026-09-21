# Analyse mots-clés Google Ads — Lundi 21/09/2026

> **Analyse cloud, aucune donnée neuve.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 4 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`) — **strictement identiques (diff vide) à la semaine dernière** (4e semaine consécutive sans nouveau pull Keyword Planner, dernier pull réel le 24/08).
> Croisé avec : `ls blog/` (48 articles) et `ls produits/` (54 fiches) — aucun fichier ajouté depuis l'analyse du 14/09, seulement des modifications (photos poissons, corrections d'accents, retitrage yeet/néré, maillage interne guedj).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**Toujours zéro trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) — situation identique à la semaine dernière : ni nouveau mot-clé (CSV inchangés), ni nouvel article (seules des retouches sur l'existant : photos néré/atlas poissons, correction d'accents, retitrage yeet/beignet). L'analyse cloud a désormais fait 4 fois le tour des mêmes 60 mots-clés sans rien de neuf à proposer côté contenu ; la priorité reste le rafraîchissement Keyword Planner en local, pas l'écriture.

---

## 2. Déjà couvert (validation)

Tous les mots-clés à volume ≥ 300/mois des 4 CSV ont un article ou une fiche dédiée (inchangé vs. semaine dernière).

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais.html` |
| riz au lait / sombi | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi.html` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide.html`, `recette-jus-de-bissap.html` + fiches bissap-blanc/rouge |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais.html` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais.html` |
| guedj | 6 600-8 100 | FAIBLE | 7+ articles (`quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`…) |
| yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet.html` |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere.html` (+ 3 photos ajoutées le 20/09) |
| cymbium | 5 400-6 600 | FAIBLE | `yeet-cymbium-maggi-africain.html` + fiche `yeet-maggi` |
| épicerie africaine | 5 400 | FAIBLE | `produits-senegalais-france.html` (dans le `<title>` : « Épicerie africaine en ligne ») |
| fonio | 5 400 | MOYENNE | `fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `beignet-banane-senegalais.html` (retitré le 07/09) |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` + fiche produit |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| pain de singe / bouye | 1 300-3 600 | MOYENNE/FAIBLE | `pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé | 1 300 | FAIBLE | `niebe-haricot-saloum.html` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` (4 graphies détaillées le 16/09) |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` |
| netetou / nététou | 590-720 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html`, `netetu-mix.html` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| oseille de guinée (= bissap) | 390 | MOYENNE | `bissap-hibiscus-guide.html`, `bissap-blanc.html` (synonyme, pas un trou) |
| tamarin jus | 320-390 | MOYENNE | `jus-de-tamarin-dakhar.html` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| poisson kong | 260-320 | FAIBLE | `poisson-kong.html` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, juste un référencement plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590, `crevettes-sechees-saloum.html`), fleur d'hibiscus séchée (1 000).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article) dans les 4 CSV actuels — 4e semaine d'affilée avec le même constat, aucun nouveau mot-clé à évaluer.

Pistes secondaires hors critère strict, à garder en réserve (inchangées) :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique ; CPC réel (0,38-0,69 €) confirme l'intérêt commercial | Angle de niche « pâte d'arachide sénégalaise maison » (moins concurrentiel) — à lier à `tigadegue`/`guerte-noflay` — *graphie à confirmer avec Lamine* |
| graine de néré | 210 | FAIBLE | Sous le seuil de 300/mois | Déjà mentionné dans plusieurs articles néré/soumbala — pas besoin d'article dédié |

---

## 4. Insights stratégiques

- **4 semaines sans donnée fraîche — le pull Keyword Planner doit être relancé en priorité.** Le CSV le plus récent date toujours du 24/08. Tant que le refresh token OAuth (mode « Testing », expiration 7 jours) n'est pas stabilisé en passant l'app Google Cloud Console en « In production », cette routine cloud continuera de recycler les mêmes 60 mots-clés chaque semaine sans plus rien apporter de neuf.
- **Le travail éditorial de la semaine a porté sur la qualité, pas le volume.** Aucun nouvel article/fiche créé depuis le 14/09 ; le rythme a été mis sur : 3 photos néré (arbre/fleur/gousses), le détail des 4 graphies du yeet + repos biologique/UNESCO, le repositionnement touffa comme « cousin » du yeet (validé Lamine), 18 liens internes sur le rayon poissons (contre 2 avant), et une passe de correction d'accents sur ~15 pages. Bon pour la qualité SEO on-page, mais ça ne change rien au diagnostic « trous = 0 » ci-dessus.
- **File d'attente PR toujours propre.** Aucun PR ouvert sur le repo actuellement — le réflexe fermer/merger avant d'ouvrir reste respecté.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter » ne se cherche pas en géo France.** « où acheter guedj », « acheter netetou », « acheter poisson séché » = 0/mois. Normal, cette géo ne capture pas la diaspora — les articles `acheter-guedj-amerique-nord.html` / `acheter-guedj-europe.html` ciblent une autre géo et ne sont pas invalidés par ce 0.
- **yeet reste le seul mot-clé au CPC réellement commercial** (1,06-4,33 €). Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads, sauf éventuellement yeet.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Zéro donnée neuve depuis 4 semaines.** Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les CSV déjà commités (le plus récent date du 24/08, diff vérifié vide vs. la semaine dernière). Un vrai rafraîchissement Keyword Planner nécessite une session locale (`etude_mots_cles.py` / `etude_mots_cles_v2.py` / `etude_passerelle_v3.py`).
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Rien à créer cette semaine — le stock de trous est toujours vide et aucun nouveau mot-clé n'est apparu. Action non-contenu prioritaire, désormais urgente après 4 semaines : **relancer un pull Keyword Planner en local** (et stabiliser le refresh token OAuth en passant l'app en mode « In production ») avant la prochaine analyse cloud, sinon celle-ci continuera de tourner à vide.

**Les 3 trous prioritaires de la semaine : aucun** — 4e semaine consécutive avec les mêmes CSV et un catalogue qui couvre déjà l'intégralité des mots-clés ≥300 recherches/mois en concurrence faible ; la seule piste de réserve reste « pâte d'arachide sénégalaise maison » (concurrence élevée, angle de niche, graphie à confirmer avec Lamine).
