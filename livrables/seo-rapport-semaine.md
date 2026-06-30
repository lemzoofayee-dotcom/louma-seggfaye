# Rapport SEO hebdomadaire — Semaine du 30 juin 2026

**Domaines suivis :** seggfaye.com · guide.seggfaye.com · maya-boutique.fr  
**Généré le :** 30/06/2026

---

## 1. Tableau de positionnement Google

| Mot-clé | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader actuel |
|---|---|---|---|---|
| produits exotiques africains france | Non classé | Non classé | Non classé | exotiquepro.fr, sougouexpress.com |
| produits halieutiques sechés sénégal | Non classé | Non classé | **Visible** (cat.) | espaceagro.com |
| poisson seché sénégalais acheter france | Non classé | Non classé | Non classé | espaceagro.com, issanny.com |
| guedj acheter france | Non classé | Non classé | **Visible** (cat.) | grandexotique.com, magasin-africain.com, keryaye.fr |
| netetou acheter en ligne | Non classé | Non classé | **Visible** (produit) | amazon.fr, sunualimentation.com, carafrique.fr |
| épicerie africaine en ligne | Non classé | Non classé | Non classé | sougouexpress.com, maryexotik.com |
| produits sénégalais en ligne | Non classé | Non classé | **Top 5** | sunualimentation.com, niokobok.com |
| recette thiéboudienne ingrédients | Non classé | Non classé | Non classé | nkosiagro.com, kelianfood.com |
| crevettes sechees sénégal | Non classé | Non classé | Non classé | espaceagro.com, timifood.com |
| ou acheter guedj en france | Non classé | Non classé | **Visible** (cat.) | afroleck.com, magasin-africain.com |

**Bilan :** seggfaye.com et guide.seggfaye.com ne rankent sur aucun des mots-clés testés cette semaine. Les pages et articles existent (sitemap correct, contenu réel), mais l'autorité de domaine est trop récente pour percer les résultats compétitifs. maya-boutique.fr est visible sur 4/10 mots-clés grâce à son ancienneté et sa structure WooCommerce.

---

## 2. Analyse concurrentielle

### maya-boutique.fr

**Forces :**
- Domaine établi avec historique d'autorité, structure WooCommerce (URLs `/product-category/`, `/product/`)
- Catégorie dédiée "Produits halieutiques" indexée et rankée pour les requêtes halieutiques
- Positionnement clair "Le Sénégal à votre porte", tagline mémorisable
- Visible top 5 pour "produits sénégalais en ligne" (mot-clé à fort volume)
- Catalogue large : alimentaire + ustensiles + déco + bien-être + box cadeaux
- Storytelling fondatrice (Ndeye, entrepreneuriat féminin sénégalais) = avantage éditorial

**Faiblesses :**
- Aucun contenu de blog/éducation détecté sur les requêtes informionnelles (qu'est-ce que le guedj, comment conserver, recettes...)
- Pas d'identité d'expert spécialisé, positionnement généraliste "produits africains"
- Pages produits basiques, pas de storytelling produit-par-produit
- Pas de schema Recipe, pas de contenu SEO sur les recettes sénégalaises
- Pas de présence TikTok/réseaux sociaux visible dans les SERPs

**Notre avantage vs maya-boutique.fr :**
- Niche ultra-spécialisée (guedj, guedjologue, Îles du Saloum) = autorité thématique potentielle forte sur le long terme
- Blog avec 15+ articles sur les requêtes que maya-boutique.fr n'adresse pas (types de guedj, conservation, recettes avec schema Article)
- Identité créatrice de contenu TikTok (@seggfaye) qui alimente le trafic direct et les backlinks naturels
- guide.seggfaye.com comme deuxième domaine capte les requêtes "guide produits africains"

### racines-shop.com

- Établi depuis 1987, très large catalogue "épicerie africaine et indienne"
- Se positionne sur le volume ("la plus large offre"), pas la spécialisation
- Peu de contenu éditorial détecté

### enviesdafrique.fr

- Marketplace B2B+B2C, catalogue vaste mais généraliste
- Positionnement "premier marketplace africain", pas spécialisé Sénégal

---

## 3. État des rich snippets

### seggfaye.com

| Rich snippet | Status | Détail |
|---|---|---|
| FAQPage | **Implémenté, non confirmé visible** | Schema présent sur index.html et epicerie-africaine.html, 4 questions. Domaine trop récent, Google ne l'affiche pas encore. |
| AggregateRating (étoiles) | **Implémenté incorrectement** | Le schema AggregateRating est attaché à l'entité `Organization` (5/5, 8 avis). Google n'affiche pas les étoiles pour Organization dans les SERPs, seulement pour `Product`, `Recipe` ou `LocalBusiness`. Les étoiles ne sont pas visibles. |
| Recipe | **Absent** | Les articles de recettes (thiéboudienne, yassa, soupoukandja, mafé, mbakhalou...) utilisent le schema `Article`, pas `Recipe`. Aucun rich snippet recette possible actuellement. |
| Product schema | **Absent** | Pas de schema Product avec AggregateRating sur les fiches produits individuelles. Opportunité manquée pour les étoiles produit. |
| Sitelinks | **Non détecté** | Domaine trop récent. |

### guide.seggfaye.com

| Rich snippet | Status | Détail |
|---|---|---|
| Recipe | **Absent ou non détecté** | Le layout.tsx ne contient pas de schema Recipe. Les pages `/plats/[slug]` devraient implémenter des schemas Recipe individuels pour chaque plat. |
| Product schema | **À vérifier** | Les pages `/produits/[slug]` devraient avoir des schemas Product avec des informations de prix et disponibilité. |
| FAQ | **Non détecté** | Pas de FAQPage dans le layout global. |

---

## 4. Actions prioritaires cette semaine

### Action 1 — Convertir les schemas Article en Recipe sur les recettes du blog

**Impact : ÉLEVÉ | Effort : Moyen | Délai résultats : 4-8 semaines**

Les 7 articles de recettes du blog seggfaye.com (thiéboudienne, yassa, soupoukandja, mafé, mbakhalou, caldou, bissap) utilisent `@type: Article`. Remplacer par `@type: Recipe` avec les champs `recipeIngredient`, `recipeInstructions`, `prepTime`, `cookTime`, `recipeYield`, `author` et `AggregateRating`.

Cela permettra d'obtenir des rich snippets dans les SERPs avec : temps de préparation, étoiles, photo du plat. Les recettes sénégalaises sont peu couvertes en France avec des schémas Recipe correctement structurés.

### Action 2 — Corriger l'AggregateRating : passer de Organization à Product sur les fiches produits

**Impact : MOYEN | Effort : Faible | Délai résultats : 2-4 semaines**

Actuellement, les étoiles sont sur `Organization` (invalide pour les SERPs). Créer un schema `Product` avec `AggregateRating` sur les pages individuelles des produits phares (guedj beurre, guedj kong, netetou, crevettes). Google affiche les étoiles pour les entités Product dans les résultats de recherche, ce qui augmente le CTR de 20-60%.

### Action 3 — Publier un article cible "acheter netetou france" + renforcer les backlinks

**Impact : ÉLEVÉ (longue traîne peu compétitive) | Effort : Faible | Délai résultats : 6-12 semaines**

Le mot-clé "netetou acheter en ligne" est dominé par amazon.fr et des petites épiceries. seggfaye.com a déjà un blog article `guide-netetou-soumbala.html` mais il ne cible pas explicitement l'achat. Créer une page dédiée `/netetou-france.html` avec contenu éditorial (qu'est-ce que le netetou, comment l'utiliser, différences barre/dôme/poudre) + CTA WhatsApp/commande. Soumettre l'URL à Google Search Console pour indexation rapide.

En parallèle, obtenir 2-3 mentions/backlinks depuis des blogs de cuisine sénégalaise ou des groupes Facebook diaspora (ex. partage de l'article thiéboudienne dans des groupes Sénégal/France avec lien retour).

---

## 5. Estimation du délai pour dépasser maya-boutique.fr

| Segment | Délai estimé | Stratégie |
|---|---|---|
| Mots-clés niche (guedj, yeet, guedjologue, Îles du Saloum) | **3-6 mois** | Autorité thématique + blog existant. Avantage compétitif réel. |
| Mots-clés produits (acheter guedj france, netetou acheter) | **4-8 mois** | Pages produits optimisées + schema Product + backlinks ciblés. |
| Mots-clés génériques (produits sénégalais en ligne) | **8-14 mois** | Nécessite autorité de domaine + volume de pages indexées. |
| Mots-clés très compétitifs (épicerie africaine en ligne) | **14-24 mois** | Concurrence large + domaines établis (sougouexpress, magasin-stalingrad). Objectif secondaire. |

**Conclusion :** maya-boutique.fr est dépassable sur la niche guedj/Îles du Saloum en 3-6 mois si les schémas Recipe sont implémentés et que le blog continue à produire du contenu informatif de qualité. Le positionnement de "spécialiste" est plus fort que leur positionnement "généraliste". Sur les mots-clés large spectre "épicerie africaine", le dépassement n'est pas prioritaire et prendra 12-24 mois.

---

*Rapport généré automatiquement par l'agent SEO Louma — Données : 30/06/2026*
