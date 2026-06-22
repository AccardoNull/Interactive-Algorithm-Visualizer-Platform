import json
from pathlib import Path
from datetime import datetime

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

IMAGE_DIR = Path("static/images")
OUTPUT_FILE = Path("data/images.json")


def filename_to_tags(filename: str) -> list[str]:
    stem = Path(filename).stem
    words = stem.replace("-", "_").split("_")

    tags = []

    for word in words:
        cleaned = word.strip().lower()
        if cleaned:
            tags.append(cleaned)

    return tags


def build_image_index() -> list[dict]:
    images = []

    for index, image_path in enumerate(IMAGE_DIR.iterdir(), start=1):
        if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        stat = image_path.stat()

        image_record = {
            "id": index,
            "filename": image_path.name,
            "url": f"/images/{image_path.name}",
            "filepath": str(image_path),
            "extension": image_path.suffix.lower(),
            "size_bytes": stat.st_size,
            "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "tags": filename_to_tags(image_path.name),
            "description": " ".join(filename_to_tags(image_path.name)),
        }

        images.append(image_record)

    return images


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    images = build_image_index()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(images, file, indent=2)

    print(f"Indexed {len(images)} image(s) into {OUTPUT_FILE}")


if __name__ == "__main__":
    main()