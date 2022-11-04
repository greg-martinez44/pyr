from typing import Optional, Tuple
import numpy as np

def c(*args: int) -> np.ndarray:
    """Creates an array from a sequence of integers."""
    return np.array([x for x in args])

def length(array: np.ndarray) -> int:
    """Returns the length of an array."""
    return len(array)

def matrix(array: np.ndarray, nrow:int=1, ncol:int=1, byrow:bool=False) -> np.ndarray:
    """Creates a nrow x ncol matrix from a given array."""
    array_length = nrow * ncol
    if len(array) < array_length:
        array = np.tile(array, array_length+len(array))
    matrix = []
    for i in range(nrow):
        this_row = []
        for j in range(ncol):
            try:
                if byrow:
                    this_row.append(array[(i*ncol) + j])
                else:
                    this_row.append(array[i + (j*nrow)])
            except IndexError:
                return "Too many columns or rows"
        matrix.append(this_row)
    return np.asarray(matrix)

def seq(lower:int, upper:int, length:Optional[int]=None) -> np.ndarray:
    """Creates an array with values from lower to upper."""
    if length:
        step = (upper - lower) / length
        return np.linspace(lower, upper, num=length, endpoint=False)
    return np.arange(lower, upper+1)


def dim(array:np.ndarray) -> Tuple[int]:
    """Returns the shape of the array."""
    return array.shape
