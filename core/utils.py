
from __future__ import absolute_import, division, print_function
from numpy.random import RandomState
import numpy as np

try:
    from types import NoneType
except ImportError:  # indicates it's python 3
    NoneType = type(None)  # NoneType is not around in Python 3
    long = int  # there's no long in python 3

__all__ = [
    'assert_is_type',
    'assert_valid_percent',
    'get_random_state'
]

def assert_is_type(x, t):
    if not isinstance(x, t):
        raise TypeError('expected %r but got type=%s'
                        % (t, type(x)))
    return x


def assert_valid_percent(x, eq_lower=False, eq_upper=False):
    # these are all castable to float
    assert_is_type(x, (float, np.float, np.int, int, long, np.long))
    x = float(x)

    # test lower bound:
    if not ((eq_lower and 0. <= x) or ((not eq_lower) and 0. < x)):
        raise ValueError('Expected 0. %s x, but got x=%r'
                         % ('<=' if eq_lower else '<', x))
    if not ((eq_upper and x <= 1.) or ((not eq_upper) and x < 1.)):
        raise ValueError('Expected x %s 1., but got x=%r'
                         % ('<=' if eq_upper else '<', x))
    return x


def get_random_state(random_state):
    # if it's a seed, return a new seeded RandomState
    if isinstance(random_state, (int, np.int, long, np.long, NoneType)):
        return RandomState(random_state)
    # if it's a RandomState, it's been initialized
    elif isinstance(random_state, RandomState):
        return random_state
    else:
        raise TypeError('cannot seed new RandomState with type=%s'
                        % type(random_state))
