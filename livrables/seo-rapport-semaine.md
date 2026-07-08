# Rapport SEO — Semaine du 8 juillet 2026

**Sites analysés :** seggfaye.com · guide.seggfaye.com  
**Concurrent principal :** maya-boutique.fr  
**Autres concurrents surveillés :** racines-shop.com · enviesdafrique.fr · issanny.com · nkosiagro.com

---

## 1. Tableau de positionnement

| Mot-clé | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader actuel |
|---|---|---|---|---|
| produits exotiques africains france | absent | absent | absent | magasin-stalingrad.com / racines-shop.com |
| produits halieutiques seches senegal | absent (page existe) | absent | catégorie indexée | maya-boutique.fr |
| poisson seche senegalais acheter | absent | absent | absent | issanny.com / afroleck.com |
| guedj acheter france | absent (blog existe) | absent | absent | magasin-africain.com / issanny.com |
| netetou acheter | absent | absent | absent | sunualimentation.com / nkosiagro.com / Amazon |
| epicerie africaine en ligne | absent | absent | absent | kissafrica.fr / issanny.com / racines-shop.com |
| produits senegalais en ligne | absent | absent | cité dans résultats | issanny.com / sunualimentation.com |
| recette thieboudienne ingredients | absent (blog existe) | absent | absent | nkosiagro.com / mesepices.com |
| crevettes sechees senegal | absent (produit existe) | absent | absent | exoticasenegal.fr / timifood.com |
| cuisine senegalaise produits | absent | absent | absent | nkosiagro.com / racines-shop.com |
| ou acheter du guedj en france | absent (page exacte existe) | absent | absent | magasin-africain.com / sunulek.com / afroleck.com |
| acheter netetou en ligne | absent | absent | absent | sunualimentation.com / nkosi / Amazon |

**Constat choc :** seggfaye.com a 90 URLs dans son sitemap (26 articles de blog + 54 pages produits + pages catégories) mais Google n'indexe que 2 pages. guide.seggfaye.com a 0 page indexée.

---

## 2. Analyse concurrentielle

### maya-boutique.fr

**Forces :**
- WooCommerce sur WordPress : indexation automatique fiable, URLs propres
- Présence physique à Lyon (7 rue de Marseille, Lyon 7) : renforce la confiance Google + Local SEO
- Référencement Pages Jaunes et presse locale
- Catégories produits halieutiques indexées (yett, guedj beurre, touffeu, kong fumé, kéthiakh)
- Fondée par Ndeye : histoire et brand story visible sur la page "À propos"
- Réseau solidaire avec entrepreneures africaines = contenu éditorial crédible

**Faiblesses :**
- Aucun avis clients sur les produits halieutiques (0 reviews affichées)
- Pas de blog ou contenu éditorial visible sur les keywords d'intention (recettes, guides)
- Pas d'autorité spécialisée sur le guedj (nous sommes les seuls "Guedjologue")
- Gamme halieutique limitée vs notre spécialisation : 5-6 produits vs nos 7 variétés de guedj + mollusques

**Ce qu'ils font mieux que nous :**
- Être indexés (WooCommerce facilite le crawl Google par défaut)
- Présence physique qui génère des backlinks locaux naturels (presse, annuaires)

### Autres concurrents à surveiller

| Concurrent | Point fort | Menace pour nous |
|---|---|---|
| issanny.com | Livraison monde entier, guedj bien référencé | Fort sur "guedj acheter france" |
| sunualimentation.com | Référence nététou, produits sénégalais | Fort sur netetou |
| nkosiagro.com | Content marketing (blog recettes, soumbala guide) | Gagne sur "recette thieboudienne" |
| racines-shop.com | Très large catalogue, autorité de domaine élevée | Généraliste difficile à battre |
| magasin-africain.com | Guedj poisson fermenté bien positionné | Concurrent direct sur guedj |
| exoticasenegal.fr | Crevettes séchées, produits halieutiques | Concurrent sur notre spécialité |

**Notre avantage différentiel non exploité :** Personne d'autre n'est "Guedjologue". L'encyclopédie des 7 guedj du Sénégal, les recettes authentiques des Îles du Saloum, l'expertise terrain — c'est unique. Ce contenu existe (blog, guide) mais est invisible car non indexé.

---

## 3. État des rich snippets

### seggfaye.com
Le schema markup est de bonne qualité et bien structuré :
- **Recettes** : Schema `Recipe` complet (HowToStep, NutritionInformation, VideoObject, author) sur les pages recettes. Bon.
- **FAQ** : Schema `FAQPage` présent sur pages blog et pages "acheter guedj". Bon.
- **Produits** : Schema `Product` avec `Offer`, `BreadcrumbList`, `VideoObject` sur toutes les fiches produits. Bon.
- **Articles** : Schema `Article` avec `Person` (author) et `Organization`. Bon.
- **Organisation** : Schema `Organization` sur la homepage avec `founder`, `sameAs` (TikTok, YouTube, guide.seggfaye.com). Bon.

**Problème critique :** Ces schemas sont invisibles à Google car les pages ne sont pas indexées. Un schema parfait sur une page non crawlée = zéro rich snippet. La priorité n'est pas d'améliorer les schemas, c'est de résoudre l'indexation.

**Point de vigilance (hors périmètre SEO) :** L'`Organization` sur la homepage contient `sameAs` vers guide.seggfaye.com. Aucun `aggregateRating` n'est présent, c'est correct. Ne pas toucher aux données d'avis.

### guide.seggfaye.com
- Site Next.js 16.2.6 (avec Supabase)
- Zéro page indexée dans Google
- Risque fort de rendu côté client (CSR) : si les pages sont rendues en JavaScript, Google Googlebot peut ne pas les crawler/indexer. Next.js en mode CSR = invisible pour Google.
- Aucun rich snippet possible tant que le site n'est pas indexé

### maya-boutique.fr
- WooCommerce génère automatiquement des schemas Product de base
- Recherche indique 0 avis clients sur les produits halieutiques : pas de rich snippets étoiles visibles pour ces produits
- Pas de schemas Recipe ou FAQ détectés

---

## 4. Actions prioritaires

### Action 1 — Résoudre l'indexation de seggfaye.com (impact : critique, délai : 2-4 semaines)

C'est l'urgence absolue. 90 pages en sitemap, 2 indexées = problème structurel.

**Diagnostic :** robots.txt est correct (Allow: /, sitemap déclaré). Le problème vient probablement de :
- Autorité de domaine trop faible (site récent, peu de backlinks) : Google crawle mais ne juge pas les pages dignes d'indexation
- Possibles erreurs dans Google Search Console (crawl budget épuisé, pages marquées "discovered but not indexed")

**Actions à faire maintenant :**
1. Vérifier Google Search Console > Indexation > Pages : identifier les erreurs (discovered not indexed, soft 404, duplicate content)
2. Soumettre manuellement les 10 pages prioritaires via "URL Inspection > Demander l'indexation" dans GSC : commencer par `epicerie-africaine.html`, `blog/acheter-guedj-france.html`, `blog/les-7-guedj-du-senegal.html`, `produits/guej-yass.html`, `blog/produits-senegalais-france.html`
3. Vérifier que les Core Web Vitals sont acceptables (PageSpeed Insights sur les pages principales)
4. Créer 2-3 backlinks depuis des sources fiables : un article chez un blogueur cuisine africaine, une mention sur un forum diaspora sénégalaise, un partage TikTok qui renvoie vers une page précise

### Action 2 — Corriger guide.seggfaye.com pour le rendu côté serveur (impact : fort, délai : 1 semaine)

Le guide est un contenu à fort potentiel SEO (recettes + guides encyclopédiques) mais il est entièrement invisible.

**Diagnostic probable :** Next.js en mode CSR (pas de SSR/SSG). Google ne voit que du JavaScript vide.

**Actions :**
1. Vérifier dans next.config.ts si les pages utilisent `generateStaticParams` ou `getServerSideProps` / Server Components
2. S'assurer que toutes les pages de recettes utilisent les Server Components (App Router de Next.js 16) ou `export const dynamic = 'force-static'`
3. Ajouter un sitemap.xml pour guide.seggfaye.com et le soumettre dans GSC
4. Vérifier avec l'outil "Test de résultats enrichis" de Google sur une URL du guide

### Action 3 — Acquérir les premiers backlinks thématiques (impact : fort sur l'autorité, délai : 4-8 semaines)

Sans backlinks, Google ne fait pas confiance au domaine et limite l'indexation. C'est la cause racine.

**Actions concrètes et gratuites :**
1. Publier un article "encyclopédie du guedj" sur un blog cuisine africaine partenaire avec lien retour vers `seggfaye.com/blog/les-7-guedj-du-senegal.html`
2. Répondre sur des forums diaspora (Facebook groupes "Sénégalais en France", "Cuisine sénégalaise Europe") avec des liens naturels vers les guides
3. Contacter nkosiagro.com pour un échange de liens éditoriaux (ils font du contenu, nous avons l'expertise guedj qu'ils n'ont pas)
4. Créer une fiche Google Business Profile pour Louma by Seggfaye (même sans local physique, cela génère un backlink depuis Google et renforce la confiance)
5. Soumettre l'URL sur des annuaires épiceries africaines (issanny.com a une page partenaires, racines-shop aussi)

---

## 5. Estimation pour dépasser maya-boutique.fr

| Horizon | Réalisme | Condition |
|---|---|---|
| Sur mots-clés spécialisés guedj ("guedj yass", "7 guedj senegal", "ou acheter guedj france") | **2-4 mois** | Indexation résolue + 5-10 backlinks thématiques |
| Sur mots-clés intermédiaires ("poisson seche senegalais", "produits halieutiques senegal") | **4-6 mois** | Idem + content cluster bien lié |
| Sur "epicerie africaine en ligne" et keywords généraux | **12-18 mois** | Nécessite autorité de domaine solide + backlinks en nombre |
| Sur "netetou acheter" | **3-5 mois** | Guide netetou existant + page catégorie epices renforcée |

**Avantage décisif :** maya-boutique.fr n'a pas d'autorité éditoriale sur le guedj ou la gastronomie du Saloum. Leur contenu est purement e-commerce. Dès que nos pages seront indexées, nous dominerons les keywords informationnels à forte intention (guides, recettes, explications) qui génèrent du trafic qualifié et des conversions. Le problème n'est pas la qualité du contenu, c'est la visibilité.

---

*Rapport généré par l'agent SEO Louma le 8 juillet 2026*  
*Méthode : recherches Google manuelles + analyse code source + analyse sitemap*
