import unittest
from pathlib import Path


class SandboxMarkerTests(unittest.TestCase):
    def test_markers_are_valid(self):
        """A synthetic rejected revision fails without disclosing input data."""
        root = Path(__file__).resolve().parents[1] / "markers"
        for marker in sorted(root.glob("*.txt")):
            with self.subTest(marker=marker.name):
                self.assertEqual(marker.read_text(encoding="utf-8").strip(), "accepted")
