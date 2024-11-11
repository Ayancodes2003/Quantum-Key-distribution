class ClassicalCommunication:
    def reconcile_key(self, alice_bases, bob_bases):
        """
        Reconciles the key by publicly comparing Alice's and Bob's bases.
        Returns the indices where the bases match.
        """
        matching_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
        return matching_indices

    def generate_final_key(self, alice_key, bob_key, matching_indices):
        """
        Generates the final reconciled key using the matching indices.
        """
        final_alice_key = [alice_key[i] for i in matching_indices]
        final_bob_key = [bob_key[i] for i in matching_indices]
        return final_alice_key, final_bob_key
