import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.eavesdropper_simulation import Eavesdropper
from src.utils import prepare_photon

class TestEavesdropper(unittest.TestCase):

    def setUp(self):
        self.eve = Eavesdropper()
    
    def test_intercept_photons(self):
        """Test that Eve can intercept photons and produce measurements."""
        photons = [prepare_photon(0, 0), prepare_photon(1, 1)]
        eve_measurements, eve_bases = self.eve.intercept_photons(photons)
        self.assertEqual(len(eve_measurements), len(photons))
        self.assertEqual(len(eve_bases), len(photons))

if __name__ == "__main__":
    unittest.main()
