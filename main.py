from data_input import get_data
from degree_detection import detect_degree
import numpy as np
import matplotlib.pyplot as plt
from analysis import analyze_polynomial



x, y = get_data()
degree = detect_degree(y)
coeffs = np.polyfit(x, y, degree)
coeffs = np.round(coeffs, 10)
y_pred = np.polyval(coeffs, x)
y_pred = np.round(y_pred, 10)
plt.scatter(x, y, label="Data Points") # dots representing the original data points
plt.plot(x, y_pred, label="Fitted Polynomial") # line representing the computation
plt.xlabel("x") # label for x-axis
plt.ylabel("y")# label for y-axis
plt.title("Polynomial Fit")# title of the plot
plt.legend()# legend to differentiate between data points and fitted polynomial
plt.show()# renders the plot on the screen
print("Predicted y:", y_pred)
print(f"Detected degree: {degree}")      
print(f"Coefficients: {coeffs}")
print(f"Polynomial: {np.poly1d(coeffs)}")
analyze_polynomial(coeffs)





#numpy functions are positional-argument order must be correct. numpy functions expect arguments in fixed order











