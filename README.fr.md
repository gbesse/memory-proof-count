# Memory Proof Count

**Repérez les observations dont le nombre de preuves diverge de leurs sources distinctes.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Projets voisins

- [Hindsight](https://github.com/vectorize-io/hindsight) — Stocke les observations et liens de sources contrôlés ici.
- [Issue #4955](https://github.com/vectorize-io/hindsight/issues/4955) — Décrit une erreur de comptage lors de la création.
- [memory-source-links](https://github.com/gbesse/memory-source-links) — Vérifie des reçus alias-source ; cet outil contrôle le nombre de preuves d’une observation.

Ces liens décrivent des projets voisins, sans affiliation.

## Essayer

```sh
python3 proof_count.py demo --lang fr
```

## Ce que cet outil vérifie

Contrôle des lignes Hindsight exportées avec `proof_count` et `source_memory_ids` ; accepte tableau JSON, enveloppe ou JSONL. Une divergence renvoie 1 en mode `check`.

## Utiliser avec vos données

```sh
python3 proof_count.py check observations.json --lang fr --json
```

Exportez uniquement les champs nécessaires de votre banque Hindsight dans `observations.json`, puis lancez `check`. La fixture compte une source répétée une seule fois.

## Périmètre et limites

Contrôle hors ligne, sans client API Hindsight ni réparation automatique. Certaines réponses API omettent les IDs de source ; ces lignes sont ignorées et une entrée sans ligne vérifiable échoue. Ne juge pas l’indépendance réelle des sources.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
