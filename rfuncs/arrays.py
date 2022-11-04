import numpy as np

def c(*args):
    return np.array([x for x in args])

def length(array):
    return len(array)

def matrix(array, nrow=1, ncol=1, byrow=False):
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

def seq(lower, upper, length=None):
    if length:
        step = (upper - lower) / length
        return np.linspace(lower, upper, num=length, endpoint=False)
    return np.arange(lower, upper+1)


def dim(array):
    return array.shape
