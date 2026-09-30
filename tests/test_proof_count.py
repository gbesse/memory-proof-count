import unittest

from proof_count import audit


class ProofCountTests(unittest.TestCase):
    def test_counts_distinct_sources(self):
        rows = audit([{"id": "o", "proof_count": 1, "source_memory_ids": ["a", "b", "b"]}])
        self.assertEqual(rows[0]["expected"], 2)
        self.assertFalse(rows[0]["matches"])

    def test_ignores_non_observation_records(self):
        rows = audit([{"type": "fact", "proof_count": 9, "source_memory_ids": ["a"]},
                      {"type": "observation", "proof_count": 1, "source_memory_ids": ["a"]}])
        self.assertEqual(len(rows), 1)

    def test_rejects_invalid_count(self):
        with self.assertRaises(ValueError):
            audit([{"proof_count": True, "source_memory_ids": ["a"]}])
