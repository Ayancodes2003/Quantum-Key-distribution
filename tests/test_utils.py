import unittest
from src.utils import prepare_photon, measure_photon

class TestUtils(unittest.TestCase):

    def test_prepare_photon(self):
        """Test photon preparation."""
        self.assertEqual(prepare_photon(0, 0), '|0>')
        self.assertEqual(prepare_photon(1, 0), '|1>')
        self.assertEqual(prepare_photon(0, 1), '|+>')
        self.assertEqual(prepare_photon(1, 1), '|->')

    def test_measure_photon(self):
        """Test photon measurement."""
        self.assertEqual(measure_photon('|0>', 0), 0)
        self.assertEqual(measure_photon('|1>', 0), 1)
        self.assertEqual(measure_photon('|+>', 1), 0)
        self.assertEqual(measure_photon('|->', 1), 1)
        # Test random measurement (simulate wrong basis)
        self.assertIn(measure_photon('|0>', 1), [0, 1])
        self.assertIn(measure_photon('|1>', 1), [0, 1])

if __name__ == "__main__":
    unittest.main()
