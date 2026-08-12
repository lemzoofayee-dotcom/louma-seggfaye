# Projet : Louma by Seggfaye (mes sites web)

Marché africain en ligne + contenu TikTok @seggfaye (Guedjologue).
Comportement général : voir `~/.claude/CLAUDE.md`. Contexte détaillé : `memory/MEMORY.md`.
Ce fichier ne liste que les règles **spécifiques au projet** à ne jamais rater.

## Contraintes dures (vérifier à chaque fois)
- **Déploiement Vercel** : avant chaque push, vérifier les extensions images `.JPG/.PNG` → `.jpg/.png`
  (Linux est sensible à la casse, un build casse sinon).
- **Noms de plats sénégalais** : toujours demander avant d'écrire un nom (ex : « thieb », pas « thiébou » seul).
  Ne jamais inventer une graphie.
- **« Îles du Saloum »** (terme UNESCO exact), jamais « Saloum » seul. Hashtag prioritaire : #IlesDuSaloum.

## Contenu TikTok
- **Caption + hashtags livrés ensemble**, jamais l'un sans l'autre.
- Checklist Videlyze obligatoire par vidéo : hook choc à 0:00, cut /2s, voix off propre, ASMR, CTA avant 45s.
- Durées : documentaires / découverte = **60s+** (Creator Rewards) ; spots promo = 15-30s.
- Formats gagnants : mystère/découverte, documentaire savoir-faire. Éviter les spots de vente directs.
- Remotion = **overlays uniquement** sur de vraies vidéos (max ~30% du temps), jamais une vidéo 100% Remotion.

## Outils & comptes
- Emails : `seggfaye@gmail.com` = boutique (Brevo/Formspree) · `lemzoofayee@gmail.com` = GitHub.
- i10X = annulé, ne plus utiliser. Privilégier outils en place ou solutions gratuites.
- Skills custom dispo : `louma-content`, `hook-rescue`, `fiche-produit-louma`, `capcut-assets`, `louma-seo`, `seedance-louma`.

## Routine SEO hebdo (cloud) — garde-fous
- La routine cloud n'a **PAS accès à Google Search Console** → elle ne DOIT **jamais** présenter des
  positions / impressions / CTR **estimés** comme des faits. Les vrais chiffres viennent **uniquement**
  de `scripts/seo/gsc-data.md` (généré en LOCAL par `scripts/seo/gsc_pull.py` ; gitignoré car repo public).
- Rôle de la routine cloud = **idées de contenu uniquement**.
- **Avant** de proposer de « créer » une page/article : vérifier qu'elle n'existe pas déjà
  (sitemaps `seggfaye.com` + `guide.seggfaye.com`, dossier `blog/`). Elle a déjà proposé des pages existantes.
- L'analyse chiffrée de positionnement se fait **en local** (session Claude sur `gsc-data.md`).

## Source de vérité contenu
- Produits poissons / guedj : `memory/reference_guedjologue.md` (encyclopédie de Lamine).
- État du projet, stack, priorités : `memory/project_louma.md`.
