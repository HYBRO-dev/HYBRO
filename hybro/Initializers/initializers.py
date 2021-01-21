from pyDOE import lhs
from hybro.problem import Problem
from hybro.initializer_base import InitializerBase
import random
import warnings


class LhsInitializer(InitializerBase):
    """Latin Hypercube Initializer"""

    def __init__(self,
                 options: dict = None):
        if options is None:
            self.options = self.get_default_options()
        self.reference_set = RefSet()

    def get_default_options(self):
        return {'criterion': 'center'}

    def get_reference_set(self,
                 problem: Problem,
                 n_reference_set: int):
        samples = lhs(len(problem.lb), samples=n_reference_set, criterion=self.options['criterion'])
        for i in range(samples.shape[0]):
            reference_set.add(ReferenceSetMember(x=sample[i, :]))
        return reference_set


class EssInitializer(InitializerBase):
    """Ess Initializer"""

    def __init__(self,
                 options: dict = None):
        if options is None:
            self.options = self.get_default_options()
        self.diversity_set = RefSet()
        self.remaining_members = None

    def get_default_options(self):
        return{'criterion': 'center',
               'n_diversity_set': None,
               'n_reference_set': None}

    def get_reference_set(self,
                 problem: Problem,
                 n_reference_set: Union[int, None]):
        n_par = len(problem.lb)
        if 'n_diversity_set' not in self.options.keys() or
            isinstance(self.options['n_diversity_set'], None):
            self.options['n_diversity_set'] = 10*n_par
        if 'n_reference_set' not in self.options.keys() or
            isinstance(self.options['n_reference_set'], None):
            roots = np.roots(1 - 1 - 10*n_par)
            self.options['n_reference_set'] = np.ceil(roots[roots>0]/2.)*2
        if self.options['n_reference_set'] > self.options['n_diversity_set']:  # PL: validity of the options should be set elsewhere.
            warnings.warn('Setting n_diversity_set to n_reference_set')
            self.options['n_diversity_set'] = self.options['n_reference_set']
        samples = lhs(len(problem.lb), samples=n_diversity_set, criterion=self.options['criterion'])
        for i in range(samples.shape[0]):
            diversity_set.add(ReferenceSetMember(x=sample[i, :]))  # PL: Question: or shall we use setitem? 
        diversity_set = diversity_set.parallel_evaluate()  # PL: Question: Shall we add this method to ReferenceSet?
        diversity_set = diversity_set.sort(key=ReferenceSetMember.get_fval)

        reference_set = diversity_set[0:self.options['n_reference_set']/2]
        self.remaining_members = list(range(self.options['n_reference_set']/2,
                                            self.options['n_diversity_set']))
        random_sample = random.sample(self.remaining_members, self.options['n_reference_set']/2)
        for i in random_sample:
            reference_set.add(diversity_set[i])
            self.remaining_members.remove(i)
        return reference_set

    def resample_one():
        if self.remaining_members:
            i = random.choice(self.remaining_members)
            self.remaining_members.remove(i)
            return self.diversity_set[i]
        else:
            return np.random(len(problem.lb))*(self.problem.ub-self.problem.lb)+self.problem.lb
