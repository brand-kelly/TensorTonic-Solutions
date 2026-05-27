import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    rng = np.random if rng is None else rng
    x_arr = np.array(x, dtype=float)
    pattern = (rng.random(x_arr.shape) < 1.0 - p).astype(x_arr.dtype)

    pattern /= (1 - p)

    applied_dropout = x_arr * pattern
    
    return (applied_dropout, pattern)