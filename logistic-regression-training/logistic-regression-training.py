import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X_arr = np.array(X)
    y_arr = np.array(y).reshape(-1, 1) 
    N = X_arr.shape[0]
    w = np.zeros((X_arr.shape[1], 1))
    b = 0.0

    for step in range(steps):
        inner = X_arr @ w + b
        p = _sigmoid(inner)

        error = p - y_arr
        dw = np.dot(X_arr.T, error) / N
        db = np.sum(error) / N

        w -= lr * dw
        b -= lr * db


    return w.ravel(), float(b)