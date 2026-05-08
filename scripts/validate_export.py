import json

# ...existing code...
#!/usr/bin/env python3
import json
import argparse
from pathlib import Path
from collections import Counter
import sys

def validate(path: Path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 1
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return 2

    if not isinstance(data, list):
        print("Expected top-level JSON array of tasks.")
        return 3

    total = len(data)
    annotated = 0
    per_label = Counter()
    tasks_without_annotations = []

    for task in data:
        anns = task.get("annotations") or []
        if len(anns) == 0:
            tasks_without_annotations.append(task.get("id"))
        else:
            annotated += 1
            for ann in anns:
                for r in ann.get("result", []):
                    labels = r.get("value", {}).get("rectanglelabels") or []
                    for l in labels:
                        per_label[l] += 1

    print(f"Total tasks: {total}")
    print(f"Annotated tasks: {annotated}")
    print("Label counts:")
    for label, cnt in per_label.most_common():
        print(f"  {label}: {cnt}")
    if tasks_without_annotations:
        print(f"Tasks without annotations (sample up to 10): {tasks_without_annotations[:10]}")
    return 0

def main():
    p = argparse.ArgumentParser(description="Validate Label Studio JSON export")
    p.add_argument("path", nargs="?", default=str(Path(__file__).resolve().parents[1] / "exports" / "label_studio_export_json.json"))
    args = p.parse_args()
    return validate(Path(args.path))

if __name__ == "__main__":
    sys.exit(main())






path = "../exports/label_studio_export_json.json"

with open(path, "r") as f:
    data = json.load(f)

print(f"Total tasks: {len(data)}")

annotated = 0

for task in data:
    if "annotations" in task and len(task["annotations"]) > 0:
        annotated += 1

print(f"Annotated tasks: {annotated}")