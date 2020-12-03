"""
Defines the problem class.
"""
import numpy as np
from typing import Callable, Union, List


class Problem:
    """
    Optimization Problem.
    """

    def __init__(self,
                 fun: Callable,
                 grad: Callable = None,
                 hess: Callable = None,
                 lb: Union[np.ndarray, List[float]] = None,
                 ub: Union[np.ndarray, List[float]] = None):

        self._fun = fun
        self._grad = grad
        self._hess = hess,
        self._lb = lb
        self._ub = ub

    @property
    def fun(self):
        return self._fun

    @property
    def grad(self):
        return self._grad

    @property
    def hess(self):
        return self._hess

    @property
    def lb(self):
        return self._lb

    @property
    def ub(self):
        return self._ub

    @property
    def has_grad(self):
        return self._grad is None

    @property
    def has_hess(self):
        return self._hess is None

    @property
    def has_lb(self):
        return self._lb is None

    @property
    def has_ub(self):
        return self._ub is None

    def check_in_bounds(self,
                        x: Union[np.ndarray, List[float]]):
        """
        Checks, if x is within the bounds of the optimization problem.
        """

        if self.has_lb and np.any(np.less(x, self._lb)):
            return False

        elif self.has_ub and np.any(np.less(self._ub, x)):
            return False

        else:
            return True
