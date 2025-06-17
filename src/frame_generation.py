from pathlib import Path
import cv2
import shutil

# ====== USER CONFIG ======
VIDEO_PATH = r'../Videos/video1.MOV'   # ← put your video file here
OUT_DIR    = r'../Image Dataset/images'    # ← where images will be saved
STRIDE     = 49                            # save every 50th frame
OVERWRITE  = True                           # delete OUT_DIR if it exists
# ==========================


def prepare_output_dir(out_dir: Path, overwrite: bool = False) -> None:
    """Create or clear the output directory."""
    if out_dir.exists() and overwrite:
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)


def save_frames(video_path: Path, out_dir: Path, stride: int) -> None:
    """Read video and write every `stride`‑th frame to disk."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise IOError(f"Could not open video: {video_path}")

    frame_idx = saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:          # end of video
            break
        if frame_idx % stride == 0:
            filename = out_dir / f"frame_{frame_idx:06d}.png"
            cv2.imwrite(str(filename), frame)
            saved += 1
        frame_idx += 1

    cap.release()
    print(f"Done: processed {frame_idx} frames, saved {saved} every {stride} frames.")


def main() -> None:
    video_path = Path(VIDEO_PATH).expanduser().resolve()
    out_dir    = Path(OUT_DIR).expanduser().resolve()

    prepare_output_dir(out_dir, OVERWRITE)
    save_frames(video_path, out_dir, STRIDE)


if __name__ == "__main__":
    main()
