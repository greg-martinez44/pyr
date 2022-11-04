import numpy as np

SEED = None

def set_seed(new_seed):
    global SEED
    SEED = new_seed

def rnorm(size, mean=0, sd=1):
    return np.random.default_rng(SEED).normal(loc=mean, scale=sd, size=size)
