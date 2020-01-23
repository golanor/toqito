from numpy import linalg as LA
import numpy as np


def is_pure(state: np.ndarray) -> bool:
    """
    Determines if a given quantum state is pure.

    :param state: The density matrix representing the quantum state.
    :return: True if state is pure and False otherwise.
    """
    eigs, _ = LA.eig(state)
    return np.isclose(np.max(np.diag(eigs)), 1)