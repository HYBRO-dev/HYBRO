import abc
from pyhybro.problem import Problem


class InitializerBase(abc.ABC):
    """Base class of the Initializers"""

    def __init__(self,
                 options: dict = None):
        if options is None:
            self.options = self.get_default_options()

    @abc.abstractmethod
    def get_default_options(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reference_set(self,
                 problem: Problem,
                 n_reference_set: int):
        raise NotImplementedError
