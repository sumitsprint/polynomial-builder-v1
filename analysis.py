import numpy as np


def analyze_polynomial(coeffs):

    # Degree of polynomial
    # Example:
    # [1, 0, -1] -> x² - 1 -> degree 2
    degree = len(coeffs) - 1

    # First coefficient is the leading coefficient
    leading_coeff = coeffs[0]

    # ---------------------------------------------------
    # END BEHAVIOR
    # ---------------------------------------------------
    # Even degree:
    #   both ends same direction
    #
    # Odd degree:
    #   ends opposite directions
    #
    # Leading coefficient decides up/down orientation
    # ---------------------------------------------------
    if degree == 0:
        end_behavior = f"horizontol line at y = {leading_coeff}"

    elif degree % 2 == 0:

        # Even degree

        if leading_coeff > 0:
            end_behavior = "both up"

        else:
            end_behavior = "both down"

    else:

        # Odd degree

        if leading_coeff > 0:
            end_behavior = "left down, right up"

        else:
            end_behavior = "left up, right down"

    # ---------------------------------------------------
    # ROOTS
    # ---------------------------------------------------
    # np.roots() returns all roots:
    # real + complex
    #
    # We only keep real roots for v1
    # ---------------------------------------------------

    roots = np.roots(coeffs)

    # Keep only real roots
    real_roots = roots[np.isreal(roots)].real

    # Sort roots left -> right
    real_roots = np.sort(real_roots)
    def evaluate(x):

        return np.polyval(coeffs, x)

    # if no real root exist
    if len(real_roots) == 0:
        intervals = [(-np.inf, np.inf)]
        test_points = [0]
        
        value = evaluate(0)
        if value > 0:
            signs = ["positive"]
        else:
            signs = ["negative"]

        sign_behavior = [((-np.inf, np.inf), signs[0])]        
        root_multiplicities = []


    

        



    else:
            
        cleaned_roots = []

        cleaned_roots.append(real_roots[0]) # this line throws error if there are no real roots

        for root in real_roots[1:]:
            last_root = cleaned_roots[-1]
            # if the distance between these 2 roots is less than 0.00001, consider them numerically the same root
            if np.isclose(root, last_root, atol=1e-5):
                continue
            cleaned_roots.append(root)

        real_roots = np.array(cleaned_roots)
        real_roots = np.sort(real_roots)    
        real_roots = [float(root) for root in real_roots]

        

        # ---------------------------------------------------
        # INTERVALS
        # ---------------------------------------------------
        # Example:
        # roots = [-2, 1]
        #
        # intervals:
        # (-inf, -2)
        # (-2, 1)
        # (1, inf)
        # ---------------------------------------------------

        intervals = []

        # Left interval
        intervals.append((-np.inf, real_roots[0]))

        # Middle intervals
        for i in range(len(real_roots) - 1):

            intervals.append(
                (real_roots[i], real_roots[i + 1])
            )

        # Right interval
        intervals.append((real_roots[-1], np.inf))

        # ---------------------------------------------------
        # HELPER FUNCTION
        # ---------------------------------------------------
        # Evaluates polynomial value at x
        # ---------------------------------------------------

        

        # ---------------------------------------------------
        # TEST POINTS
        # ---------------------------------------------------
        # We choose one sample point inside each interval
        #
        # Example:
        # roots = [-2, 1]
        #
        # test points:
        # -3
        # -0.5
        # 2
        # ---------------------------------------------------

        test_points = []

        # Left side point
        test_points.append(real_roots[0] - 1)

        # Midpoints between roots
        for i in range(len(real_roots) - 1):

            midpoint = (
                real_roots[i] + real_roots[i + 1]
            ) / 2

            test_points.append(midpoint)

        # Right side point
        test_points.append(real_roots[-1] + 1)

        # ---------------------------------------------------
        # SIGN DETECTION
        # ---------------------------------------------------
        # Evaluate polynomial at each test point
        #
        # Positive value  -> positive interval
        # Negative value  -> negative interval
        # ---------------------------------------------------

        signs = []

        for point in test_points:

            value = evaluate(point)

            if value > 0:
                signs.append("positive")

            else:
                signs.append("negative")

        # ---------------------------------------------------
        # COMBINE INTERVALS + SIGNS
        # ---------------------------------------------------

        sign_behavior = []

        for interval, sign in zip(intervals, signs):

            sign_behavior.append((interval, sign))


        # multiplicity detection 

        root_multiplicities = []

        for i, root in enumerate(real_roots):
            left_sign = signs[i]
            right_sign = signs[i + 1]
            if left_sign != right_sign:
                multiplicity = "odd"
                behavior = "crosses x-axis"
            else:
                multiplicity = "even"
                behavior = "BOUNCES off x-axis"
            root_multiplicities.append((root, f"multiplicity: {multiplicity}, behavior: {behavior}"))
           



    # ---------------------------------------------------
    # FORMATTED OUTPUT
    # ---------------------------------------------------

    print("\nPolynomial Analysis")
    print("---------------------")

    # Degree parity
    if degree % 2 == 0:
        parity = "even"

    else:
        parity = "odd"

    # Leading coefficient sign
    if leading_coeff > 0:
        leading_sign = "positive"

    else:
        leading_sign = "negative"

    print(f"Degree: {degree} ({parity})")

    print(f"Leading coefficient: {leading_sign}")

    print(f"End behavior: {end_behavior}")

    print(f"Real roots: {real_roots}")

    print("\nSign behavior:")

    for interval, sign in sign_behavior:

        print(f"{interval}: {sign}")

    print("\nRoot multiplicities:")
    for root, multiplicity_info in root_multiplicities:

        print(f"Root: {root}, {multiplicity_info}")
       





if __name__ == "__main__":
    coeffs = [1, 0, 1]  # x³ - 3x + 2
    analyze_polynomial(coeffs)
