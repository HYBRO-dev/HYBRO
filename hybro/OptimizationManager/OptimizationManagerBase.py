"""
Base class for the Optimization Strategy.
The Optimization Strategy schedules which type of optimization is done in which order.
"""
import abc

from hybro import Problem
from hybro.OptimizationResult import OptimizationResult, ReferenceSet
from hybro.optimizer_base import OptimizerBase


class OptimizationManagerBase(abc.ABC):
    """Base class of the  OptimizationManagers"""

    def __init__(self,
                 reference_set: ReferenceSet):
        self.reference_set = reference_set

    def minimize(self,
                 problem: Problem,
                 reference_set: ReferenceSet) -> OptimizationResult:
        """
        minimizes
        """

        # TODO: Create an optimization result object
        optimization_result = None # OptimizationResult(...)

        while not self.check_termination():

            # TODO update optimization result object

            optimizer = self.get_next_optimizer()
            optimizer.minimize(optimization_result)

    def get_next_optimizer(self,
                           optimization_result: OptimizationResult = None
                           ) -> OptimizerBase:
        raise NotImplementedError

    def check_termination(self,
                          optimization_result: OptimizationResult = None
                          ) -> bool:
        raise NotImplementedError
