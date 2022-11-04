import numpy as np
import pytest

from rfuncs import *

seed = 50

@pytest.fixture(autouse=True)
def setup():
    set_seed(seed)

def test_rnorm_output_is_correct_length():
    expected = np.random.default_rng(seed).normal(0, 1, 3)
    actual = rnorm(size=3)

    assert (expected == actual).all()

def test_rnorm_with_different_mean():
    expected = np.random.default_rng(seed).normal(50, 1, 3)
    actual = rnorm(size=3, mean=50)

    assert (expected == actual).all()

def test_rnorm_with_different_std():
    expected = np.random.default_rng(seed).normal(3, 0.3, 3)
    actual = rnorm(size=3, mean=3, sd=0.3)

    assert (expected == actual).all()
