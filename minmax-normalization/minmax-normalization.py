import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    x_arr = np.array(X, dtype=float)

    numerator = x_arr - np.min(x_arr, axis=axis, keepdims=True)
    denominator = np.maximum(np.max(x_arr, axis=axis, keepdims=True) - np.min(x_arr, axis=axis, keepdims=True), eps)
    norm = numerator / denominator

    return norm
