import numpy as np
from utils import prepare_photon, measure_photon

class BB84:
    def __init__(self, photon_count=100):
        self.photon_count = photon_count
        self.alice_bases = []
        self.bob_bases = []
        self.alice_key = []
        self.bob_key = []
    
    def generate_key(self):
        # Step 1: Alice prepares random bits and bases
        alice_bits = np.random.randint(0, 2, self.photon_count)
        self.alice_bases = np.random.randint(0, 2, self.photon_count)
        
        # Step 2: Alice sends photons to Bob
        photons = [prepare_photon(bit, base) for bit, base in zip(alice_bits, self.alice_bases)]
        
        # Step 3: Bob randomly chooses bases to measure the photons
        self.bob_bases = np.random.randint(0, 2, self.photon_count)
        bob_measurements = [measure_photon(photon, base) for photon, base in zip(photons, self.bob_bases)]
        
        # Step 4: Classical communication to reconcile the key
        for i in range(self.photon_count):
            if self.alice_bases[i] == self.bob_bases[i]:
                self.alice_key.append(alice_bits[i])
                self.bob_key.append(bob_measurements[i])

    def get_reconciled_key(self):
        return self.alice_key, self.bob_key
