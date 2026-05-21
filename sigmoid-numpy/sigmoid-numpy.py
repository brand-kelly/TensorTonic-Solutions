import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    sigma_res = 1 / (1 + (1 / np.exp(x)))

    return sigma_res