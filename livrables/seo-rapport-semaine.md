# Rapport SEO Louma by Seggfaye — Semaine du 15 juillet 2026

> Périmètre : seggfaye.com + guide.seggfaye.com  
> Concurrent de référence : maya-boutique.fr  
> Note : résultats de recherche issus de Google.com (US). Les positions France peuvent varier légèrement mais reflètent les tendances générales.

---

## 1. Tableau de positionnement

| Mot-clé | Volume est. | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader actuel |
|---------|-------------|--------------|-------------------|-----------------|--------------|
| produits exotiques africains france | ~3 000/mois | **Absent** | Absent | Absent | europages.fr / exotiquepro.fr |
| produits halieutiques séchés sénégal | ~500/mois | **Absent** | Absent | Absent | espaceagro.com |
| poisson seche senegalais acheter france | ~600/mois | **P.1-3 (blog)** | Absent | Absent | espaceagro.com / issanny.com |
| guedj acheter france | ~900/mois | **Absent** | Absent | **Présent (cat. halieutiques)** | magasin-africain.com / grand-exotique.com |
| netetou acheter france | ~800/mois | **Absent** | Absent | **Présent (fiche produit)** | miamland.com / tamexotique.com / Amazon |
| epicerie africaine en ligne | ~5 000/mois | **Absent** | Absent | Absent | racines-shop.com / issanny.com / nkosiagro.com |
| produits senegalais en ligne | ~1 200/mois | **Absent** | Absent | Absent | sunualimentation.com / niokobok.com |
| recette thieboudienne ingredients | ~2 000/mois | **Absent** | Absent | Absent | inspifoodbykinouche.com |
| crevettes sechees senegal acheter france | ~400/mois | **Absent** | Absent | Absent | espaceagro.com / magasin-africain.fr |
| ou acheter du guedj en france | ~600/mois | **Absent** | Absent | Absent | grand-exotique.com / magasin-africain.com |
| acheter netetou en ligne france | ~700/mois | **Absent** | Absent | Absent | miamland.com / Amazon |
| cuisine senegalaise produits | ~1 500/mois | **Absent** | Absent | Absent | nkosiagro.com / cuisinemetisse.fr |

**Résumé positionnement :**
- seggfaye.com est indexé par Google sur 3 articles de blog (`quest-ce-que-le-guedj.html`, `recette-basse-salte.html`, `recette-jus-de-bissap.html`). L'article guedj apparaît sur des requêtes informationnelles type "poisson seche senegalais" mais pas sur les requêtes transactionnelles à fort intent d'achat.
- guide.seggfaye.com : **zéro page indexée** (vérification `site:guide.seggfaye.com` = 0 résultat). Le guide n'existe pas pour Google.
- maya-boutique.fr est positionné sur les requêtes transactionnelles clés (guedj, netetou) via ses fiches produits WooCommerce.

---

## 2. Analyse concurrentielle

### maya-boutique.fr (concurrent principal)

**Ce qu'ils font mieux que nous :**
- Fiches produits dédiées avec URL propres : `/product/guedj-beurre`, `/produit/netetou-soumbala`
- Schema `Product` automatique via WooCommerce (permet les rich snippets prix en SERP)
- Catalogue couvrant la totalité des halieutiques sénégalais : guedj beurre, yett, pagne, kethiakh, kong fumé, netetou, touffeu, mollusques
- Indexation WordPress solide, domaine plus ancien
- Présents sur les requêtes transactionnelles à fort intent d'achat

**Nos avantages sur eux :**
- Contenu éditorial de qualité (articles blog seggfaye.com indexés, expertise "Guedjologue" unique)
- Storytelling différenciant : traçabilité directe des Îles du Saloum, sans intermédiaire
- 3 articles déjà indexés (maya-boutique.fr semble avoir peu de contenu éditorial)
- Identité créatrice forte (TikTok @seggfaye, communauté engagée)
- Schema FAQPage et Recipe implémentés (avantage rich snippets éditorial)

### racines-shop.com

- Concurrent établi depuis 30+ ans. Très large gamme (Afrique + Océan Indien + Madagascar)
- Forte autorité de domaine, section recettes, section ingrédients
- Ciblage généraliste, pas la même niche que seggfaye (pas de spécialité guedj/terroir saloum)
- Quasi impossible à dépasser sur "épicerie africaine en ligne" à court terme

### enviesdafrique.fr

- Marketplace généraliste africain (poisson capitaine en 5 kg, positionnement grossiste)
- Peu de contenu éditorial visible
- Moins dangereux que maya-boutique sur notre niche

### Autres acteurs visibles

`issanny.com`, `grand-exotique.com`, `magasin-africain.com` : e-shops généralistes bien positionnés sur guedj et netetou, sans expertise ni storytelling Saloum.

---

## 3. État des rich snippets

| Élément | Statut | Commentaire |
|---------|--------|-------------|
| FAQPage (seggfaye.com index) | ✅ Implémenté | 3+ questions, markup valide. Apparition SERP à confirmer via Search Console |
| Recipe schema (articles blog) | ✅ Implémenté | caldou + autres. HowToStep + NutritionInformation présents |
| VideoObject (yeet-maggi et autres) | ✅ Implémenté | Miniatures hébergées, vidéo TikTok intégrée |
| guide.seggfaye.com (Next.js) | ❌ Non indexé | Zéro page visible dans Google. Robots.ts et sitemap.ts configurés mais guide non indexé |
| aggregateRating | ⚠️ À SIGNALER | Voir section critique ci-dessous |

### ALERTE aggregateRating — À traiter manuellement par Lamine

**Problème détecté (signalement uniquement, pas de correction par l'agent SEO) :**

L'`aggregateRating` est actuellement placé dans le bloc `@type: "Organization"` du schema JSON-LD de l'index.html (lignes 66-72) avec les valeurs suivantes :

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "5",
  "reviewCount": "8",
  "bestRating": "5",
  "worstRating": "5"
}
```

**Pourquoi c'est un risque :**
1. Google ne génère **pas** de rich snippets étoiles pour le type `Organization`. Ce markup est ignoré pour les étoiles en SERP.
2. `worstRating: "5"` est identique à `bestRating: "5"` : cela indique que toutes les notes sont 5/5, ce qui peut être lu comme une anomalie par les algorithmes de qualité.
3. Si Google décide de lire ce bloc (possible avec GEO/AI Overview), un score 5/5 avec seulement 8 avis sur une marque e-commerce peut signaler un contenu peu fiable.

**Ce que Lamine doit décider :** soit supprimer ce bloc, soit le déplacer sur un type compatible (`LocalBusiness`, `Store`) avec des valeurs cohérentes et des vrais avis publics affichés sur la page. Cette décision lui appartient.

---

## 4. Actions prioritaires cette semaine

### Action 1 — Indexer guide.seggfaye.com (URGENT, impact fort)

**Problème :** guide.seggfaye.com n'a aucune page indexée dans Google. L'ensemble du guide (pages plats, pages produits, recherche) n'existe pas pour les moteurs.

**Causes possibles à vérifier :**
- Le build Vercel est-il déployé sur le bon domaine (`guide.seggfaye.com`) ?
- Vérifier dans Google Search Console si le site est soumis
- Vérifier que `robots.txt` de guide.seggfaye.com n'est pas en `Disallow: /`
- Soumettre manuellement le sitemap `https://guide.seggfaye.com/sitemap.xml` dans Search Console

**Impact estimé :** Fort. Des dizaines de pages produits et plats pourraient cibler des mots-clés longue traîne à fort potentiel (thiéboudienne guedj, caldou netetou, etc.).

**Délai d'indexation après correction :** 2 à 6 semaines pour les premières pages.

### Action 2 — Créer une landing page "Guedj acheter France" (impact moyen-fort, 4-8 semaines)

**Problème :** Aucune page produit transactionnelle de seggfaye.com n'est indexée. Maya-boutique et d'autres sont positionnés sur "guedj acheter france" avec de simples fiches WooCommerce.

**Recommandation :** Optimiser la page `/blog/acheter-guedj-france.html` existante (déjà dans le codebase) avec :
- Title tag : "Acheter du guedj en France — Livraison 48h | Louma by Seggfaye"
- H1 ciblant "acheter guedj france"
- Intégration d'un bloc produit avec CTA WhatsApp/commande directe
- Schema `Product` ou `ItemList` sur la page
- Maillage interne depuis l'article "quest-ce-que-le-guedj.html" (déjà indexé)

**Impact estimé :** Moyen à fort. La page existe déjà, c'est surtout une affaire d'optimisation title/H1/CTA + maillage.

### Action 3 — Maillage interne et longue traîne : netetou (impact moyen, 6-10 semaines)

**Problème :** seggfaye.com est absent de toutes les requêtes netetou alors que le produit est en catalogue.

**Recommandation :** Vérifier que la page `/blog/guide-netetou-soumbala.html` (existante) est :
- Accessible via le menu ou le footer (crawlable)
- Optimisée avec title "Acheter netetou en ligne France" ou "Netetou soumbala : guide + achat"
- Liée depuis l'article guedj déjà indexé ("voir aussi : netetou, l'autre condiment essentiel")

En parallèle : créer un maillage systématique blog-vers-boutique pour tous les produits en catalogue.

---

## 5. Estimation délai pour dépasser maya-boutique.fr

| Requête | Délai estimé | Condition |
|---------|-------------|-----------|
| guedj acheter france | 4 à 8 mois | Si landing page optimisée + backlinks blog internes |
| netetou acheter france | 6 à 10 mois | Si guide.seggfaye.com indexé + landing page netetou |
| poisson seche senegalais | 1 à 3 mois | Article déjà indexé, optimisation title suffit |
| epicerie africaine en ligne | 12 à 24 mois | Domaine très concurrentiel, hors portée immédiate |
| guide.seggfaye.com (pages plats/produits) | 2 à 4 mois après indexation | Si indexation corrigée rapidement |

**Conclusion globale :** maya-boutique.fr est vulnérable sur le contenu (peu d'éditorial) et le storytelling (généraliste). Sur les requêtes transactionnelles guedj/netetou, un délai de 6 à 9 mois est réaliste si les trois actions ci-dessus sont menées. Le levier le plus rapide reste l'indexation de guide.seggfaye.com, qui peut doubler le nombre de pages en lice en quelques semaines.

---

*Généré automatiquement le 15 juillet 2026 par l'agent SEO Yolélé.*  
*Source des positions : Google Search (US, indicatif France). Confirmer les positions réelles via Google Search Console.*
