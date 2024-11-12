import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.classical_communication import ClassicalCommunication

class TestClassicalCommunication(unittest.TestCase):
    def setUp(self):
        self.cc = ClassicalCommunication()

    def test_reconcile_key(self):
        """Test that key reconciliation returns the correct indices."""
        alice_bases = [0, 1, 0, 1, 0]
        bob_bases = [0, 1, 1, 0, 0]
        matching_indices = self.cc.reconcile_key(alice_bases, bob_bases)
        self.assertEqual(matching_indices, [0, 1, 4])

    def test_generate_final_key(self):
        """Test that final key generation works correctly."""
        alice_key = [0, 1, 0, 1, 0]
        bob_key = [0, 1, 1, 1, 0]
        matching_indices = [0, 1, 4]
        final_alice_key, final_bob_key = self.cc.generate_final_key(alice_key, bob_key, matching_indices)
        self.assertEqual(final_alice_key, [0, 1, 0])
        self.assertEqual(final_bob_key, [0, 1, 0])

if __name__ == "__main__":
    unittest.main()
