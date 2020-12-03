"""
Implements the Reference Set.
"""

from typing import List
import numpy as np


class ReferenceSetMember:
    """
    Instance of the ReferenceSet
    """
    def __init__(self,
                 x: np.ndarray,
                 fval: float,
                 grad: np.ndarray = None,
                 hess: np.ndarray = None):

        self._x = x
        self._fval = fval
        self._grad = grad
        self._hess = hess

    def get_x(self):
        return self._x

    def get_fval(self):
        return self._fval

    def get_grad(self):
        return self._grad

    def get_hess(self):
        return self._hess


class ReferenceSet:
    """
    Set of Reference Points that are handed to the global/local optimizers.
    """

    def __init__(self,
                 reference_set: List[ReferenceSetMember]):

        self._reference_set = reference_set

    def __getitem__(self, item):
        """This function makes the Reference Set index-able."""
        return self._reference_set[item]

    def __setitem__(self, key, value):
        self._reference_set[key] = value

    def __len__(self):
        return len(self._reference_set)



