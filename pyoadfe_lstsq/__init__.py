import numpy as np


def lstsq(A, b, rcond = None):
    return np.dot(np.linalg.inv(np.dot(A.T, A)), A.T @ b)
