"""
Stores the reference set and meat information of the hybrid optimization run.
"""
from .reference_set import ReferenceSet


class OptimizationResult:
    """
    Stores result of the hybrid optimization run.
    """

    def __init__(self,
                 reference_set: ReferenceSet):

        self.reference_set = reference_set
        self.n_fval = 0
        self.n_grad = 0
        self.n_hess = 0

    def sort_reference_set(self):
        """
        Sorts the reference set by function value, from smallest to largest.
        """
        return self.reference_set.sort(key=ReferenceSetMember.get_x)
