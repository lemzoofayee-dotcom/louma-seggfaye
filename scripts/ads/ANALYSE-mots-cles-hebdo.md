# Analyse mots-clés Google Ads — rapport hebdo

_Rapport du 17/08/2026 (routine cloud)._
_Source : CSV déjà commités — `mots_cles_resultats.csv` (v1), `mots_cles_resultats_v2.csv` (v2), `mots_cles_passerelle_v3.csv`. Aucun appel API Ads (cloud = pas d'accès aux secrets)._
_Croisé avec : 38 articles `blog/` et 53 fiches `produits/` (état au 17/08/2026)._
_Géo : France (2250) · Langue : français._

---

## 1. Verdict en une ligne

Bonne nouvelle : **4 des 6 trous identifiés la semaine dernière sont déjà comblés** (thiébou yapp, domoda, ditakh, bouillie de mil) — reste **lakh, couscous de mil/thiéré et niébé** comme plus gros volumes encore sans article dédié, plus 3 trous secondaires.

---

## 2. Déjà couvert — validation rapide

| Mot-clé | Vol./mois | Concurrence | Contenu existant |
|---|---:|---|---|
| pain perdu | 90 500 | FAIBLE | `pain-perdu-mbourou-fass-senegalais` |
| riz au lait | 74 000 | FAIBLE | `riz-au-lait-senegalais-sombi` |
| bissap | 60 500 | FAIBLE | `bissap-hibiscus-guide`, `recette-jus-de-bissap` + fiches bissap blanc/rouge |
| dégué | 12 100 | FAIBLE | `thiakry-degue-dessert-senegalais` |
| recette mafé | 9 900 | FAIBLE | `recette-mafe-senegalais` |
| guedj / néré | 8 100 / 6 600 | FAIBLE | `quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`, `quest-ce-que-le-nere` |
| recette yassa poulet | 8 100 | FAIBLE | `recette-yassa-poulet` |
| cymbium | 6 600 | FAIBLE | `yeet-cymbium-maggi-africain` + fiche `yeet-maggi` |
| fonio | 5 400 | MOYENNE* | `fonio-cereale-sans-gluten` — *voir piège CPC en §4* |
| **thiébou yapp** | 1 300 | FAIBLE | ✅ NOUVEAU — `thiebou-yapp-riz-viande-senegalais` |
| **domoda** | 880 | FAIBLE | ✅ NOUVEAU — `domoda-senegalais` |
| **ditakh** | 1 000 | FAIBLE | ✅ NOUVEAU — `ditakh-fruit-vitamine-c-senegal` |
| **bouillie de mil** | 1 000 | FAIBLE | ✅ NOUVEAU — `fonde-araw-bouillie-mil-senegalais` |
| pain de singe / bouye | 3 600 / 1 300 | MOYENNE/FAIBLE | `pain-de-singe-bouye-baobab` + fiche `bouye-baobab` |
| soumbala / netetou | 1 600 / 720 | FAIBLE | `guide-netetou-soumbala`, `acheter-netetou-france` |
| soupou kandja | 720 | FAIBLE | `recette-soupoukandja` |
| mbakhalou Saloum | 320 | FAIBLE | `recette-mbakhalou-saloum`, `mbakhal-poisson-mbaxal-jen` |
| caldou / bassi salté | 140 / 50 | FAIBLE | `recette-caldou-senegalais`, `recette-basse-salte` |
| beignet banane/africain/sénégalais | 4 400/1 900/390 | FAIBLE | `beignet-banane-senegalais` (couvre le cluster, voir §4) |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain`, `guedj-ou-yeet-difference` |

Les 4 nouveaux articles (publiés le 15/08) ferment exactement les trous signalés la semaine dernière — bon signal d'exécution.

---

## 3. Les trous à occuper (PRIORITÉ)

Volume ≥ ~300/mois + concurrence **FAIBLE** + **aucun article dédié** (les termes apparaissent seulement en passage dans d'autres articles, jamais en page dédiée).

| # | Mot-clé | Vol./mois | Concurrence | Angle proposé | Produit à lier |
|---|---|---:|---|---|---|
| 1 | **lakh** | 1 300 | FAIBLE | Article dédié « lakh, la bouillie de mil fermentée » — distinct de fondé/araw (déjà traité), lakh = base de céréale fermentée avec lait caillé | `sankal-duggup`, `arraw-dugup` |
| 2 | **thiéré / couscous de mil** | 1 300 + 590 | FAIBLE | Article « qu'est-ce que le thiéré » (couscous de mil sénégalais) — mot-clé jamais traité en page dédiée malgré 20 mentions en passage | **produit direct : `thiere-champion`** |
| 3 | **niébé** | 1 300 | FAIBLE | Article « niébé, le haricot du Saloum » (nutrition + recettes) | **produit direct : `niebe-saloum`** |
| 4 | **jus de bouye** | 880 | FAIBLE | Angle recette/conservation à part du contenu bouye général — intention plus commerciale (boisson prête à consommer) | `bouye-baobab` |
| 5 | **ngalakh** | 590 | FAIBLE | Toujours ouvert depuis la semaine dernière — dessert (thiakry + bouye + pâte d'arachide), fête religieuse | `bouye-baobab`, `ciakri` |
| 6 | **poisson kong** | 320 | FAIBLE | Aucune mention nulle part sur le site (seul mot-clé à zéro occurrence) — article + optimisation fiche produit | **produit direct : `guej-kong`, `kongfume`** |

> #1–3 sont les plus gros volumes non traités du corpus actuel : lakh, thiéré et niébé ont chacun un produit ou un ingrédient déjà en catalogue mais zéro contenu éditorial dédié.
> Orthographes (lakh, ngalakh, thiéré, niébé) déjà utilisées ailleurs sur le site — pas de nouvelle graphie à valider avec Lamine.

### Optimisation rapide (pas un nouvel article)

- **beignet africain** (1 900, FAIBLE) : le terme apparaît déjà dans `beignet-banane-senegalais` mais pas dans le H1/title. Ajuster les balises meta pour capter le terme générique en plus de « beignet banane ».

---

## 4. Insights stratégiques

- **Progrès net cette semaine** : 4 trous sur 6 comblés depuis le dernier rapport → le rythme d'un article/semaine est tenu.
- **Le préfixe « acheter » ne se cherche pas en géo France.** Cluster achat-diaspora à 0 (« où acheter guedj », « acheter netetou »…) : les gens tapent le **nom du produit**, pas la tournure d'achat. Les articles `acheter-guedj-amerique-nord` / `-europe` restent valides — ils ciblent une autre géo (diaspora USA/Canada), non couverte par cette étude.
- **yeet reste le seul mot-clé réellement commercial** (CPC 1,12–4,33 €). Le reste du catalogue tourne à ~0 € de CPC → levier **SEO organique**, pas Ads payant.
- **Piège fonio confirmé** : CPC 20,70–172,75 € sur « fonio » — homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Ads.
- **Îles du Saloum** : les mots-clés Saloum (mbakhalou Saloum, crevettes séchées Saloum, pack Saloum) restent à faible volume individuellement mais couvrent bien le territoire de marque — aucune action requise, juste rappel de toujours écrire « Îles du Saloum » en entier dans les futurs contenus.

---

## 5. Limites de l'étude

- **Géo = France uniquement.** Les 0 sur le cluster diaspora sont normaux, pas un échec de ces articles.
- **Aucune donnée Search Console** : ce rapport ne présente ni positions, ni impressions, ni CTR — uniquement les CSV Ads déjà commités.
- **Volumes Google = fourchettes arrondies**, pas des chiffres exacts. « UNSPECIFIED » = pas assez de données, pas « zéro recherche ».

---

## 6. Recommandation

Ordre suggéré : **thiéré/couscous de mil → niébé → lakh** (les 3 plus gros volumes restants, chacun avec un produit direct en catalogue), puis `ngalakh` et `jus de bouye`. `poisson kong` en dernier (volume plus faible, mais zéro contenu actuel).
