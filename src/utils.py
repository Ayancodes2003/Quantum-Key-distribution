import numpy as np

def prepare_photon(bit, base):
    """
    Prepares a photon in a specific state based on the bit and base.
    Base 0 = rectilinear (|0⟩, |1⟩), Base 1 = diagonal (|+⟩, |-⟩)
    """
    if base == 0:
        return '|0>' if bit == 0 else '|1>'
    else:
        return '|+>' if bit == 0 else '|->'

def measure_photon(photon, base):
    """
    Measures the photon based on Bob's randomly chosen base.
    If Bob's base matches Alice's, the bit is correctly measured.
    """
    if photon in ['|0>', '|1>']:
        # Rectilinear basis (Base 0)
        if base == 0:
            return 0 if photon == '|0>' else 1
        else:
            return np.random.randint(0, 2)  # Random measurement if wrong base
    elif photon in ['|+>', '|->']:
        # Diagonal basis (Base 1)
        if base == 1:
            return 0 if photon == '|+>' else 1
        else:
            return np.random.randint(0, 2)  # Random measurement if wrong base
