from pathlib import Path
from PIL import Image
import shutil

# ──── USER CONFIG ────────────────────────────────────────────────────────────
INPUT_DIR      = r'../../1/Image Sample Dataset'   # folder containing images
OUTPUT_DIR     = r"../../1/webp"     # where .webp files will be written
RECURSIVE      = True     # descend into subfolders
OVERWRITE_OUT  = True     # delete OUTPUT_DIR before starting
LOSSLESS       = False    # True → lossless WebP; False → lossy
QUALITY        = 80       # 0–100 (ignored if LOSSLESS=True)
KEEP_STRUCTURE = True     # mirror the source folder tree in OUTPUT_DIR?
# ─────────────────────────────────────────────────────────────────────────────

VALID_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff",
    ".gif", ".webp", ".heic", ".heif", ".avif", ".jfif"
}

def prepare_out_dir(out_dir: Path, overwrite: bool = False) -> None:
    if out_dir.exists() and overwrite:
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

def convert_image(src_path: Path, dst_path: Path) -> None:
    with Image.open(src_path) as img:
        # Convert mode if needed to preserve transparency
        if img.mode in ("P", "RGBA", "LA"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")

        params = {"lossless": LOSSLESS}
        if not LOSSLESS:
            params["quality"] = QUALITY

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(dst_path, "webp", **params)

def iter_images(folder: Path, recursive: bool = True):
    if recursive:
        yield from (p for p in folder.rglob("*") if p.suffix.lower() in VALID_SUFFIXES)
    else:
        yield from (p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in VALID_SUFFIXES)

def main() -> None:
    src_root = Path(INPUT_DIR).expanduser().resolve()
    dst_root = Path(OUTPUT_DIR).expanduser().resolve()

    prepare_out_dir(dst_root, OVERWRITE_OUT)

    total, converted = 0, 0
    for src in iter_images(src_root, RECURSIVE):
        total += 1
        rel_path = src.relative_to(src_root) if KEEP_STRUCTURE else src.name
        dst = dst_root / rel_path
        dst = dst.with_suffix(".webp")

        try:
            convert_image(src, dst)
            converted += 1
        except Exception as e:
            print(f"[WARN] Skipped {src} → {e}")

    print(
        f"Finished. Found {total} images, successfully converted {converted} "
        f"({converted/total*100:.1f}%). Output in: {dst_root}"
    )

if __name__ == "__main__":
    main()
