import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param_arr = np.array(param)
    grad_arr = np.array(grad)
    m_arr = np.array(m)
    v_arr = np.array(v)
    # Write code here
    m_new = beta1 * m_arr + (1 - beta1) * grad_arr
    v_new = beta2 * v_arr + (1 - beta2) * (grad_arr ** 2)
    m_hat = m_new / (1 - beta1 ** t)
    v_hat = v_new / (1 - beta2 ** t)

    param_new = param_arr - (lr * m_hat) / (np.sqrt(v_hat) + eps)

    return param_new, m_new, v_new