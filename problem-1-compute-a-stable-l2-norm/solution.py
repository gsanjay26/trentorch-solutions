import numpy as np

def solve(x):
    x = np.asarray(x, dtype=float)
    m = np.max(np.abs(x))
    if m == 0:
        return 0.0
    return m * np.sqrt(np.sum((x / m) ** 2))
