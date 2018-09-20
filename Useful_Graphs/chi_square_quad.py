import numpy as np
from Chi_Squared_Fit.Least_Squares_Quadratic import least_squares
from Chi_Squared_Fit.Chi_Squared_Quadratic import chi_squared

x_vals = []
y_vals = []
x_err = []
y_err = [] 

fptr = open("air_data.txt", "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data = result.split( )
    for i in range(0, len(data)):
        if i == 0:
            x_vals.append(float(data[i]))
        elif i == 1:
            y_vals.append(float(data[i]))
        elif i == 2:
            x_err.append(float(data[i]))
        elif i == 3:
            y_err.append(float(data[i]))
       
fptr.close()

def func(x, a, b, c): # the model function that we pass into curve_fit() - in this case a straight line
        return a * (x ** 2) + b * x + c

# Initial guess.
wini = np.array([2.0, -1.8, 0.4])

least_squares(func, x_vals, y_vals, x_err, y_err, wini)
chi_squared(func, x_vals, y_vals, x_err, y_err, wini)
