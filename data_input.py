import numpy as np

def validate_spacing(x, y):

    if len(x) < 2:
        raise ValueError("x must have at least two elements to check spacing.")
    diffs = np.diff(x)

    if not np.all(diffs == diffs[0]):  # it will enter if ut is true
        raise ValueError("X values must be equally spaced (e.g. 0, 1, 2, 3, 4).")
    return np.array(x), np.array(y)





