import pytest

from rfuncs import *

def test_cor_returns_a_single_value():
    x = rnorm(size=30, mean=10, sd=0.2)
    y = x+rnorm(size=30, mean=10, sd=0.2)
    actual_cor = cor(x, y)

    assert isinstance(actual_cor, float)

@pytest.mark.parametrize("mean", [10, 50, 30])
def test_cor_is_bound_between_neg1_and_1(mean):
    x = rnorm(size=30)
    y = x+rnorm(size=30, mean=mean, sd=0.2)
    actual_cor = cor(x, y)

    assert -1.0 <= actual_cor and actual_cor <= 1.0

@pytest.mark.parametrize("expected_array", [
    c(1, 2, 3, 4),
    matrix(c(1, 2, 3, 4), nrow=2, ncol=2)
])
def test_mean_returns_a_single_float(expected_array):
    actual_mean = mean(expected_array)

    assert isinstance(actual_mean, float)

def test_mean_returns_mean_of_vector():
    expected_array = c(1, 2, 3, 4)
    expected_mean = (1 + 2 + 3 + 4) / 4
    actual_mean = mean(expected_array)

    assert expected_mean == actual_mean

def test_mean_returns_approx_mean_of_rnorm():
    expected_array = rnorm(50, mean=30)
    expected_mean = 30
    actual_mean = mean(expected_array)

    assert expected_mean == pytest.approx(actual_mean, 0.1)

def test_var_returns_variance_of_vector():
    expected_array = c(1, 2, 3, 4)
    expected_variance = mean(abs(expected_array - mean(expected_array))**2)
    actual_variance = var(expected_array)

    assert expected_variance == pytest.approx(actual_variance, 0.1)

def test_sd_returns_standard_deviation_of_a_vector():
    expected_array = c(1, 2, 3, 4)
    expected_sd = sqrt(var(expected_array))
    actual_sd = sd(expected_array)

    assert expected_sd == pytest.approx(actual_sd, 0.1)
