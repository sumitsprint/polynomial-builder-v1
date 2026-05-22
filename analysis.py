import numpy as np

def group_roots(real_roots, tolerance=1e-5):
    grouped = []
    for root in real_roots:
        if len(grouped) == 0:
            grouped.append([root, 1])
        else:
            last_root = grouped[-1][0]
            if abs(root - last_root) < tolerance:
                grouped[-1][1] += 1
            else:
                grouped.append([root, 1])

    return grouped
                

    



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

    if degree % 2 == 0:

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

    grouped_roots = group_roots(real_roots)

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

    def evaluate(x):

        return np.polyval(coeffs, x)

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

    print(grouped_roots)    





if __name__ == "__main__":
    coeffs = [1, 0, -1]  # x² - 1
    analyze_polynomial(coeffs)
