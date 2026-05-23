import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
        return np.empty((0,0))

    if max_len is None:
        max_len = len(max(seqs, key=len))


    padded_seqs = np.full((len(seqs), max_len), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        padded_seqs[i, :length] = seq[:length]
    print(padded_seqs)

    return padded_seqs