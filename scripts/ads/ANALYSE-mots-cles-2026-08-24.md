# Analyse mots-clés Google Ads — Lundi 24/08/2026

> **Données FRAÎCHES** — étude relancée en local le 24/08 (auth OAuth régénérée le jour même).
> Source : Google Ads Keyword Planner, géo **France**, langue FR. 60 mots-clés uniques.
> Comparaison avec le snapshot du **05/08/2026** (`mots_cles_resultats_v2_snapshot_2026-08-05.csv`).
> ⚠️ Ce sont des volumes **Keyword Planner** (recherche Google Ads), pas des données Search Console.

---

## 1. Mouvements notables depuis le 05/08

| Mot-clé | Volume | Évolution | Lecture |
|---------|--------|-----------|---------|
| **bissap blanc** | 1 600/mois | concurrence **HIGH → MEDIUM** ⬇️ | La barrière baisse sur un gros volume → fenêtre de tir |
| **bouye** | 1 300/mois (LOW) | CPC **0 € → 0,23-0,70 €** ⬆️ | Intérêt commercial qui monte sur le fruit du baobab |
| **soupou kandja** | 720 → **590** (−18 %) | recul | Demande saisonnière en baisse |
| **poisson kong** | 320 → **260** (−19 %) | recul | Volume qui s'effrite |
| **kethiakh** | 50 → **70** (+40 %) | hausse | Petit signal sur le poisson braisé-séché |
| **yoxos** | concurrence définie **LOW** | donnée stabilisée | Ton produit (yokhos) — volume encore faible |

Le socle haute-valeur reste stable : **guedj (6 600)**, **néré (6 600)**, **cymbium (5 400)**, tous en concurrence LOW et déjà couverts par des articles.

---

## 2. Trous prioritaires (volume + concurrence faible + PAS de page dédiée)

Vérifié par `grep` sur `blog/*.html` — ces termes ne sont PAS déjà traités par une page dédiée (au mieux cités en passant).

### 🥇 Priorité 1 — Recette « jus de bouye »
- **Volumes** : bouye 1 300/mois + jus de bouye 880/mois, concurrence **LOW**.
- **État** : seul l'explicatif `pain-de-singe-bouye-baobab.html` existe (le fruit), **aucune page recette**.
- **Pourquoi maintenant** : symétrie avec `recette-jus-de-bissap.html` qui existe déjà → même intention "recette/jus". Le CPC du bouye vient d'apparaître (intérêt marchand ↑).
- **Action** : article `recette-jus-de-bouye.html` (recette + bienfaits + lien produit poudre de baobab/bouye).

### 🥈 Priorité 2 — Page « bissap blanc »
- **Volume** : 1 600/mois, concurrence **MEDIUM** (vient de baisser depuis HIGH).
- **État** : « bissap blanc » est cité dans plusieurs pages mais **aucune ne le cible** en propre (le guide vise l'hibiscus rouge / général).
- **Action** : page ou gros bloc dédié `bissap blanc` (différence rouge/blanc, goût plus doux, usage) — capte un terme gros volume dont la concurrence se dégonfle.

### 🥉 Priorité 3 — « jus de tamarin / dakhar »
- **Volume** : tamarin jus 320/mois, concurrence **MEDIUM**. Couverture actuelle ≈ **nulle** (1 mention dans l'article thieboudienne).
- **Atout** : s'appuie sur ton savoir **ndiambane / dakhar** (déjà en mémoire) → autorité naturelle, nouveau point d'entrée de cluster.
- **Action** : article `jus-de-tamarin-dakhar-senegal.html` (jus + condiment ndiambane).

### Priorité 4 (bonus autorité) — « poisson kong »
- **Volume** : 260/mois (LOW), + kong fumé 70 + guedj kong 20. **Aucune page dédiée** (« kong » n'apparaît que dans les articles guedj génériques).
- **Atout** : 100 % domaine Guedjologue → article court, gain d'autorité facile.

---

## 3. Ce qui est DÉJÀ bien couvert (ne rien recréer)

guedj (7+ articles), néré, netetou/soumbala/dawadawa, cymbium/yeet, pain de singe/baobab, bissap (guide + recette jus), ditakh, thiébou yapp, domoda, soupou kandja, mbakhalou saloum, caldou, crevettes séchées, niébé, kinkeliba, fonio, fondé/araw, lakh, thiakry/dégué, thiéré + tous les grands plats (mafé, yassa, thieboudienne…).

**oseille de guinée** (390) = synonyme de bissap → déjà traité par `bissap-hibiscus-guide.html`. Ne pas dupliquer.

---

## 4. Rappel process

⚠️ **3 PR Ads précédentes encore ouvertes, jamais mergées** : #11 (17/08), #9 (10/08), #3 (03/08). Elles tournaient toutes sur le CSV du 05/08 (mêmes chiffres). **Décision à prendre** : merger celle qui a de la valeur / fermer les redondantes, pour ne pas accumuler.

**Pour garder des chiffres frais chaque semaine** : le refresh token Google expire à 7 jours (app en mode « test »). Fix durable = passer l'écran de consentement OAuth de *Testing* à *In production* dans Google Cloud Console.
