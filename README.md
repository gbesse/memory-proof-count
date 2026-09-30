# Memory Proof Count

**Find observations whose stored proof count disagrees with their distinct source IDs.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Related projects

- [Hindsight](https://github.com/vectorize-io/hindsight) — Stores observations and source links that this tool audits.
- [Issue #4955](https://github.com/vectorize-io/hindsight/issues/4955) — Reports a create-path count mismatch.
- [memory-source-links](https://github.com/gbesse/memory-source-links) — Checks alias-to-source receipts; this tool checks an observation’s numeric proof count.

Links describe technical neighbors, not an affiliation.

## Try it

```sh
python3 proof_count.py demo --lang en
```

## What this checks

Checks exported Hindsight observation rows with `proof_count` and `source_memory_ids`; accepts JSON arrays, envelopes and JSONL. A mismatch exits 1 in `check` mode.

## Use with your data

```sh
python3 proof_count.py check observations.json --lang en --json
```

Export only the needed fields from your own Hindsight bank to `observations.json`, then run `check`. The fixture shows a repeated source counted only once.

## Scope and limits

It is an offline consistency check, not an Hindsight API client or automatic repair. Some API responses omit source IDs; those records are skipped and an all-skipped input is an error. It cannot judge whether sources are genuinely independent.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
