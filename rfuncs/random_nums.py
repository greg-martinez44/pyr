import numpy as np

SEED = None

def set_seed(new_seed: int) -> None:
    """Sets the seed for random value generation."""
    global SEED
    SEED = new_seed

def rnorm(size:int, mean:int=0, sd:int=1) -> np.ndarray:
    """Creates a random array of integers with given mean and standard deviation."""
    return np.random.default_rng(SEED).normal(loc=mean, scale=sd, size=size)
