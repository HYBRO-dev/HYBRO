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
                 grad: Union[Callable, bool] = False,
                 hess: Union[Callable, bool] = False,
                 lb: Union[np.ndarray, List[float]] = None,
                 ub: Union[np.ndarray, List[float]] = None):
        """
        The problem contains the objective function and optimization bounds.
        """

        self._fun = fun
        self._grad = grad
        self._hess = hess

        # stores if the objective is evaluated simultaneously
        # or given within separate functions.
        self._simultaneous_objective = isinstance(grad, bool)

        self._lb = lb
        self._ub = ub

    def __call__(self,
                 x: Union[np.ndarray, List[float]],
                 derivative_order: tuple = (0, ))->tuple:
        """
        Implements the functionality to compute the derivatives in a
        simultaneous way. Returns a tuple with all derivatives, that
        are in derivative_order

        Parameters:
        -----------

        x:
            point, at which the objective shall be evaluated.
        derivative_order:
            Tuple, that contains
                - 0, if the function shall be evaluated,
                - 1, if the gradient shall be evaluated,
                - 2, if the hessian shall be evaluated.
        """
        if (1 in derivative_order and not self._grad)\
                or (2 in derivative_order and not self._hess):
            raise ValueError(f'Derivative order {derivative_order} contains '
                             f'not supported derivatives.')

        # case 1) objective already returns simultaneous fun/grad/hess values
        if self._simultaneous_objective:
            objective_evaluation = self._fun(x)
            return tuple([objective_evaluation[i]
                          for i in range(3) if i in derivative_order])

        # case 2) generate a tuple with all of the desired values by hand.
        else:
            return tuple([f(x)
                          for i, f in enumerate([self._fun,
                                                 self._grad,
                                                 self._hess])
                          if i in derivative_order])


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
