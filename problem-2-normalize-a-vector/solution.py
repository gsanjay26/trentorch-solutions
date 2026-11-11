import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    x=np.asarray(x,dtype=float)
    m=np.max(np.abs(x))
    if(m==0):
        raise ValueError("NO DIRECTION")
    y=x/m
    return y/np.linalg.norm(y)
