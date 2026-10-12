# Analyse mots-clés Google Ads — Lundi 12/10/2026

> **Analyse cloud, aucune donnée neuve générée.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 5 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`, et **nouveau** : `mots_cles_elargie_v4.csv`).
> **Nouveauté cette semaine** : `mots_cles_elargie_v4.csv` a été ajouté en local le 30/09 (commit `398a1e1`) — exactement la suite demandée dans le rapport du 28/09 (« relancer un pull avec des seeds élargies »). 4 nouveaux clusters testés : `poisson-frais`, `conservation`, `fetes`, `cadeaux-diaspora`. Les 4 autres CSV sont inchangés depuis le 23/09.
> Croisé avec : `ls blog/` (49 articles), `ls produits/` (54 fiches), et les pages racine pertinentes (`epicerie-africaine.html`, `poissons-prix.html`, `atlas-poissons-wolof.html`).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**5e semaine consécutive sans trou strict**, mais celle-ci compte : la nouvelle étude élargie (v4) teste 4 clusters inédits (poisson frais, fêtes, cadeaux diaspora, conservation) et le catalogue absorbe encore tout — y compris « tilapia » (18 100/mois, FAIBLE) et « poisson capitaine » (5 400/mois, FAIBLE), déjà couverts par des fiches produit existantes. C'est un signal positif (le catalogue est robuste même face à de nouvelles seeds), pas un signal d'arrêt : il reste des pistes sous le seuil de volume à garder en réserve, détaillées en §3-4.

---

## 2. Déjà couvert (validation)

### Nouveaux mots-clés testés (v4) — tous déjà couverts

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| tilapia | 18 100 | FAIBLE | `produits/tilapia-rouge.html` |
| poisson capitaine | 5 400 | FAIBLE | `produits/diane-capitaine.html`, `produits/beurre-capitaine.html` |
| poisson braisé | 1 000 | FAIBLE | `blog/poisson-braise.html` |
| thiof | 590 | FAIBLE | `produits/thiof-decoupe.html` |
| poisson africain | 480 | FAIBLE | `poissons-prix.html` (title : « Prix des poissons africains du Sénégal ») — page racine, hors blog/produits mais dédiée |

*Sardinelle (260/mois) et poisson fumé africain (140/mois) sont sous le seuil de 300 mais déjà couverts quand même (`blog/kethiakh-sardinelle-fumee-senegal.html`, articles guedj fumé).*

### Mots-clés des CSV v1/v2/passerelle (rappel, inchangés depuis le 23/09)

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
| épicerie africaine | 5 400 | FAIBLE | `epicerie-africaine.html` (page racine ; **l'ancienne `blog/produits-senegalais-france.html` a été supprimée le 11/10**, redirection 308 déjà en place) |
| fonio | 5 400 | MOYENNE | `fonio-cereale-sans-gluten.html` — ⚠️ piège CPC, voir §4 |
| beignet africain / banane | 4 400 / 1 900 | FAIBLE | `beignet-banane-senegalais.html` |
| thiakry / plat sénégalais | 4 400 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `plats-senegalais.html` |
| bissap blanc | 1 600 | MOYENNE | `bissap-blanc.html` + fiche produit |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala.html` |
| thiébou yapp | 1 300 | FAIBLE | `thiebou-yapp-riz-viande-senegalais.html` |
| pain de singe / bouye / poudre de baobab | 1 300-3 600 | MOYENNE/FAIBLE/ÉLEVÉE | `pain-de-singe-bouye-baobab.html` + fiche `bouye-baobab` |
| lakh / bouillie de mil | 1 000-1 300 | FAIBLE | `lakh-bouillie-mil-lait-caille.html`, `fonde-araw-bouillie-mil-senegalais.html` |
| thiéré / couscous de mil | 590-1 300 | FAIBLE | `thiere-couscous-mil-senegalais.html` |
| niébé (des Îles du Saloum) | 1 300 | FAIBLE | `niebe-haricot-saloum.html` — produit renommé le 02/10 |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain.html`, `guedj-ou-yeet-difference.html` |
| ditakh | 1 000 | FAIBLE | `ditakh-fruit-vitamine-c-senegal.html` |
| domoda | 880 | FAIBLE | `domoda-senegalais.html` |
| jus de bouye | 880 | FAIBLE | `recette-jus-de-bouye.html` |
| dessert sénégalais | 480 | FAIBLE | `thiakry-degue-dessert-senegalais.html`, `ngalakh-dessert-senegalais.html` |
| netetou / nététou | 390 / 590 | FAIBLE | `acheter-netetou-france.html`, `guide-netetou-soumbala.html`, fiche `netetu-mix` |
| soupou kandja | 590-720 | FAIBLE | `recette-soupoukandja.html` |
| ngalakh | 590 | FAIBLE | `ngalakh-dessert-senegalais.html` |
| recette thieboudienne | 590 | FAIBLE | `recette-thieboudienne-authentique.html` |
| bissap rouge | 390 | ÉLEVÉE | fiche `bissap-rouge`, `bissap-hibiscus-guide.html` |
| oseille de guinée (= bissap) | 390 | FAIBLE | `bissap-hibiscus-guide.html` (synonyme, pas un trou) |
| beignets sénégalais | 390 | FAIBLE | `beignet-banane-senegalais.html` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum.html` |
| poisson kong | 260-320 (sous le seuil) | FAIBLE | `poisson-kong.html` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais.html` |

*Concurrence ÉLEVÉE, déjà couvertes malgré tout (pas des trous, référencement juste plus dur) : kinkeliba (3 600), poudre de baobab (2 400), crevettes séchées (590), fleur d'hibiscus séchée (1 000), bissap rouge (390).*

---

## 3. Les trous à occuper (PRIORITÉ)

**Aucun trou strict** (volume ≥ 300/mois + concurrence FAIBLE + zéro article/fiche) dans les 5 CSV actuels, nouveaux clusters v4 inclus. 5e semaine d'affilée, mais la première fois que ce verdict est testé contre des seeds vraiment nouvelles.

Pistes secondaires hors critère strict, à garder en réserve :

| Mot-clé | Vol./mois | Concurrence | Pourquoi ce n'est pas un trou prioritaire | Piste si jamais |
|---|---:|---|---|---|
| pâte d'arachide | 4 400 | **ÉLEVÉE** | Concurrence trop forte pour viser le terme générique | Angle de niche « pâte d'arachide sénégalaise maison » — à lier à `tigadegue`/`guerte-noflay` — *graphie à confirmer avec Lamine* |
| buffet africain | 90 | FAIBLE | Sous le seuil de 300/mois, mais cluster « fêtes » nouveau et thématiquement inexploité | Article/angle « coffret buffet africain pour les fêtes » lié à `produits/pack-saloum.html` — *à valider avec Lamine avant tout nom de plat précis* |
| graine de néré | 170 | FAIBLE | Sous le seuil, déjà mentionné dans les articles néré/soumbala | Pas besoin d'article dédié |
| épicerie fine africaine | 40 | FAIBLE | Sous le seuil | Déjà proche d'`epicerie-africaine.html` — pas de nouvel article nécessaire |

---

## 4. Insights stratégiques

- **L'élargissement des seeds demandé la semaine dernière a été fait, et le catalogue a tenu.** La v4 teste 4 clusters inédits (poisson frais, fêtes, cadeaux diaspora, conservation) — y compris le très gros volume « tilapia » (18 100/mois) — et tout est déjà couvert par des fiches produit ou pages racine existantes. C'est une validation utile du travail de maillage déjà fait, pas une impasse : les prochaines seeds à tester en local pourraient cibler des angles encore absents du Keyword Planner France, comme des variantes longues « recette tabaski »/« recette korité » (actuellement à 10/mois, trop tôt pour en tirer une conclusion) à repuller après le Ramadan/Tabaski prochain pour voir si le volume monte en saison.
- **Bruit de données à surveiller dans `mots_cles_elargie_v4.csv` : requêtes « tilapia » non francophones.** Le cluster `poisson-frais` fait remonter des variantes espagnoles/néerlandaises (« tilapia a la mexicana », « tilapia prijs », « tilapia in de oven », « vis tilapia »…) — normal pour un terme générique international capté par Keyword Planner même en géo France, mais ça ne reflète pas une intention FR réelle. Ne pas les compter comme signal de demande francophone.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter »/diaspora reste à 0 en géo France, c'est normal.** « où acheter guedj », « acheter netetou », « acheter poisson séché », « coffret produits africains », « colis alimentaire afrique » = 0/mois dans cette géo. Les articles diaspora (`acheter-guedj-amerique-nord.html`, `acheter-guedj-europe.html`) ciblent une autre géo et ne sont pas invalidés par ce 0 — une vraie validation de ce cluster nécessiterait un pull Keyword Planner en géo USA/Canada, à faire en local.
- **yeet reste le seul mot-clé au CPC réellement commercial** dans les CSV disponibles. Le reste du catalogue est quasi à 0 € de CPC → levier SEO organique, pas budget Ads.
- **Page supprimée à surveiller** : `blog/produits-senegalais-france.html` a été supprimée le 11/10 (redirection 308 vers `/epicerie-africaine.html` depuis le 23/09) — le mot-clé « épicerie africaine » reste couvert par la page racine, mais si une future étude Ads cherche encore l'ancienne URL, c'est normal, elle est intentionnellement retirée.

---

## 5. Limites de l'étude (à lire avant d'agir)

- **Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console** — elle recoupe uniquement les 5 CSV déjà commités dans `scripts/ads/`.
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu — voir §4. Les clusters « fêtes »/« cadeaux diaspora » de la v4 sont aussi en géo France, donc leurs très petits volumes (10-90/mois) ne disent rien de la demande réelle côté diaspora.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.
- **Bruit linguistique dans la v4** (requêtes tilapia en espagnol/néerlandais) — voir §4, à ignorer pour la stratégie FR.

---

## 6. Recommandation

Rien à créer cette semaine — même les nouvelles seeds (v4) ne révèlent aucun trou strict. Deux pistes non-contenu pour la prochaine étude locale : (1) tester une géo USA/Canada pour valider réellement le cluster diaspora « acheter » qui est structurellement à 0 en France ; (2) repuller les requêtes saisonnières (tabaski, korité, ramadan africain) après la prochaine fête religieuse pour voir si leur volume (10/mois actuellement) grimpe en saison.

**Les 3 trous prioritaires de la semaine : aucun** — la nouvelle étude élargie (v4 : poisson frais, fêtes, cadeaux diaspora, conservation) confirme que le catalogue (49 articles + 54 fiches + pages racine) couvre déjà tous les mots-clés ≥300/mois en concurrence faible, y compris « tilapia » (18 100/mois) et « poisson capitaine » (5 400/mois) ; seules pistes de réserve sous le seuil : « pâte d'arachide sénégalaise maison » (concurrence élevée) et « coffret buffet africain pour les fêtes » (faible volume, cluster neuf).
