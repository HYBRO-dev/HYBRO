import abc
from hybro.OptimizationResult import OptimizationResult
from hybro.problem import Problem


class OptimizerBase(abc.ABC):
    """Base class of the Optimizers"""

    def __init__(self,
                 options: dict = None):

        if options is None:
            self.options = self.get_default_options()

    @abc.abstractmethod
    def get_default_options(self):
        raise NotImplementedError

    @abc.abstractmethod
    def minimize(self,
                 problem: Problem,
                 optimization_result: OptimizationResult):

        raise NotImplementedError
