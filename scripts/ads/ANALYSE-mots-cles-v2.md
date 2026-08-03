# Analyse mots-clés Google Ads — étude v2

_Source : `mots_cles_resultats_v2.csv` (étude du 12/07/2026, seeds élargies post-découvertes)._
_Croisé avec : étude v1 (`mots_cles_resultats.csv`), passerelle v3 (`mots_cles_passerelle_v3.csv`), les 32 articles du blog et les 55 fiches produits._
_Géo : France (2250) · Langue : français._

---

## 1. Verdict en une ligne

Le catalogue capte déjà **tous les gros volumes** (guedj, néré, cymbium, pain de singe, bissap, mafé…).
Les gains restants sont dans **6 plats/fruits à volume moyen et concurrence FAIBLE qui n'ont encore aucun article** — filons faciles à occuper avant les concurrents.

---

## 2. Déjà couvert — rien à faire (validation)

| Mot-clé | Vol./mois | Concurrence | Contenu existant |
|---|---:|---|---|
| guedj | 6 600 | FAIBLE | `quest-ce-que-le-guedj`, `les-7-guedj-du-senegal`, `comment-cuisiner/conserver-le-guedj` |
| néré | 6 600 | FAIBLE | `quest-ce-que-le-nere` |
| cymbium | 5 400 | FAIBLE | `yeet-cymbium-maggi-africain` + fiche `yeet-maggi` |
| pain de singe | 3 600 | MOYENNE | `pain-de-singe-bouye-baobab` + fiche `bouye-baobab` |
| soumbala | 1 600 | FAIBLE | `guide-netetou-soumbala` |
| bissap blanc/rouge | 1 600 / 390 | ÉLEVÉE | `bissap-hibiscus-guide` + fiches `bissap-blanc/rouge` |
| bouye | 1 300 | FAIBLE | `pain-de-singe-bouye-baobab` |
| yeet | 1 000 | FAIBLE | `yeet-cymbium-maggi-africain`, `guedj-ou-yeet-difference` |
| netetou / nététou | 720 / 590 | FAIBLE | `acheter-netetou-france`, `guide-netetou-soumbala` |
| soupou kandja | 720 | FAIBLE | `recette-soupoukandja` |
| mbakhalou saloum | 320 | FAIBLE | `recette-mbakhalou-saloum` |
| caldou | 140 | FAIBLE | `recette-caldou-senegalais` |

Rappel des gros volumes v1/v3 déjà couverts : bissap 60 500, pain perdu 90 500, riz au lait 74 000, dégué 12 100, recette mafé 9 900, yassa poulet 8 100, fonio 5 400, thiakry 4 400, beignet banane 4 400.

---

## 3. Les trous à occuper (PRIORITÉ)

Volume réel + concurrence **FAIBLE** + **aucun article dédié** aujourd'hui.

| # | Mot-clé | Vol./mois | Concurrence | Angle proposé | Produit à lier |
|---|---|---:|---|---|---|
| 1 | **beignet africain** | 1 900 | FAIBLE | Élargir/renommer `beignet-banane-senegalais` pour capter le terme générique | — |
| 2 | **thiébou yapp** | 1 300 | FAIBLE | Nouvel article recette (riz à la viande) — pendant du thiéboudienne | `thiere-champion`, tigadegue |
| 3 | **ditakh / ditax** | ~1 090 | FAIBLE | Article « le ditakh, fruit du Saloum » (info + culture) | pas de produit → SEO pur |
| 4 | **bouillie de mil** | 1 000 | FAIBLE | Article rattaché aux céréales | `arraw-dugup`, `sankal-duggup` |
| 5 | **domoda** | 880 | FAIBLE | Nouvel article recette (ragoût tomate/arachide) | tigadegue, `guerte-noflay` |
| 6 | **ngalakh** | 590 | FAIBLE | Article dessert (thiakry + bouye + pâte d'arachide) — croise 3 produits | `bouye-baobab`, `ciakri`, tigadegue |

> Tous en concurrence FAIBLE : peu de sites français les couvrent → positionnement rapide possible.
> `ditakh` n'a pas de produit associé (fruit non vendu) : article utile pour l'autorité de marque, pas pour la conversion directe.

---

## 4. Insights stratégiques

- **Le préfixe « acheter » ne se cherche pas (en géo France).** Tout le cluster achat-diaspora est à 0 : « où acheter guedj » = 0, « acheter netetou » = 0, « acheter poisson séché » = 0. Les gens tapent le **nom du produit**, pas « acheter X ». → SEO sur les noms de produits, pas sur les tournures d'achat.
- **guedj (6 600) ≈ néré (6 600) ex aequo.** Le néré/soumbala pèse autant que le produit phare guedj — le `guide-netetou-soumbala` mérite d'être aussi soigné que les pages guedj.
- **yeet = seul mot-clé réellement commercial** (CPC 1,12–3,20 €). Tout le reste est à ~0 € : ces requêtes sont **informationnelles** → stratégie **SEO organique**, pas Google Ads payant, sur l'essentiel du catalogue.
- **Piège fonio (v1).** « fonio » remonte un CPC 20,70–172,75 € : c'est un homonyme (ticker/finance), pas notre céréale. **Ne jamais enchérir dessus en Ads.**

---

## 5. Limites de l'étude (à savoir avant d'agir)

- **Géo = France uniquement.** Les mots-clés diaspora (USA/Canada) sortent à 0 ici mais ont du volume sur leur propre géo. Les articles `acheter-guedj-amerique-nord` / `-europe` ne sont pas invalidés par ce 0 — ils ciblent une autre géo. Refaire une passe en géo US/CA pour les valider.
- **Volumes Google = fourchettes arrondies**, pas des chiffres exacts.
- **UNSPECIFIED / 0** = pas assez de données, pas forcément « aucune recherche ».

---

## 6. Recommandation

Créer **3 articles prioritaires** dans l'ordre : `thiébou yapp` → `domoda` → `ngalakh` (recettes qui lient des produits vendus), puis élargir `beignet-banane` vers « beignet africain ». Les mots-clés à 0 € confirment que le levier est le **SEO organique**, pas l'achat Ads (sauf éventuellement `yeet`).
