import numpy as np

class Eavesdropper:
    def intercept_photons(self, photons):
        """
        Eve intercepts and randomly measures the photons with random bases.
        This causes errors in the final key if Bob and Alice compare their bits.
        """
        eve_bases = np.random.randint(0, 2, len(photons))
        eve_measurements = [self.measure_photon(photon, base) for photon, base in zip(photons, eve_bases)]
        return eve_measurements, eve_bases

    def measure_photon(self, photon, base):
        """
        Measures a photon similarly to Bob, but causes errors if her base is wrong.
        """
        # Simulate measurement based on base, similar to Bob's process
        if photon in ['|0>', '|1>']:
            return 0 if photon == '|0>' else 1
        elif photon in ['|+>', '|->']:
            return 0 if photon == '|+>' else 1
        else:
            return np.random.randint(0, 2)  # Random error
