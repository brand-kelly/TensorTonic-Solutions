import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    counts = np.unique(y, return_counts=True)[1]
    N = len(y)
    entropy = 0.0
    for i in range(len(counts)):
        p = counts[i] / N
        if p == 0:
            continue

        entropy += p * np.log2(p)

    entropy *= -1.0
    return entropy