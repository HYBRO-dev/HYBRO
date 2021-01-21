"""
Tests of the hybro problem class.
"""
import numpy as np
import scipy.optimize as opt
import hybro
import pytest


def test_init():
    """
    Tests the initialization of the hybro problem
    :return:
    """
    test_problem, test_problem_tuple = get_test_problems()


def test_call_problems():
    """
    Tests if both versions of defining the objective gives the same
    when calling the objective.
    """

    test_problem, test_problem_tuple = get_test_problems()

    x = np.ones(5)
    res_1 = test_problem(x, derivative_order=(0, 1, 2))
    res_2 = test_problem(x, derivative_order=(0, 1, 2))

    # check if all values are the same
    for i in range(3):
        assert np.all(np.equal(res_1[i], res_2[i]))


def get_test_problems():
    """
    Generates two test problems.
    :return:
    """
    # test init for separate definition of fun/grad/hess
    test_problem = hybro.Problem(fun=opt.rosen,
                                 grad=opt.rosen_der,
                                 hess=opt.rosen_hess)

    # test init for combined definition of fun/grad/hess
    def aggregate_objective(x):
        return (opt.rosen(x),
                opt.rosen_der(x),
                opt.rosen_hess(x))

    test_problem_tuple = hybro.Problem(fun=aggregate_objective,
                                       grad=True,
                                       hess=True)

    return test_problem, test_problem_tuple
