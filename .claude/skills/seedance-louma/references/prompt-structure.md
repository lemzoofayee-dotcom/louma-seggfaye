# Structure de Prompt Seedance 2.0 — 8 blocs

Toujours respecter cet ordre. Total 100-260 mots.

## Bloc 1 — DURATION + ASPECT + SETTING + LIGHTING

Ouvrir avec les contraintes techniques + le décor + la lumière.

**Pattern** :
```
{duration}, {aspect_ratio} vertical, {surface/setting},
{lighting description with angle and temperature}.
```

**Exemple Louma** :
```
5 seconds, 9:16 vertical, dark slate marble surface with subtle natural veining,
warm golden side light from right at 45°, color temperature 4500K, soft halo on subject edge.
```

---

## Bloc 2 — CHARACTER (si humain présent)

Décrire les mains/personne qui apparaît, avec habillage couvrant.

**Pattern** :
```
{character description with covered skin, hands only for Lamine}
```

**Exemple Louma (mains de Lamine)** :
```
Dark-skinned hands of a Senegalese man in his mid-40s, deep brown West African complexion, warm rich umber tone, two thin gold rings on right hand,
long-sleeve cream linen shirt with cuffs visible, gentle confident gestures.
```

**Si pas de personnage** : sauter ce bloc.

---

## Bloc 3 — CAMERA SETUP

Lentille, profondeur, hauteur, type de plan.

**Pattern** :
```
{lens} {depth of field} {camera height/angle} {static or movement}
```

**Exemple Louma** :
```
Macro lens 100mm, shallow depth of field f/2.8, 
camera at eye level slightly downward 15°, locked tripod feel.
```

**Variantes utiles** :
- Hook produit : `"50mm lens, slight wide angle, low angle 30° looking up at product"`
- Flat-lay : `"top-down 90° angle, 35mm lens, deep depth of field"`
- B-roll Saloum : `"24mm wide angle, deep depth of field, chest height handheld"`

---

## Bloc 4 — SCENE / PRODUCT

Décrire ce qu'on voit dans le cadre. **Si image-to-video, référencer l'image source ici** avec `@(product)`.

**Pattern** :
```
@(product) {placement} {context} {peripheral elements}
```

**Exemple Louma** :
```
@(product) sitting centered on the marble surface. 
Steam slowly rises and dissipates. 
Cream linen cloth corner visible top-left of frame.
A single hibiscus flower placed at the bottom-right edge as accent.
```

---

## Bloc 5 — BEAT-BY-BEAT TIMELINE

Découper la durée en moments précis.

**Pattern (5 secondes)** :
```
0-1s: {opening action}.
1-3s: {main action / development}.
3-5s: {closing beat / final emphasis}.
```

**Exemple Louma — 5s hook** :
```
0-1s: empty marble surface, light gradient softly shifts.
1-3s: hand enters from right edge, fingertips first, then full hand.
3-4s: hand gently lifts the product and holds it close to camera.
4-5s: subtle rotation of the product, light catches the gold accents.
```

**Exemple Louma — 10s reveal** :
```
0-2s: closed kraft paper box centered on marble, gold foil label visible.
2-4s: hands enter, slowly lift the lid.
4-7s: lid opens, revealing 4 vacuum pouches arranged inside.
7-9s: hand picks up one pouch, holds it close to camera.
9-10s: pouch slowly turning, label glinting in golden light.
```

---

## Bloc 6 — TONE / MOOD

3-5 mots-clés émotionnels.

**Pattern** :
```
{adjective}, {adjective}, {adjective} feel.
```

**Bibliothèque Louma approuvée** :
- "intimate, reverent, slow-motion feel"
- "contemplative, earthy, soulful feel"
- "warm, ASMR, hypnotic feel"
- "premium, refined, hushed feel"
- "ancestral, soulful, grounded feel"

**INTERDITS** : "cinematic", "professional", "stunning", "dramatic", "modern".

---

## Bloc 7 — CAMERA MOVEMENT + GRAIN + STYLE

Ajouter la touche finale stylistique.

**Pattern** :
```
{camera movement} {film grain} {color grade} {special effect}
```

**Exemple Louma** :
```
Subtle slow push-in dolly 5%, fine 35mm film grain, 
warm 4500K color grade with golden highlights,
gentle vignette, no lens flare.
```

**Variantes** :
- Hook intense : `"slow push-in 8%, heavier 16mm grain, warmer 4000K, slight vignette"`
- Macro contemplatif : `"completely static lock, very fine grain, neutral 5000K, no vignette"`
- B-roll Saloum : `"slow pan right 30°, organic 35mm grain, sun-warmed 5500K, gentle haze"`

---

## Bloc 8 — CLOSING EMOTIONAL LINE

Une phrase qui résume l'émotion, écrite comme un copywriter.

**Exemples Louma** :
- "the kind of moment that makes you remember your grandmother's kitchen."
- "a small object holding the entire story of a coastline."
- "what your mother brought back from her last trip home, wrapped in linen."
- "the patience of two days of sun, two hands, and one ancient method."
- "before there were supermarkets, there was this."

**Cette phrase oriente l'algorithme Seedance vers une émotion précise**.

---

## Constraints (TOUJOURS finir par ça)

```
No on-screen text, no captions, no subtitles, no logos.
Hands only, no face visible.
```

---

## Template complet (à copier-coller-adapter)

```
{1. DURATION+ASPECT+SETTING+LIGHTING}.

{2. CHARACTER si présent}.

{3. CAMERA SETUP}.

{4. SCENE/PRODUCT avec @(product) si image-to-video}.

Beats:
{5. BEAT-BY-BEAT TIMELINE}.

Tone: {6. TONE/MOOD}.

Style: {7. CAMERA MOVEMENT + GRAIN + STYLE}.

{8. CLOSING EMOTIONAL LINE}.

No on-screen text, no captions, no subtitles, no logos. 
Hands only, no face visible.
```

---

## Comptage de mots — règle stricte

- **Min 100 mots** : sinon le modèle improvise trop
- **Max 260 mots** : au-delà, le modèle perd la cohérence
- **Sweet spot Louma** : **150-200 mots**

## Ne JAMAIS écrire

- ❌ Mots interdits : `cinematic`, `professional`, `stunning`, `beautiful`, `amazing`
- ❌ Texte affiché : `"showing text 'BUY NOW'"`, `"with subtitle"`, `"caption appears"`
- ❌ Personnages avec peau exposée : `"bare arms"`, `"shorts"`, `"tank top"` → modération refuse
- ❌ Marques tierces : `"like in [name brand] ad"`, `"Apple style"` (copyright)
- ❌ Personnes réelles : `"Rihanna style"`, `"Beyoncé look"` (modération refuse)
