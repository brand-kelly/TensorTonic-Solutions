import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x_arr = np.array(x)

    relu = np.where(x_arr >= 0, x, alpha * x_arr)

    return relu