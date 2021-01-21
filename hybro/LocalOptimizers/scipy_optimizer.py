"""
Implements the interface to scipys local optimizer
"""
from typing import List
from scipy.optimize import minimize

from hybro import OptimizerBase, Problem
from hybro.OptimizationResult import OptimizationResult, ReferenceSet


class ScipyLocalOptimizer(OptimizerBase):
    """
    Implements an interface to the scipys local optimizers.
    """

    def __init__(self,
                 options: dict = None):

        super().__init__()

        if options is None:
            options = self.get_default_options()

        self.options = options

    def minimize(self,
                 problem: Problem,
                 optimization_result: OptimizationResult) -> OptimizationResult:

        pass

    def get_default_options(self):
        return {'method': 'L-BFGS-B',
                'maxiter': 1000}
