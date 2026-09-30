# Memory Proof Count

**Detecte observaciones cuyo número de pruebas no coincide con sus fuentes distintas.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Proyectos relacionados

- [Hindsight](https://github.com/vectorize-io/hindsight) — Almacena las observaciones y enlaces de fuentes auditados aquí.
- [Issue #4955](https://github.com/vectorize-io/hindsight/issues/4955) — Describe un error de recuento durante la creación.
- [memory-source-links](https://github.com/gbesse/memory-source-links) — Comprueba recibos de alias y fuente; esta herramienta comprueba el número de pruebas de una observación.

Estos enlaces describen proyectos relacionados, sin afiliación.

## Probar

```sh
python3 proof_count.py demo --lang es
```

## Qué comprueba esta herramienta

Comprueba filas exportadas de Hindsight con `proof_count` y `source_memory_ids`; acepta arreglos JSON, envoltorios y JSONL. Una diferencia devuelve 1 en modo `check`.

## Usar con sus datos

```sh
python3 proof_count.py check observations.json --lang es --json
```

Exporte solo los campos necesarios de su banco Hindsight a `observations.json` y ejecute `check`. La prueba cuenta una fuente repetida una sola vez.

## Alcance y límites

Comprobación local sin cliente API de Hindsight ni reparación automática. Algunas respuestas omiten los ID de fuente; se saltan y una entrada sin filas verificables falla. No juzga la independencia real de las fuentes.

## Pruebas

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
