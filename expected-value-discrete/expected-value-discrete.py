import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.sum(p) != 1:
        raise ValueError
    return float(np.dot(x, p))