import numpy as np
from least_squares_line import least_squares
from chi_square_line import chi_squared

x_vals = []
y_vals = []
x_err = []
y_err = [] 

fptr = open("magnetic.txt", "r", newline = None)

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
            y_err.append(float(data[i]))
       
fptr.close()

def func(x, a, b): # the model function that we pass into curve_fit() - in this case a straight line
        return a * x + b

# Initial guess.
wini = np.array([-0.00003, 3.62e-11])

least_squares(func, x_vals, y_vals, y_err, wini)
chi_squared(func, x_vals, y_vals, y_err, wini)
