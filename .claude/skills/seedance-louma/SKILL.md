---
name: seedance-louma
description: "Génération de pubs vidéo IA pour Louma by Seggfaye via Seedance 2.0 (fal.ai). Utiliser quand l'utilisateur demande une pub vidéo, un spot TikTok, un teaser produit, un B-roll, un hook vidéo, ou veut animer une photo produit avec Seedance/fal. Adapté à la marque Louma (gold, marbre noir, mains, golden hour) et aux 5 best-sellers (crevettes Cipakh, yokhos, bissap, netetou, pack Saloum)."
author: Lamine Faye
---

# Seedance pour Louma by Seggfaye

Ce skill génère des prompts et des vidéos Seedance 2.0 (ByteDance, via fal.ai) adaptés à la **marque Louma** et au format **TikTok faceless**.

## Quand l'utiliser
- Animer une photo produit en clip vidéo (image-to-video)
- Créer un hook vidéo 5-8s (mystère/découverte)
- Pubs courtes 10-15s (vente directe)
- B-roll d'ambiance pour habiller le documentaire Saloum
- Storytelling produit (geste culinaire, plateau marbre noir, vapeur)

## Workflow standard
1. **Identifier le besoin** : produit + objectif + format (durée, ratio)
2. **Lire les references/** :
   - `brand-dna.md` — DNA visuel Louma (à respecter à 100%)
   - `products.md` — connaissance des 5 best-sellers
   - `prompt-structure.md` — structure 8 blocs Seedance
   - `templates.md` — 3 templates prêts (faceless_lifestyle, unboxing, mystere)
3. **Rédiger le prompt** selon la structure 8 blocs (100-260 mots)
4. **Présenter le prompt à l'utilisateur** pour validation avant génération
5. **Générer** via `scripts/generate.py` avec FAL_KEY (déjà dans `.env`)
6. **Sauvegarder** le mp4 dans `outputs/` avec auto-versioning v1, v2, v3...

## Paramètres Seedance 2.0 par défaut (Louma)
- Endpoint : `bytedance/seedance-2.0/image-to-video` (i2v) ou `text-to-video` (t2v)
- Aspect ratio : **9:16** (TikTok vertical)
- Resolution : **720p** (suffit pour TikTok, ~30% moins cher que 1080p)
- Duration : **5s** (hook), **10s** (pub courte), **15s** (storytelling)
- Generate audio : **true** (Seedance 2.0 génère audio natif gratuit)
- Coût indicatif : ~$0.30/sec en 720p, ~$1.50 pour 5s, ~$4.50 pour 15s

## Règles strictes (à suivre toujours)

**Mots interdits dans les prompts** (tendent à dégrader la qualité Seedance) :
- ❌ "cinematic", "professional", "stunning", "beautiful", "amazing"
- ✅ Décrire concrètement : "low angle 30°", "warm golden side light", "shallow depth of field"

**Toujours inclure** dans le prompt final :
- `No on-screen text, no captions, no subtitles.`
- `Hands only, no face visible.` (Lamine est faceless creator)

**Personnages** :
- Couvrir la peau (manches longues, pas de peau exposée → modération Seedance refuse)
- Ex : "olive skin hands with delicate gold rings, long-sleeve cream linen shirt"

**Couleurs Louma** (palette à utiliser) :
- Or doré (#D4AF37) — touches lumineuses
- Noir profond (marbre, plateau, fond)
- Crème ivoire (papier kraft, lin naturel)
- Vert mangrove (rappels Saloum)
- Pas de couleurs criardes (rouge vif, bleu électrique → off-brand)

**Lumière Louma** (signature) :
- Golden hour latérale (45° latérale, depuis la droite)
- Backlight subtle (halo doré sur le sujet)
- Marbre noir = surface principale (réflexions douces)
- Jamais de néon, fluo, plein soleil dur

## Structure de prompt (8 blocs — toujours dans cet ordre)

```
1. DURATION + ASPECT + SETTING + LIGHTING
   "5s, 9:16 vertical, dark slate marble surface, golden hour side light from right at 45°"

2. CHARACTER (si présent)
   "dark-skinned hands of a Senegalese man, deep brown West African complexion, two thin gold rings, long-sleeve cream linen shirt cuffs visible"

3. CAMERA SETUP
   "macro lens 100mm, shallow depth of field f/2.8, locked tripod, eye-level slightly downward"

4. SCENE / PRODUCT (avec image refs)
   "@(product) sitting centered on marble. Steam slowly rises. Linen cloth corner visible top-left."

5. BEAT-BY-BEAT TIMELINE
   "0-2s: hand enters from right, fingertips first. 2-4s: gently lifts product. 4-5s: holds product close to camera, slight rotation."

6. TONE / MOOD
   "intimate, reverent, slow-motion, ASMR feel"

7. CAMERA MOVEMENT / GRAIN / STYLE
   "subtle slow push-in 5%, fine 35mm grain, warm 4500K color grade, shallow vignette"

8. CLOSING EMOTIONAL LINE
   "the kind of moment that makes you remember your grandmother's kitchen"

Constraints: No on-screen text, no captions, no subtitles. Hands only, no face visible.
```

## Templates prêts à l'emploi
Voir `references/templates.md` pour 3 templates testés :
- **Faceless Lifestyle** (mains qui touchent, gestes culinaires)
- **Product Reveal** (hook mystère 5s, ouverture pack Saloum)
- **Saloum B-Roll** (paysages mangrove, eau, golden hour)

## Quand demander à l'utilisateur (toujours avant de générer)
1. Quel produit ? (Crevettes Cipakh / Yokhos / Bissap / Netetou / Pack Saloum / Guedj X)
2. Quelle photo de référence ? (chemin local ou URL)
3. Quel objectif ? (hook 5s / pub 10-15s / B-roll d'ambiance)
4. Quel template appliquer ? (Faceless Lifestyle / Reveal / B-Roll / Custom)

Une fois validé → écrire le prompt complet, le **montrer à l'utilisateur** avant exécution, attendre l'OK explicite ("go", "lance", "ok").

## Coûts à signaler avant chaque génération
Toujours dire à l'utilisateur le coût estimé AVANT de lancer :
- 5s en 720p ≈ $1,50
- 10s en 720p ≈ $3,00
- 15s en 720p ≈ $4,50
- 5s en 1080p ≈ $2,40
- 10s en 1080p ≈ $4,80

## Ressources
- API doc : https://fal.ai/models/bytedance/seedance-2.0/image-to-video/api
- Pricing : https://www.atlascloud.ai/blog/case-studies/seedance-2.0-pricing-full-cost-breakdown-2026
- Repo source d'inspiration : https://github.com/jasonlee-breadcrumb/claude-arcads
