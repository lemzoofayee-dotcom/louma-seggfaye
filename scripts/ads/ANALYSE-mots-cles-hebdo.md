# Analyse mots-clés Google Ads — Lundi 05/10/2026

> **Analyse cloud, aucune donnée neuve générée.** Pas d'accès à l'API Google Ads ni à Google Search Console depuis le cloud.
> Source : les 5 CSV déjà commités dans `scripts/ads/` (`mots_cles_resultats.csv` v1, `mots_cles_resultats_v2.csv` + son snapshot du 05/08, `mots_cles_passerelle_v3.csv`, **`mots_cles_elargie_v4.csv` — nouveau**).
> **Nouveauté cette semaine** : le pull à seeds élargies demandé depuis plusieurs semaines a été fait en local le 30/09 (commit `398a1e1`) — 4 nouveaux clusters (`poisson-frais`, `conservation`, `fetes`, `cadeaux-diaspora`). Les 4 autres CSV sont inchangés depuis le 23/09.
> Croisé avec : `ls blog/` (54 articles) et `ls produits/` (55 fiches).
> Géo des études : France · langue FR.

---

## 1. Verdict en une ligne

**Le pull élargi demandé a enfin eu lieu — et il sort un vrai trou** : « poisson africain » (480/mois, concurrence FAIBLE, 0 contenu dédié). Le reste du nouveau cluster `poisson-frais` (tilapia, poisson capitaine, poisson braisé, thiof) est déjà bien couvert par les fiches produits dédiées ; les clusters `fetes` et `cadeaux-diaspora` ne sortent que des volumes trop faibles (≤ 90/mois) pour ce pull-ci.

---

## 2. Déjà couvert (validation)

### Cluster `poisson-frais` (nouveau, v4)

| Mot-clé | Vol./mois | Concurrence | Contenu |
|---|---:|---|---|
| tilapia | 18 100 | FAIBLE | `produits/tilapia-rouge.html` (+ mentionné dans `poisson-braise.html`, `produits-senegalais-france.html`, `recette-caldou-senegalais.html`) |
| poisson capitaine | 5 400 | FAIBLE | `produits/beurre-capitaine.html` (« le gros poisson capitaine »), `produits/diane-capitaine.html` (« le petit poisson capitaine ») |
| poisson braisé | 1 000 | FAIBLE | `blog/poisson-braise.html` (title ciblé explicitement) |
| thiof | 590 | FAIBLE | `produits/thiof-decoupe.html` + `blog/quel-poisson-thieboudienne.html` (« Le thiof et ses cousins ») |
| sardinelle | 260 (sous le seuil, déjà couvert) | FAIBLE | `blog/kethiakh-sardinelle-fumee-senegal.html`, fiche `produits/yaboye.html` |

### Clusters `fetes` / `conservation` / `cadeaux-diaspora` (nouveau, v4)

Aucun mot-clé n'atteint le seuil de 300/mois dans ces 3 clusters sur ce pull (max : « buffet africain » 90/mois, « poisson fumé africain » 140/mois déjà couvert par les articles guedj/conservation existants, « épicerie fine africaine » 40/mois). Rien à traiter cette semaine de ce côté — volumes trop faibles pour prioriser un article dédié, à garder en réserve si un futur pull confirme une tendance à la hausse.

### Rappel — clusters déjà validés les semaines précédentes (v1, v2, passerelle v3, inchangés depuis le 23/09)

bissap, pain perdu, riz au lait, dégué, recette mafé, guedj, yassa poulet, néré, cymbium, épicerie africaine, fonio (⚠️ piège CPC, voir §4), beignet africain/banane, thiakry, bissap blanc, soumbala, thiébou yapp, pain de singe/bouye/poudre de baobab, lakh/bouillie de mil, thiéré/couscous de mil, niébé, yeet, ditakh, domoda, jus de bouye, dessert sénégalais, netetou/nététou, soupou kandja, ngalakh, recette thieboudienne, bissap rouge, oseille de guinée, beignets sénégalais, mbakhalou saloum, poisson kong, caldou — tous couverts, voir rapport du 28/09 pour le détail.

---

## 3. Les trous à occuper (PRIORITÉ)

| Mot-clé | Vol./mois | Concurrence | Angle d'article proposé | Produit à lier |
|---|---:|---|---|---|
| **poisson africain** | **480** | **FAIBLE** | Article hub « Quels sont les poissons africains/sénégalais ? » — guide des espèces vendues chez Louma (frais et séché), qui maille vers toutes les fiches poisson existantes. Terme générique porteur pour le SEO informationnel (pas de produit unique à cibler, c'est une page de maillage). | `thiof-decoupe`, `tilapia-rouge`, `beurre-capitaine`, `diane-capitaine`, `poisson-sompate`, `poisson-eau-douce`, `seude-baracouda`, `yakh-carpe-rouge` |

C'est le seul trou strict (volume ≥ 300/mois + concurrence FAIBLE + zéro article/fiche dédié) remonté par les 5 CSV cette semaine. Il vient entièrement du nouveau pull élargi v4.

---

## 4. Insights stratégiques

- **Le pull élargi a fonctionné une fois, mais n'a ouvert qu'un seul trou.** Les 4 nouveaux clusters (poisson-frais, conservation, fêtes, cadeaux-diaspora) représentaient le pari pour sortir du statu quo des 4 semaines précédentes — le pari est à moitié payant : 1 trou réel (« poisson africain »), le reste du volume est soit déjà couvert (poisson-frais), soit trop faible pour prioriser (fêtes, conservation, cadeaux-diaspora, tous ≤ 140/mois).
- **« poisson africain » est une page de maillage, pas une fiche produit.** Contrairement aux trous habituels liés à un produit précis, ce mot-clé générique appelle un article de blog qui agrège les 8 fiches poisson existantes plutôt qu'une nouvelle fiche produit — bon levier pour le maillage interne du catalogue poisson.
- **Piège fonio inchangé.** « fonio » (5 400/mois) republie un CPC 20-172 € : homonyme finance (ticker), pas la céréale. Ne jamais enchérir dessus en Google Ads — trafic 100 % organique sur `fonio-cereale-sans-gluten.html`.
- **Le préfixe « acheter » / la diaspora ne se cherchent pas en géo France.** Normal pour cette géo (voir v2/v3) — les articles diaspora (`acheter-guedj-amerique-nord.html`, `acheter-guedj-europe.html`) ne sont pas invalidés par ces volumes à 0.
- **CPC quasi nul sur tout le catalogue sauf yeet** → les requêtes informationnelles (dont « poisson africain », CPC non mesuré dans v4 — pas de colonne CPC sur ce pull) restent un levier SEO organique, pas Ads payant.
- **Prochaine étape utile côté data** : le cluster `poisson-frais` n'a pas de colonnes CPC (le script `etude_elargie_v4.py` n'en extrait pas) — à ajouter si un futur pull Ads veut chiffrer le potentiel commercial de « poisson africain » / « tilapia ».

---

## 5. Limites de l'étude (à lire avant d'agir)

- Cette routine cloud n'a pas accès à l'API Google Ads ni à Google Search Console — elle recoupe uniquement les 5 CSV déjà commités. Un nouvel élargissement de seeds nécessite une session locale (`etude_mots_cles.py` / `etude_mots_cles_v2.py` / `etude_passerelle_v3.py` / `etude_elargie_v4.py`).
- **Le CSV v4 n'a pas de colonnes CPC** (`cpc_bas_eur`/`cpc_haut_eur` absentes), contrairement aux CSV v1/v2 — aucun chiffre de coût par clic n'est disponible pour « poisson africain » ou les autres mots-clés de ce pull.
- **Géo = France uniquement.** Le cluster diaspora (achat USA/Canada) ressort à 0 ici, c'est attendu.
- **Volumes Google Ads = fourchettes arrondies**, pas des chiffres exacts. `UNSPECIFIED` = pas assez de données, pas « zéro recherche ».
- **Positions/impressions/CTR réels** : uniquement dans `scripts/seo/gsc-data.md` (généré en local), jamais dans cette analyse.

---

## 6. Recommandation

Lamine décide : si « poisson africain » (480/mois, concurrence FAIBLE) mérite un article hub de maillage vers les 8 fiches poisson du catalogue. Côté data, ajouter les colonnes CPC au prochain pull v4/v5 pour pouvoir chiffrer le potentiel commercial de ce cluster.

**Les 3 trous prioritaires de la semaine : un seul — « poisson africain » (480/mois, concurrence faible, 0 article dédié). Pas d'autre trou strict remonté par les 5 CSV cette semaine.**
