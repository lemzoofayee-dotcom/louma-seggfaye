#!/usr/bin/env python3
"""
Seedance 2.0 video generator pour Louma by Seggfaye.
Utilise fal.ai (FAL_KEY dans .env).

Usage:
    python3 generate.py --prompt-file prompt.txt --image path/to/product.jpg --duration 10
    python3 generate.py --prompt-file prompt.txt --duration 5 --no-image  # text-to-video

Requires:
    pip install fal-client python-dotenv
    FAL_KEY défini dans .env à la racine du projet
"""

import argparse
import os
import sys
import time
from pathlib import Path

try:
    import fal_client
except ImportError:
    print("ERREUR: fal_client non installé. Faire: pip3 install fal-client --break-system-packages", file=sys.stderr)
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # optional


def next_version(folder: Path, prefix: str) -> int:
    """Retourne le prochain numéro de version v1, v2, v3..."""
    folder.mkdir(parents=True, exist_ok=True)
    existing = list(folder.glob(f"{prefix}-v*.mp4"))
    return len(existing) + 1


def upload_image(image_path: Path) -> str:
    """Upload une image locale vers fal.ai et retourne l'URL."""
    print(f"  → Upload image: {image_path.name}", flush=True)
    url = fal_client.upload_file(str(image_path))
    print(f"  → Image URL: {url[:80]}...", flush=True)
    return url


def estimate_cost(duration: int, resolution: str) -> float:
    """Estimation tarif Seedance 2.0 sur fal.ai (avril 2026)."""
    rate = {
        "480p": 0.20,
        "720p": 0.30,
        "1080p": 0.48,
    }.get(resolution, 0.30)
    return duration * rate


def generate(prompt: str, image_url: str | None, duration: int, aspect: str,
             resolution: str, generate_audio: bool) -> dict:
    """Lance la génération Seedance 2.0 et retourne le dict résultat."""

    if image_url:
        endpoint = "fal-ai/bytedance/seedance/v2/pro/image-to-video"
        payload = {
            "prompt": prompt,
            "image_url": image_url,
            "duration": str(duration) if duration in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) else "auto",
            "aspect_ratio": aspect,
            "resolution": resolution,
            "generate_audio": generate_audio,
        }
    else:
        endpoint = "fal-ai/bytedance/seedance/v2/pro/text-to-video"
        payload = {
            "prompt": prompt,
            "duration": str(duration),
            "aspect_ratio": aspect,
            "resolution": resolution,
            "generate_audio": generate_audio,
        }

    print(f"\n  → Endpoint: {endpoint}", flush=True)
    print(f"  → Duration: {duration}s | Aspect: {aspect} | Resolution: {resolution}", flush=True)
    print(f"  → Coût estimé: ~${estimate_cost(duration, resolution):.2f}", flush=True)
    print(f"  → Lancement génération (peut prendre 1-3 minutes)...", flush=True)

    handler = fal_client.submit(endpoint, arguments=payload)

    # Stream des updates
    for event in handler.iter_events(with_logs=False):
        if hasattr(event, "status"):
            print(f"    {time.strftime('%H:%M:%S')} status: {event.status}", flush=True)

    result = handler.get()
    return result


def download(video_url: str, dest: Path) -> bool:
    """Télécharge la vidéo générée."""
    import urllib.request
    print(f"  → Download → {dest.name}", flush=True)
    try:
        urllib.request.urlretrieve(video_url, dest)
        size_kb = dest.stat().st_size // 1024
        print(f"  ✓ Saved: {dest} ({size_kb} KB)", flush=True)
        return size_kb > 50  # 0KB = échec modération
    except Exception as e:
        print(f"  ✗ Download failed: {e}", flush=True)
        return False


def main():
    parser = argparse.ArgumentParser(description="Seedance 2.0 video generator pour Louma")
    parser.add_argument("--prompt-file", type=Path, help="Fichier .txt contenant le prompt")
    parser.add_argument("--prompt", type=str, help="Prompt en ligne de commande (si pas de fichier)")
    parser.add_argument("--image", type=Path, help="Image source pour image-to-video")
    parser.add_argument("--no-image", action="store_true", help="Mode text-to-video (pas d'image)")
    parser.add_argument("--duration", type=int, default=10, help="Durée en secondes (4-15)")
    parser.add_argument("--aspect", type=str, default="9:16", help="Aspect ratio (9:16, 16:9, 1:1...)")
    parser.add_argument("--resolution", type=str, default="720p", choices=["480p", "720p", "1080p"])
    parser.add_argument("--no-audio", action="store_true", help="Désactiver audio (par défaut audio activé)")
    parser.add_argument("--name", type=str, default="louma", help="Préfixe nom fichier (ex: crevettes-cipakh-faceless)")
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).parent.parent / "outputs",
                        help="Dossier de sortie")

    args = parser.parse_args()

    if not os.environ.get("FAL_KEY"):
        print("ERREUR: FAL_KEY non défini. Vérifier .env à la racine du projet.", file=sys.stderr)
        sys.exit(1)

    # Lecture du prompt
    if args.prompt_file:
        prompt = args.prompt_file.read_text().strip()
    elif args.prompt:
        prompt = args.prompt.strip()
    else:
        print("ERREUR: --prompt-file ou --prompt requis.", file=sys.stderr)
        sys.exit(1)

    word_count = len(prompt.split())
    print(f"\n=== Seedance 2.0 — Louma ===", flush=True)
    print(f"  Prompt: {word_count} mots", flush=True)
    if word_count < 100:
        print(f"  ⚠️  Prompt court (<100 mots) — Seedance peut improviser", flush=True)
    elif word_count > 260:
        print(f"  ⚠️  Prompt long (>260 mots) — risque perte cohérence", flush=True)

    # Upload image si présente
    image_url = None
    if args.image and not args.no_image:
        if not args.image.exists():
            print(f"ERREUR: Image introuvable: {args.image}", file=sys.stderr)
            sys.exit(1)
        image_url = upload_image(args.image)

    # Génération
    result = generate(prompt, image_url, args.duration, args.aspect,
                      args.resolution, not args.no_audio)

    video_url = result.get("video", {}).get("url") if isinstance(result.get("video"), dict) else result.get("video_url")
    if not video_url:
        print(f"  ✗ Pas d'URL vidéo dans la réponse: {result}", file=sys.stderr)
        sys.exit(1)

    # Download
    args.output_dir.mkdir(parents=True, exist_ok=True)
    v = next_version(args.output_dir, args.name)
    dest = args.output_dir / f"{args.name}-v{v}.mp4"

    if download(video_url, dest):
        print(f"\n✅ DONE — {dest}", flush=True)
        print(f"   URL fal.ai (expire dans ~1h): {video_url}", flush=True)
    else:
        print(f"\n❌ ÉCHEC — Vidéo trop petite (probable rejet modération).", flush=True)
        print(f"   Vérifier: peau couverte, pas de marques, pas de personnes réelles.", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
