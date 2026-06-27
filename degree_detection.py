import numpy as np
def first_difference(y):
    return np.diff(y)

def detect_degree(y):
    if len(y) < 2:
        raise ValueError("not enough data points")
    
    current = y
    degree = 0
    # if np.all(y == 0):
    #     raise ValueError("Zero polynomial has undefined degree.")
    #constant p(x)
    if np.all(y == y[0]):
        return 0
    
    while True:
        diffs = np.diff(current)
        degree += 1
        if np.all(diffs == diffs[0]):
            break
        current = diffs
    return degree







