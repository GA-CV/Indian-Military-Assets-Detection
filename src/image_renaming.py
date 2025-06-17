from pathlib import Path
import itertools

# ─── USER CONFIG ─────────────────────────────────────────────────────────────
IMG_DIR     = r'../Sample Image Dataset'  # folder containing images
EXTENSIONS  = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".gif"}  # case‑insensitive
ZERO_PAD    = True     # 1 → 0001, 0002, …  if you prefer natural numbers set to False
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    folder = Path(IMG_DIR).expanduser().resolve()
    if not folder.is_dir():
        raise SystemExit(f"Folder not found: {folder}")

    # Collect and sort images for deterministic renaming
    images = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )

    if not images:
        print("No images found with specified extensions.")
        return

    # Zero‑padding width (only used if ZERO_PAD=True)
    pad = len(str(len(images))) if ZERO_PAD else 0

    # Two‑pass strategy to avoid name collisions:
    # 1. Rename to a temporary hidden name
    # 2. Rename to final sequential name
    temp_suffix = ".tmp_renaming"

    print(f"Found {len(images)} images, renaming …")

    # Pass 1 – temporary names
    for idx, img in enumerate(images, 1):
        img.rename(img.with_name(f".tmp_{idx}{temp_suffix}{img.suffix}"))

    # Pass 2 – final sequential names
    temp_files = sorted(folder.glob(f".tmp_*{temp_suffix}*"))
    for idx, tmp in enumerate(temp_files, 1):
        new_name = f"{idx:0{pad}d}{tmp.suffix.replace(temp_suffix,'')}" if ZERO_PAD else f"{idx}{tmp.suffix.replace(temp_suffix,'')}"
        tmp.rename(tmp.with_name(new_name))

    print("Renaming complete!")

if __name__ == "__main__":
    main()
