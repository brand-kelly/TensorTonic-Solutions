import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a_arr = np.array(a, dtype=float)
    b_arr = np.array(b, dtype=float)
    a_norm = np.linalg.norm(a_arr)
    b_norm = np.linalg.norm(b_arr)
    if a_norm == 0 or b_norm == 0:
        return 0.0
        
    cos_sim = np.dot(a_arr, b_arr) / (a_norm * b_norm)

    return cos_sim