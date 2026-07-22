# Rapport SEO Semaine du 22 juillet 2026

> Agent SEO automatique. Aucune note, avis, étoile ni prix modifié.
> Toutes les corrections proposées sont à valider par Lamine avant application.

---

## 1. Tableau de positionnement Google

| Mot-clé | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader actuel |
|---|---|---|---|---|
| produits exotiques africains france | ~Top 10 (blog) | Non indexé | ~Top 5 | NKOSI, nomad-exotic.com |
| produits halieutiques séchés sénégal | Non classé | Non indexé | Non classé | espaceagro.com |
| poisson seche senegalais acheter france | Non classé | Non indexé | Non classé | ISSANNY, espaceagro.com |
| guedj acheter france | ~Top 10 (article blog) | Non indexé | ~Top 15 (fiche produit) | magasin-africain.com, afroleck.com |
| netetou acheter | Non classé | Non indexé | Non classé | NKOSI, sunualimentation.com |
| epicerie africaine en ligne | Non classé | Non indexé | Non classé | NKOSI, ISSANNY |
| produits senegalais en ligne | Non classé | Non indexé | Non classé | NKOSI, sunualimentation.com |
| recette thieboudienne ingredients | Non classé | Non indexé | Non classé | ileauxepices.com, o-poisson.fr |
| crevettes sechees senegal | Non classé | Non indexé | Non classé | exoticasenegal.fr |
| cuisine senegalaise produits | Non classé | Non indexé | Non classé | cuisinemetisse.fr, NKOSI |
| ou acheter du guedj en france | Non classé | Non indexé | Non classé | magasin-africain.com, ISSANNY |
| acheter netetou en ligne | Non classé | Non indexé | Non classé | NKOSI, Amazon.fr |

**Légende :** "Non indexé" = aucune page de ce domaine apparaît dans les résultats pour cette requête. "Non classé" = présence inexistante ou hors Top 30 estimé.

### Observations clés

- seggfaye.com a une présence réelle sur les requêtes "guedj" grâce aux articles de blog, mais reste absent des requêtes transactionnelles.
- guide.seggfaye.com est pratiquement invisible : une seule page ("dibi") apparaît dans Google. C'est le problème le plus urgent.
- maya-boutique.fr apparaît sur ses propres fiches produits mais pas sur les requêtes génériques, ce qui confirme un faible travail éditorial.

---

## 2. Analyse concurrentielle

### maya-boutique.fr (Lyon)

**Forces :**
- E-commerce mature (WooCommerce/WordPress), tunnel d'achat complet
- Catalogue large : alimentaire + accessoires + décoration + traiteur
- Catégorie "produits halieutiques" avec plusieurs sous-produits (guedj beurre, kong fumé, yett, pagne)
- Page "Recettes" pour attirer du trafic informationnel
- Présence Google My Business (Lyon)

**Faiblesses :**
- Zéro contenu éditorial expert : aucun article de fond, aucune page "guide"
- Produits décrits très brièvement, pas de contenu long
- Gamme trop large et non différenciante (décoration, santé, textile = dilution)
- Pas d'identité forte ni d'angle unique
- Visibilité limitée hors de son propre nom de marque

**Nos avantages vs maya-boutique :**
- Contenu expert profond : l'article "quest-ce-que-le-guedj" est déjà indexé et visible
- Identité unique (Guedjologue, Îles du Saloum) = autorité de niche que maya-boutique ne peut pas copier
- Spécialisation sur les produits halieutiques des Îles du Saloum = différenciation réelle
- guide.seggfaye.com = futur actif SEO considérable si indexé correctement

### Autres concurrents à surveiller

| Concurrent | Point fort | Menace |
|---|---|---|
| NKOSI (nkosiagro.com) | 500+ produits, livraison 48h, très bien référencé | Leader sur "épicerie africaine" et "netetou" |
| ISSANNY (issanny.com) | Bien positionné sur "guedj" et "épicerie africaine" | Concurrent direct sur guedj et produits sénégalais |
| magasin-africain.com | #1-3 sur "ou acheter guedj france" | Forte autorité de domaine sur le guedj |
| racines-shop.com | 30 ans d'existence, large catalogue ethnique | Autorité de domaine très élevée |
| enviesdafrique.fr | Marketplace 100% africaine, modèle B2B+B2C | Croissance rapide, plusieurs vendeurs |

---

## 3. État des rich snippets

### guide.seggfaye.com (schémas Recipe/FAQ)

**Situation :** guide.seggfaye.com est quasi-absent des résultats Google (1 seule page indexée sur l'ensemble du site). Les schémas Recipe ne peuvent pas générer de rich snippets si les pages ne sont pas indexées.

**Ce qu'il faut vérifier (à faire manuellement) :**
- Soumettre le sitemap de guide.seggfaye.com dans Google Search Console
- Vérifier que le fichier robots.txt de guide.seggfaye.com n'empêche pas l'indexation
- Vérifier que le schema `@type: Recipe` est bien présent dans le HTML des pages de recettes

**SIGNAL :** Aucun schema Recipe ni FAQ n'est apparu dans les SERP pour les requêtes testées. Soit les pages ne sont pas indexées, soit les schémas sont absents ou mal formés.

### seggfaye.com (étoiles AggregateRating)

**Situation :** L'article "quest-ce-que-le-guedj" et le blog apparaissent dans les SERP sans rich snippets (pas d'étoiles, pas de FAQ, pas de breadcrumbs enrichis).

**SIGNAL À VÉRIFIER (mais non corrigé par cet agent) :**
Un commit récent (fcfc887) a corrigé `worstRating 5→1` sur le schema Organization. Si un `aggregateRating` est positionné sur un élément Organization (plutôt que sur un Product ou un Article), Google l'ignorera. Ce point est à valider par Lamine avec l'outil de test des données structurées de Google (search.google.com/test/rich-results).

**Ce que cet agent ne touche pas :**
- Aucune modification des `aggregateRating`, `ratingValue`, `reviewCount` ni des balises `Review`
- Les avis et étoiles restent 100% sous contrôle de Lamine

### FAQ structurée

Aucune FAQ structurée n'a été détectée dans les résultats de recherche pour nos pages. À vérifier si des balises `FAQPage` sont présentes dans les articles de blog.

---

## 4. Les 3 actions prioritaires

### Action 1 : Indexer guide.seggfaye.com (URGENT)

**Impact estimé : Élevé / Délai : 2-4 semaines**

guide.seggfaye.com est un actif SEO majeur avec des dizaines de recettes mais 1 seule page indexée. C'est la perte de valeur SEO la plus grave identifiée cette semaine.

**À faire :**
1. Ouvrir Google Search Console pour guide.seggfaye.com
2. Soumettre le sitemap XML du guide
3. Inspecter le robots.txt et la configuration Next.js pour s'assurer que le crawling est autorisé
4. Demander l'indexation manuelle des 5-10 pages les plus importantes (thieboudienne, yassa, mafé...)

**Note technique :** Le guide est en Next.js (TypeScript). Vérifier que le `next.config.ts` ne désactive pas les métadonnées ou le rendu SSR/SSG, qui sont indispensables pour l'indexation.

### Action 2 : Créer une page "Acheter netetou en ligne" sur seggfaye.com

**Impact estimé : Moyen-Élevé / Délai SEO : 4-8 semaines**

"netetou acheter" et "acheter netetou en ligne" sont des requêtes avec forte intention d'achat. Nos concurrents NKOSI et Amazon.fr y répondent, mais pas nous malgré le fait que nous vendons du netetou.

**À faire :**
1. Créer un article de blog dédié `/blog/acheter-netetou-france.html` (format guide complet : qu'est-ce que le netetou, comment le choisir, où acheter, pourquoi Louma)
2. Lier cet article à la fiche produit `/produits/netetu-dom.html` et `/produits/netetu-poudre.html`
3. Optimiser les titles et meta descriptions des fiches produit netetou (actuellement non visibles dans les SERP)

### Action 3 : Soumettre les fiches produits à Google Search Console

**Impact estimé : Élevé / Délai : 4-8 semaines**

Les URLs `/produits/guej-beurre.html`, `/produits/guej-kong.html`, etc. ne semblent pas indexées : elles n'apparaissent dans aucun résultat de recherche testé cette semaine, même en recherche `site:seggfaye.com`.

**À faire :**
1. Dans Google Search Console, inspecter les URLs produits clés (guej-beurre, guej-kong, crevettes-sechees, netetu-dom)
2. Demander l'indexation manuelle si elles ne sont pas encore crawlées
3. Vérifier que les pages produits ont bien des titles et meta descriptions uniques (non dupliqués)

---

## 5. Délai estimé pour dépasser maya-boutique.fr

| Segment | Délai estimé | Condition |
|---|---|---|
| Requêtes "guedj" (acheter guedj france, ou acheter guedj) | 1 à 3 mois | Blog déjà présent, fiches produits à indexer |
| Requêtes "netetou acheter" | 3 à 6 mois | Après création article + indexation fiches produits |
| Requêtes "poisson seche senegalais acheter" | 4 à 8 mois | Contenu existant + travail sur l'autorité du domaine |
| Requêtes "produits senegalais en ligne" | 6 à 12 mois | Concurrence plus forte (NKOSI, racines-shop) |
| Requêtes "épicerie africaine en ligne" | 12 à 24 mois | Dominées par des acteurs établis depuis plusieurs années |

**Conclusion :** maya-boutique.fr est déjà dépassable sur les requêtes niches (guedj, produits halieutiques) dans 1 à 3 mois avec les actions ci-dessus. L'indexation de guide.seggfaye.com est la priorité absolue : elle peut doubler notre surface SEO en quelques semaines.

---

*Rapport généré automatiquement le 22/07/2026. Aucune note, étoile, avis ni prix modifié par cet agent.*
