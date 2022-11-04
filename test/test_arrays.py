import numpy as np
import pytest

from rfuncs import *

def test_c_creates_n_array():
    expected = np.array([1, 2, 3])
    actual = c(1, 2, 3)

    assert (expected == actual).all()

def test_length_gives_correct_length_of_array():
    expected_array = np.array([1, 2, 3])
    expected_length = len(expected_array)

    actual = c(1, 2, 3)
    actual_length = length(actual)

    assert expected_length == actual_length

@pytest.mark.parametrize("ref_test", [
    ([[1, 3], [2, 4]], matrix(c(1, 2, 3, 4), nrow=2, ncol=2)),
    ([[4, 2], [5, 9]], matrix(c(4, 5, 2, 9), nrow=2, ncol=2)),
    ([[4, 2, 3], [6, 9, 8]], matrix(c(4, 6, 2, 9, 3, 8), nrow=2, ncol=3)),
    ([[8, 9], [7, 5], [1, 2]], matrix(c(8, 7, 1, 9, 5, 2), nrow=3, ncol=2)),
    ([[5, 8, 9], [3, 4, 7], [1, 2, 6]], matrix(c(5, 3, 1, 8, 4, 2, 9, 7, 6), nrow=3, ncol=3))
])
def test_matrix_creates_multiindex_array(ref_test):
    expected_array, actual_matrix = ref_test

    assert (expected_array == actual_matrix).all()

@pytest.mark.parametrize("ref_test", [
    ([[1, 2], [3, 4]], c(1, 2, 3 ,4)),
    ([[5, 6], [7, 8]], c(5, 6, 7, 8)),
    ([[2, 1, 3], [5, 6, 8]], c(2, 1, 3, 5, 6, 8))
])
def test_matrix_creates_multiindex_array_by_rows(ref_test):
    expected_array, actual_array = ref_test
    rows = 2
    cols = 2
    if len(actual_array) > 4:
        cols = 3

    actual_matrix = matrix(actual_array, nrow=rows, ncol=cols, byrow=True)
    assert (expected_array == actual_matrix).all()

def test_matrix_operations_with_sqrt():
    expected_input = [[1, 3], [2, 4]]
    expected_output = [[1.00, 1.73205], [1.41, 2.00]]

    actual_matrix = matrix(c(1, 2, 3, 4), nrow=2, ncol=2)
    actual_sqrt = sqrt(actual_matrix)

    np.testing.assert_allclose(actual_sqrt, expected_output, rtol=0.01)

    assert (actual_matrix == expected_input).all()

@pytest.mark.parametrize("power", [2, 3, 1.5])
def test_matrix_operations_with_exp(power):
    expected_input = [[1, 3], [2, 4]]
    expected_output = [
        [1**power, 3**power],
        [2**power, 4**power]
    ]

    actual_matrix = matrix(c(1, 2, 3, 4), nrow=2, ncol=2)
    actual_squared = exp(actual_matrix, power)

    np.testing.assert_allclose(actual_squared, expected_output)

def test_seq_builds_inclusive_range():
    expected_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    actual_array = seq(1, 10)

    assert (expected_array == actual_array).all()

@pytest.mark.parametrize("expected_values", [
    (10, (0, 1), np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])),
    (5, (6, 9), np.array([6.0, 6.6, 7.2, 7.8, 8.4]))
])
def test_seq_builds_evenly_spaced_arrays_of_given_length(expected_values):
    length, steps, expected_array = expected_values
    lower, upper = steps
    actual_array = seq(lower, upper, length=length)

    np.testing.assert_allclose(actual_array, expected_array, rtol=0.01)

@pytest.mark.parametrize("ref_test", [
    ([[1, 3, 2], [2, 1, 3]], matrix(c(1, 2, 3), nrow=2, ncol=3)),
    ([[1, 2, 3], [1, 2, 3]], matrix(c(1, 2, 3), nrow=2, ncol=3, byrow=True)),
    ([[1, 1], [2, 2], [3, 3]], matrix(c(1,2,3), nrow=3, ncol=2)),
    ([[1, 2], [3, 1], [2, 3]], matrix(c(1,2,3), nrow=3, ncol=2, byrow=True))
])
def test_matrix_repeats_data_when_input_array_is_too_short(ref_test):
    expected_matrix, actual_matrix = ref_test

    assert (expected_matrix == actual_matrix).all()

@pytest.mark.parametrize("ref_test", [
    (c(1, 2, 3), (3,)),
    (matrix(c(1,2,3,4), nrow=2, ncol=2), (2, 2)),
    (matrix(c(1, 2, 3, 4, 5 ,6), nrow=2, ncol=3), (2, 3)),
    (matrix(c(1, 2, 3, 4, 5, 6), nrow=3, ncol=2), (3, 2))
])
def test_dim_returns_size_of_array_or_matrix(ref_test):
    expected_array, expected_size = ref_test
    actual_size = dim(expected_array)

    assert expected_size == actual_size
