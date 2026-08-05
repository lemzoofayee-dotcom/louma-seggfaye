# Rapport SEO Louma by Seggfaye — Semaine du 4 août 2026

> **AVERTISSEMENT : Positions et indexations = ESTIMATIONS hors GSC, issues de recherches web publiques. À confirmer obligatoirement dans Google Search Console et via l'outil de test des résultats enrichis Google.**

---

## 1. Tableau de positionnement ESTIMÉ (recherches web, hors GSC)

| Mot-clé | seggfaye.com | guide.seggfaye.com | maya-boutique.fr | Leader estimé |
|---|---|---|---|---|
| produits exotiques africains france | non vu | non vu | ~top 2 | europages.fr / maya-boutique.fr |
| produits halieutiques séchés sénégal | non vu | non vu | non vu | espaceagro.com / persee.fr |
| poisson séché sénégalais acheter | non vu | non vu | non vu | espaceagro.com / keryaye.fr |
| guedj acheter france | blog visible (~pos. 4-6) | non vu | non vu | keryaye.fr / issanny.com |
| netetou acheter | non vu | non vu | ~pos. 8 | sunu alimentation / halalfrais.fr |
| epicerie africaine en ligne | non vu | non vu | non vu | nkosi / issanny / racines-shop |
| produits sénégalais en ligne | non vu | non vu | ~pos. 1 | maya-boutique.fr |
| recette thieboudienne ingrédients | blog visible (~pos. 5) | non vu directement | non vu | nkosiagro.com / 196flavors.com |
| crevettes séchées sénégal | non vu | non vu | non vu | exoticasenegal.fr / espaceagro |
| cuisine sénégalaise produits | blog visible (~pos. 4) | non vu | non vu | chefsimon / cuisinemetisse.fr |
| ou acheter du guedj en france | non vu | non vu | non vu | magasin-africain.com / keryaye.fr |
| acheter netetou en ligne | non vu | non vu | ~pos. 7-8 | sunu alimentation / carafrique.fr |

**Lecture rapide :** seggfaye.com est visible uniquement sur les requêtes orientées "guedj" grâce aux articles de blog. Sur les requêtes transactionnelles génériques (épicerie africaine, produits sénégalais, netetou acheter), il n'est pas vu dans mes recherches. À vérifier GSC pour les vraies positions et le volume de clics.

---

## 2. Analyse concurrentielle

### 2.1 maya-boutique.fr (principal concurrent direct)

**Forces détectées :**
- Première position estimée sur "produits sénégalais en ligne" et visible sur "netetou acheter" — forte autorité de domaine sur les termes génériques sénégalais
- Structure WordPress/WooCommerce avec pages catégories indexées (produits-halieutiques, céréales, accessoires, mon-marché), ce qui multiplie les pages d'entrée SEO
- Produits halieutiques (yett/mollusque, feuille de nguer, netetou soumbala) et accessoires présents dans l'index Google
- Page "a-propos" dédiée qui renforce la confiance et l'autorité de marque
- Livraison France + livraison main propre Lyon : cible locale + nationale
- Positionnement différenciant : "mamans entrepreneures" = angle storytelling engageant

**Faiblesses estimées (sans accès direct au site) :**
- Site retourne HTTP 403 à l'exploration automatique — signe possible de protections Cloudflare qui peuvent ralentir l'exploration Googlebot (à surveiller)
- Modèle généraliste (alimentation + ustensiles + décoration + bien-être) vs positionnement expert de seggfaye.com sur les produits halieutiques
- Aucun contenu blog visible dans les résultats de recherche — peu de stratégie contenu / longue traine

**Avantages de seggfaye.com vs maya-boutique.fr :**
- Expertise produit unique : le Guedjologue est une autorité sur les guedj/produits halieutiques, ce qu'aucun concurrent ne peut copier facilement
- Blog actif (~20 articles) sur des requêtes longue traine à fort potentiel (quest-ce-que-le-guedj, acheter-guedj-france, les-7-guedj-du-senegal)
- guide.seggfaye.com = actif SEO unique, avec schema Recipe sur chaque plat (caldou, dibi, mbakhalou saloum, lakh indexés)
- Contenu TikTok @seggfaye = signal de marque et source de backlinks potentiels
- 53 produits spécialisés halieutiques vs gamme généraliste chez maya-boutique

### 2.2 Autres concurrents à surveiller

| Concurrent | Forces | Menace pour Louma |
|---|---|---|
| nkosiagro.com | Fort sur "épicerie africaine", blog actif avec recette thieboudienne | Moyenne (généraliste) |
| racines-shop.com | Gamme très large, visible sur "épicerie africaine" | Faible (pas spécialisé poissons) |
| issanny.com | Visible sur "guedj acheter france" avec une page produit guedj 1kg | Haute (même produit, même marché) |
| keryaye.fr | Visible sur "guedj" et "ou acheter guedj france" | Haute (même niche) |
| exoticasenegal.fr | Visible sur "crevettes séchées sénégal" | Moyenne (produit concurrent) |
| grandexotique.com | Visible sur "guedj acheter france" | Moyenne |

---

## 3. État des rich snippets (estimé, hors GSC)

### 3.1 Schema FAQPage — seggfaye.com (page d'accueil)

**Implémentation :** FAQPage en JSON-LD avec 4 questions (qu'est-ce que le guedj, livraison, conservation, quel guedj choisir). Schéma bien formé, syntaxe correcte.
**Visibilité dans les SERP :** non observée dans mes recherches, mais cela ne prouve pas l'absence — les FAQ rich snippets peuvent être actifs sans apparaître dans des recherches génériques. **À vérifier avec le Rich Results Test Google et dans GSC > Résultats enrichis.**

### 3.2 Schema Recipe — guide.seggfaye.com (pages plats)

**Implémentation :** Recipe JSON-LD complet sur chaque page plat — name, description, image absolue (gestion correcte des URL relatives/absolues), author (Le Guedjologue), publisher, prepTime/cookTime en format ISO 8601, recipeIngredient, recipeInstructions (HowToStep). Schéma solide et éligible aux rich snippets.
**Visibilité dans les SERP :** pages indexées (caldou, dibi, mbakhalou saloum, lakh visibles dans les résultats) mais rich snippets Recipe (temps, portions) non observés. **À vérifier dans GSC > Résultats enrichis > Recettes.**

### 3.3 AggregateRating — seggfaye.com (page d'accueil)

**Situation à signaler (pas corrigé par ce rapport) :** L'aggregateRating (5/5, 8 avis) est implémenté sur le type `Organization`. Google n'affiche généralement pas les étoiles dans les SERP pour ce type — il recommande de placer l'aggregateRating sur `Product`, `LocalBusiness` ou `Recipe`. Le schema Organization n'est probablement pas éligible aux étoiles. Si Lamine souhaite corriger cela, il faudra soit changer le type en `LocalBusiness`, soit ajouter des schemas `Product` individuels sur les pages produits. **Décision de correction à valider par Lamine, pas appliquée automatiquement.**

---

## 4. Trois actions prioritaires pour la semaine

### Action 1 — Dupliquer le modèle blog "guedj" sur "netetou" et "crevettes séchées"
**Impact estimé : Élevé | Délai pour voir résultats : 4-8 semaines**

Le blog article `quest-ce-que-le-guedj.html` est visible dans les résultats Google sur les termes "guedj" — le modèle fonctionne. Ce même modèle (guide complet + FAQ schema + CTA boutique) doit être appliqué à :
- `acheter-netetou-france.html` existe déjà — à vérifier si le schema FAQPage y est implémenté comme dans le blog guedj
- Créer `quest-ce-que-le-netetou.html` (il existe `guide-netetou-soumbala.html` — à évaluer si bien optimisé)
- Créer `crevettes-sechees-saloum.html` — aucun article existant sur ce produit alors qu'il est en vente

Sur "netetou acheter france", seggfaye.com n'est pas vu mais maya-boutique.fr l'est (~pos. 8). L'article blog spécialisé de seggfaye.com a un avantage d'expertise que maya-boutique ne peut pas répliquer.

### Action 2 — Ajouter la page "thiéboudienne" dans guide.seggfaye.com
**Impact estimé : Élevé | Délai pour voir résultats : 6-10 semaines**

"Recette thieboudienne ingredients" est le mot-clé culinaire sénégalais le plus recherché en France. guide.seggfaye.com a des pages pour caldou, dibi, mbakhalou saloum, lakh — mais la thiéboudienne (plat national) n'est pas visible dans les résultats. C'est le plat qui pourrait générer le plus de trafic organique, surtout avec un schema Recipe complet éligible aux rich snippets. La page lierait directement aux produits guedj, netetou, yeet vendus sur seggfaye.com.

### Action 3 — Vérifier et activer les rich snippets via GSC + Rich Results Test
**Impact estimé : Moyen | Délai : immédiat si les schemas sont validés**

Le schema Recipe sur guide.seggfaye.com et le schema FAQPage sur seggfaye.com sont en place mais la visibilité en SERP n'est pas confirmée. Action concrète :
1. Tester chaque URL dans [Rich Results Test Google](https://search.google.com/test/rich-results) pour confirmer l'éligibilité
2. Dans GSC > Résultats enrichis : vérifier les erreurs/avertissements sur Recettes et FAQ
3. Vérifier si une image valide est présente sur chaque page plat du guide (le code prévoit un fallback logo.webp — s'assurer que les plats principaux ont une vraie photo pour maximiser les chances)
4. Pour l'aggregateRating (étoiles) : envisager de changer le type Organization en LocalBusiness dans le schema de seggfaye.com si Lamine souhaite des étoiles dans les SERP

---

## 5. Estimation du délai pour dépasser maya-boutique.fr

| Critère | maya-boutique.fr (estimé) | seggfaye.com aujourd'hui | Délai estimé |
|---|---|---|---|
| Requêtes produits sénégalais génériques | ~pos. 1-3 | non vu | 6-12 mois (si pages catégories créées) |
| Requêtes "guedj / poissons séchés" | non vu | blog pos. 4-6 | Déjà en avance sur cette niche |
| Requêtes "netetou acheter" | ~pos. 7-8 | non vu | 2-4 mois (article optimisé) |
| Contenu blog / longue traine | peu ou pas visible | ~20 articles actifs | Déjà en avance |
| Rich snippets Recipe | non détecté | Schema en place, non activé | 4-8 semaines après activation |

**Scénario réaliste :** Sur la niche spécifique "guedj et poissons séchés sénégalais", seggfaye.com est déjà en avance ou au niveau de maya-boutique.fr grâce au blog. Sur les termes génériques ("produits sénégalais", "épicerie africaine"), maya-boutique.fr bénéficie d'une autorité de domaine plus établie — le rattraper prendra 6 à 12 mois avec une stratégie contenu + pages catégories + liens entrants.

La vraie fenêtre d'opportunité court terme (2-4 mois) : devenir la référence sur "guedj", "netetou", "yeet" et "poissons séchés sénégalais" — une niche que maya-boutique.fr n'occupe pas.

---

*Rapport généré automatiquement le 5 août 2026. Sources : recherches web publiques Google (hors Search Console). Toute position citée est une estimation — la vérité est dans GSC.*
