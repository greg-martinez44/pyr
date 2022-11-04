import numpy as np

def exp(arr:np.ndarray, exp:int) -> np.ndarray:
    """Returns an array with all elements raised to exp."""
    return np.power(arr, exp)

def sqrt(arr:np.ndarray) -> np.ndarray:
    """Returns an array with the square root of each element."""
    return np.sqrt(arr)

def cor(x:np.ndarray, y:np.ndarray) -> np.ndarray:
    """Returns the correlation coefficient from two arrays."""
    return np.corrcoef(x, y)[0][1]

def mean(arr:np.ndarray) -> float:
    """Returns the mean of an array."""
    return np.mean(arr)

def var(arr:np.ndarray) -> float:
    """Returns the variance of an array."""
    return np.var(arr)

def sd(arr:np.ndarray) -> float:
    """Returns the standard deviation of an array."""
    return np.std(arr)
