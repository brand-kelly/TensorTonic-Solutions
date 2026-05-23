import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    x_arr = np.array(X, dtype=float)

    numerator = x_arr - np.mean(x_arr, axis=axis, keepdims=True)
    denominator = np.std(x_arr, axis=axis, keepdims=True) + eps

    return numerator / denominator