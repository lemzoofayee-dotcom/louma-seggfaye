# Templates Seedance Prêts à l'Emploi — Louma

3 templates testés et adaptés à la marque. Copier, adapter le produit, lancer.

---

## TEMPLATE 1 — Faceless Lifestyle (mains qui touchent)

**Quand l'utiliser** : pub courte 5-10s qui montre un produit manipulé par des mains. Format signature de Lamine. Idéal pour TikTok hook ou storytelling produit.

**Cas d'usage** :
- Mains qui versent des crevettes Cipakh dans un bol
- Mains qui ouvrent un sachet vacuum de Netetou
- Mains qui prennent une pincée de bissap

### Prompt template (à personnaliser)

```
10 seconds, 9:16 vertical, dark slate marble surface with subtle natural veining,
warm golden side light from right at 45°, color temperature 4500K, soft halo on subject edge.

Dark-skinned hands of a Senegalese man in his mid-40s, deep brown West African complexion, warm rich umber tone, two thin gold rings on right hand,
long-sleeve cream linen shirt with cuffs visible, gentle confident gestures.

Macro lens 100mm, shallow depth of field f/2.8,
camera at eye level slightly downward 15°, locked tripod feel.

@(product) sitting centered on the marble surface.
Cream linen cloth corner visible top-left of frame.

Beats:
0-2s: empty marble, light gradient softly shifts. Then hand enters from right.
2-5s: fingertips touch the product, slowly cup it into the palm.
5-8s: hand lifts the product close to camera, gently rotates it once.
8-10s: hand lowers product back to marble. Hand exits frame to the right.

Tone: intimate, reverent, slow-motion feel.

Style: subtle slow push-in dolly 5%, fine 35mm film grain,
warm 4500K color grade with golden highlights, gentle vignette, no lens flare.

Subtle ambient sound of soft handling and quiet breathing, no music.

The kind of moment that makes you remember your grandmother's kitchen.

No on-screen text, no captions, no subtitles, no logos.
Hands only, no face visible.
```

**Paramètres fal.ai** :
- Endpoint : `bytedance/seedance-2.0/image-to-video`
- duration: 10
- aspect_ratio: "9:16"
- resolution: "720p"
- generate_audio: true
- image_url: URL de la photo produit Louma (ex : crevettes-saloum-1.jpg uploadée)

**Coût estimé** : ~$3,00

---

## TEMPLATE 2 — Product Reveal (hook mystère 5s)

**Quand l'utiliser** : hook ultra-court 5s pour ouvrir une vidéo TikTok éducative ou pour les pubs hook+CTA. Construit pour intriguer.

**Cas d'usage** :
- Pack Saloum qui s'ouvre lentement
- Cloth qui se soulève pour révéler 7 guedj alignés
- Vacuum pouch qui se déchire et libère le produit

### Prompt template

```
5 seconds, 9:16 vertical, dark slate marble surface,
low key lighting with strong golden backlight from behind subject,
subject in semi-silhouette, rim light tracing the contours, deep shadows.

Dark-skinned hands of a Senegalese man in his mid-40s, deep brown West African complexion, warm rich umber tone, two thin gold rings,
long-sleeve cream linen shirt cuffs visible.

Macro lens 50mm, very shallow depth of field f/1.8,
camera at low angle 30° looking up at subject, locked tripod.

@(product_or_box) centered, partially veiled by a folded cream linen cloth.
Background fades to deep black.

Beats:
0-1s: cloth covers everything. Light shifts subtly.
1-3s: hand enters slowly from below, grabs the corner of the cloth.
3-4s: cloth slowly lifts upward in slow-motion, revealing the product underneath.
4-5s: full reveal, golden light catches the product, hand exits frame.

Tone: contemplative, ancestral, soulful feel.

Style: slow push-in 8%, heavier 16mm grain, warmer 4000K color grade,
slight vignette, golden highlights blooming softly.

Subtle ambient sound of fabric sliding and soft breath, no music.

What your mother brought back from her last trip home, wrapped in linen.

No on-screen text, no captions, no subtitles, no logos.
Hands only, no face visible.
```

**Paramètres fal.ai** :
- duration: 5
- aspect_ratio: "9:16"
- resolution: "720p"
- generate_audio: true

**Coût estimé** : ~$1,50

---

## TEMPLATE 3 — Saloum B-Roll (paysage / origine)

**Quand l'utiliser** : B-roll pour habiller le documentaire Saloum, raconter l'origine, ou faire un transition cinématographique. Pas de produit visible — juste paysage et ambiance.

**Cas d'usage** :
- Mangrove à marée basse, golden hour
- Pirogue traditionnelle qui glisse sur l'eau
- Femme qui sèche du poisson (silhouette de loin)
- Mains qui plongent dans l'eau saumâtre

### Prompt template

```
8 seconds, 9:16 vertical, Saloum Islands mangrove waters at golden hour,
sun low on horizon, warm orange-red light bathing the scene,
distant mangrove trees in soft silhouette.

24mm wide angle lens, deep depth of field, all in focus,
camera at chest height, very subtle handheld micro-shake, organic feel.

Foreground: brackish water gently rippling, reflecting golden sky.
Mid-ground: traditional wooden pirogue floating, no figures visible.
Background: dense mangrove root system at water edge, distant horizon.

Beats:
0-2s: static wide shot, water shimmering, gentle ripples.
2-5s: smooth slow pan right 30°, revealing more of the coastline.
5-8s: pan slows to a stop on a single mangrove tree silhouetted against the sun.

Tone: contemplative, earthy, soulful feel.

Style: smooth slow pan, organic 35mm grain, sun-warmed 5500K color grade,
gentle atmospheric haze, no lens flare.

Distant ocean waves, mangrove leaves rustling in breeze, no music.

The patience of two days of sun, two hands, and one ancient method.

No on-screen text, no captions, no subtitles, no logos.
```

**Paramètres fal.ai** :
- Endpoint : `bytedance/seedance-2.0/text-to-video` (ou image-to-video si tu as une photo Saloum de référence)
- duration: 8
- aspect_ratio: "9:16"
- resolution: "720p" (ou 1080p si pour documentaire premium)
- generate_audio: true

**Coût estimé** : ~$2,40 en 720p, ~$3,80 en 1080p

---

## Template 4 — Variant Macro ASMR (10-15s)

**Quand l'utiliser** : pour les contenus éducatifs Quiz Guedjologue, montrer la texture/qualité produit en ASMR. Vise l'engagement (sauvegardes, replays).

### Prompt template

```
12 seconds, 9:16 vertical, dark slate marble surface,
warm golden side light from right at 45°, color temperature 4500K.

Dark-skinned hands of a Senegalese man in his mid-40s, deep brown West African complexion, warm rich umber tone, gold rings,
long-sleeve cream linen shirt cuffs visible.

Macro lens 100mm, very shallow depth of field f/2.0,
camera at top-down 80° angle, completely static lock.

@(product) arranged in a small ceramic bowl on marble.
Soft natural shadow under bowl.

Beats:
0-2s: static shot, slight light pulse.
2-5s: fingertips enter from right, slowly stir the product.
5-8s: a small pinch is lifted close to camera, particles falling slowly.
8-12s: pinch released back into bowl, hand exits, settles back to stillness.

Tone: warm, ASMR, hypnotic feel.

Style: completely locked tripod, very fine grain, neutral 5000K color grade,
no vignette, sharp focus on grains and texture.

ASMR sound of stirring particles, gentle clinking, no music.

Before there were supermarkets, there was this.

No on-screen text, no captions, no subtitles, no logos.
Hands only, no face visible.
```

**Paramètres fal.ai** :
- duration: 12
- aspect_ratio: "9:16"
- resolution: "720p"
- generate_audio: true

**Coût estimé** : ~$3,60

---

## Comment utiliser ces templates

1. **Choisir le template** selon l'objectif (hook 5s / pub 10s / B-roll 8-12s)
2. **Remplacer `@(product)`** par la description visuelle du produit (voir `products.md`)
3. **Personnaliser la "Closing Emotional Line"** pour coller au produit/contexte
4. **Ajuster les beats** selon ce qu'on veut montrer
5. **Vérifier mots interdits** (cinematic, professional, etc.) — réécrire si besoin
6. **Vérifier nombre de mots** (150-200 idéal, max 260)
7. **Présenter le prompt à Lamine** pour validation
8. **Lancer** via `scripts/generate.py` après son OK

## Convention de nommage des outputs

```
outputs/
  ├── crevettes-cipakh-faceless-v1.mp4
  ├── crevettes-cipakh-faceless-v2.mp4
  ├── pack-saloum-reveal-v1.mp4
  ├── saloum-broll-pan-v1.mp4
  └── netetou-asmr-v1.mp4
```

Format : `{produit}-{type}-v{N}.mp4`
