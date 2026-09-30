#!/usr/bin/env python3
"""Compare an exported Hindsight observation's proof_count to distinct source IDs."""
import argparse
import json
import sys
from pathlib import Path

LABELS = {
    "en": ("Proof count check", "matches", "mismatch", "observations checked"),
    "fr": ("Contrôle du nombre de preuves", "cohérent", "écart", "observations contrôlées"),
    "es": ("Comprobación del número de pruebas", "coincide", "diferencia", "observaciones comprobadas"),
}


def records_from_file(path):
    text = Path(path).read_text(encoding="utf-8")
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            for key in ("observations", "memory_units", "items"):
                if isinstance(data.get(key), list):
                    return data[key]
            return [data]
        if isinstance(data, list):
            return data
    except json.JSONDecodeError:
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    raise ValueError("expected a JSON object, array or JSONL file")


def audit(records):
    result = []
    for index, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"record {index} is not an object")
        if item.get("type", item.get("kind", "observation")) != "observation":
            continue
        if "source_memory_ids" not in item or "proof_count" not in item:
            continue
        ids = item["source_memory_ids"]
        count = item["proof_count"]
        if not isinstance(ids, list) or not all(isinstance(x, str) and x for x in ids):
            raise ValueError(f"record {index} has invalid source_memory_ids")
        if type(count) is not int or count < 0:
            raise ValueError(f"record {index} has invalid proof_count")
        expected = len(set(ids))
        result.append({"id": str(item.get("id", index)), "stored": count, "expected": expected, "matches": count == expected})
    if not result:
        raise ValueError("no observations with source_memory_ids and proof_count")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("demo", "check"))
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--lang", choices=LABELS, default="en")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    path = Path(__file__).parent / "fixtures" / "observations.json" if args.command == "demo" else args.path
    if not path:
        parser.error("check requires a JSON or JSONL path")
    try:
        rows = audit(records_from_file(path))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"observations": rows}, ensure_ascii=False))
    else:
        title, good, bad, total = LABELS[args.lang]
        print(f"{title}: {len(rows)} {total}")
        for row in rows:
            print(f"{row['id']}: {good if row['matches'] else bad} ({row['stored']} / {row['expected']})")
    return 1 if args.command == "check" and any(not r["matches"] for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
