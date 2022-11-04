import numpy as np

def exp(arr, exp):
    return np.power(arr, exp)

def sqrt(arr):
    return np.sqrt(arr)

def cor(x, y):
    return np.corrcoef(x, y)[0][1]

def mean(arr):
    return np.mean(arr)

def var(arr):
    return np.var(arr)

def sd(arr):
    return np.std(arr)
