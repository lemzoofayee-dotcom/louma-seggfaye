# Rapport SEO — Semaine du 15 juillet 2026

**Domaines audités :** seggfaye.com · guide.seggfaye.com
**Concurrent de référence :** maya-boutique.fr
**Autres concurrents surveillés :** racines-shop.com · enviesdafrique.fr

---

## 1. Tableau de positionnement Google

| Mot-clé | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader actuel |
|---|---|---|---|---|
| produits exotiques africains france | Absent | Absent | Visible (résultats produits) | NKOSI / racines-shop.com |
| produits halieutiques seches senegal | Absent | Absent | Catégorie dédiée | espaceagro.com (B2B) |
| poisson seche senegalais acheter | Absent | Absent | Absent | ISSANNY / NKOSI / Grand Exotique |
| guedj acheter france | Blog ~pos 7 | Absent | Catégorie halieutiques | magasin-africain.com |
| netetou acheter | Absent | Absent | Absent | Amazon FR / NKOSI / Carafrique |
| epicerie africaine en ligne | Absent | Absent | Absent | NKOSI (#1) / ISSANNY (#2) |
| produits senegalais en ligne | Absent | Absent | Visible (~pos 5) | Sunu Alimentation / Niokobok |
| recette thieboudienne ingredients | Absent | Absent | Absent | MesEpices / InspiFoodByKinouche |
| crevettes sechees senegal | Absent | Absent | Absent | ExoticaSénégal / Magasin-Africain |
| ou acheter du guedj en france | Blog ~pos 6 | Absent | Présent (halieutiques) | magasin-africain.com |
| acheter netetou en ligne france | Absent | Absent | Absent | NKOSI / Amazon FR |

**Synthèse positionnement :** seggfaye.com n'est visible que sur 2 requêtes guedj (via le blog), grâce à l'article "Qu'est-ce que le guedj". Sur tous les autres mots-clés, aucune position détectée. guide.seggfaye.com n'apparaît sur aucune requête.

---

## 2. Analyse concurrentielle

### maya-boutique.fr

**Ce qu'ils font mieux :**
- Structure WooCommerce classique (URLs `/product-category/`) favorisée par Google Shopping
- Catégories claires indexées : produits halieutiques, boissons, huiles, accessoires, céréales, marché
- Visibilité organique sur "produits sénégalais en ligne" (~pos 5)
- Ancienneté domaine probable (signal d'autorité fort)
- Large diversification : alimentaire + accessoires + bien-être

**Nos avantages sur eux :**
- Expertise contenu inégalée (28 articles de blog vs 0 côté maya-boutique.fr)
- Identité forte : Guedjologue, Îles du Saloum, sourcing direct artisanal
- Schema markup avancé (Recipe, FAQPage, Article, BreadcrumbList, VideoObject)
- Catalogue plus profond sur le guedj : 7 variétés spécifiques vs guedj beurre seul chez maya
- 92 URLs au sitemap vs structure maya-boutique beaucoup moins dense en contenu

**Faiblesse commune :** ni l'un ni l'autre ne capte les requêtes générales "épicerie africaine en ligne" — dominées par NKOSI et racines-shop.com.

---

### racines-shop.com

Acteur historique (depuis 1987), large catalogue (marques industrielles : Bonmafé, Bonnet Rouge, Maggi, Nido, etc.) + section bio. Livraison Mondial Relay gratuite dès 50€. Autorité de domaine très élevée. Cible : diaspora généraliste, pas la niche guedj/produits artisanaux Saloum. Pas un concurrent direct sur notre positionnement d'expertise.

### enviesdafrique.fr

Présent sur "poissonnerie" et "poissons et fruits de mer" (stockfish, capitaine 5kg). Pas de guedj spécifique identifié. Concurrent indirect : s'ils développent une offre guedj sénégalais artisanal, ils pourraient empiéter sur notre terrain.

### Concurrents émergents à surveiller

- **NKOSI (nkosiagro.com)** : épicerie africaine/antillaise/exotique, 500+ références, livraison rapide, visibilité forte sur "épicerie africaine en ligne" et "netetou acheter". Blog actif (ex : Africa Day 2026).
- **Grand Exotique (grandexotique.com)** : visible sur "guedj acheter france" et "poisson seche senegalais acheter". Concurrent direct sur le guedj.
- **magasin-africain.com** : leader actuel sur "guedj acheter france" et "ou acheter du guedj en france". À surveiller.
- **Exotica Sénégal (exoticasenegal.fr)** : visible sur "crevettes sechees senegal". Niche proche.

---

## 3. État des rich snippets

### seggfaye.com

| Type | Page | Statut |
|---|---|---|
| FAQPage (6 questions) | /blog/quest-ce-que-le-guedj.html | Structurellement correct |
| Recipe + FAQPage + VideoObject | /blog/recette-jus-de-bissap.html | Structurellement correct |
| Recipe + FAQPage | /blog/recette-basse-salte.html | Structurellement correct |
| BreadcrumbList | Toutes les pages blog | Structurellement correct |
| AggregateRating sur Organization | index.html | PROBLÈME (voir ci-dessous) |

**SIGNALEMENT — À NE PAS CORRIGER SANS VALIDATION DE LAMINE :**

La homepage (index.html) contient un `aggregateRating` (ratingValue "5", reviewCount "8") attaché à l'entité `Organization`. Google n'affiche plus les étoiles sur Organization depuis 2019 et peut interpréter cette donnée comme un balisage trompeur. Risque : pénalité Search Actions. Les étoiles/avis restent hors périmètre de l'agent SEO — Lamine doit décider s'il faut supprimer ce bloc ou le déplacer sur des pages produits individuelles (Product schema) avec de vrais avis clients vérifiables.

### guide.seggfaye.com

**PROBLÈME CRITIQUE : guide.seggfaye.com n'est pas indexé par Google.**

La recherche `site:guide.seggfaye.com` ne retourne aucun résultat. Pourtant :
- Le fichier `robots.ts` autorise correctement l'indexation (`allow: "/"`)
- Le `sitemap.ts` génère dynamiquement des URLs pour les plats et produits
- Les pages plats comportent probablement un schema Recipe

Des dizaines de pages recettes avec rich snippets potentiels sont actuellement invisibles. Il faut soumettre guide.seggfaye.com à Google Search Console et Bing Webmaster Tools.

---

## 4. Actions prioritaires de la semaine

### ACTION 1 — Soumettre guide.seggfaye.com à Google Search Console
**Impact estimé :** Élevé | **Délai de résultat :** 4 à 8 semaines

Le guide de recettes n'est pas du tout indexé. Une fois soumis dans Search Console (propriété de domaine ou préfixe d'URL), Google va crawler les pages plats et déclencher les rich snippets Recipe (étoiles, temps de préparation, image). C'est le levier le plus rapide disponible sans écrire une ligne de code.

Étapes : Search Console > Ajouter une propriété > `guide.seggfaye.com` > Méthode DNS ou balise meta > Soumettre le sitemap `https://guide.seggfaye.com/sitemap.xml` > Demander l'indexation de la page d'accueil en priorité.

---

### ACTION 2 — Créer ou optimiser une page dédiée "netetou acheter france"
**Impact estimé :** Moyen à élevé | **Délai de résultat :** 6 à 12 semaines

"netetou acheter" et "acheter netetou en ligne france" ont une demande réelle (Amazon FR, NKOSI, Carafrique, Kissafrica, Miamland sont tous positionnés). Seggfaye.com a 4 formats de nététou (dôme, barre, mixte, poudre) + l'article "quest-ce-que-le-nere.html" déjà en base. Manque : une page d'atterrissage optimisée pour l'intention d'achat.

Proposition : optimiser `/produits/netetu-dom.html` et ses variantes avec les balises title/meta incluant "acheter netetou france", puis créer un article comparatif des formats (dôme vs barre vs poudre) avec lien interne vers chaque produit et schema FAQPage.

---

### ACTION 3 — Renforcer les liens internes depuis le blog vers les pages produits guedj
**Impact estimé :** Moyen | **Délai de résultat :** 4 à 8 semaines

Les articles de blog guedj (quest-ce-que-le-guedj, les-7-guedj-du-senegal, acheter-guedj-france, comment-cuisiner-le-guedj, guedj-ou-yeet-difference) génèrent des visites organiques (~pos 6-7 sur "où acheter du guedj en france"). Or, aucun de ces articles ne transfère du PageRank vers les pages produits `/produits/guej-beurre.html`, `/produits/guej-yass.html`, etc. Ajouter des liens contextuels dans le corps du texte (ex : "le guedj beurre" → lien vers `/produits/guej-beurre.html`) permettrait de faire remonter les pages produits dans les SERP transactionnels.

---

## 5. Estimation du délai pour dépasser maya-boutique.fr

| Segment de mots-clés | Délai estimé | Condition |
|---|---|---|
| "guedj" (toutes variantes) | 2 à 4 mois | Actions 1 + 3 exécutées |
| "netetou acheter" | 4 à 6 mois | Action 2 exécutée, 1 article de soutien |
| "produits senegalais en ligne" | 8 à 12 mois | Nécessite maillage interne + liens externes |
| "epicerie africaine en ligne" | +12 mois | Segment dominé par acteurs établis (NKOSI, Racines) |

**Conclusion :** Sur notre niche (guedj, produits halieutiques sénégalais artisanaux, Îles du Saloum), le contenu de seggfaye.com est déjà supérieur à maya-boutique.fr. Le blocage principal est technique (guide.seggfaye.com non indexé) et structurel (pas de liens internes blog → produits). Corriger ces deux points peut produire un delta visible en 2 à 3 mois.

---

*Rapport généré le 15 juillet 2026 — Agent SEO Louma by Seggfaye*
