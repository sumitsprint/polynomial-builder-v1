import numpy as np
def get_data():

    # x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    # y = [100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100]
    # x = [1,2,3,4,5]
    # y = [4,10,12,16,20]
    x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    y = [-1000,-729,-512,-343,-216,-125,-64,-27,-8,-1,0,1,8,27,64,125,216,343,512,729,1000]
    if len(x) < 2:
        raise ValueError("x must have at least two elements to check spacing.")
    diffs = np.diff(x)

    if not np.all(diffs == diffs[0]):  # it will enter if ut is true
        raise ValueError("x values must be equally spaced for finite differences.")
    return np.array(x), np.array(y)




