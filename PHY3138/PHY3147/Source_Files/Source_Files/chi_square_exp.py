import numpy as np
from Chi_Squared_Exp import chi_squared

theta_vals = []
R_vals = []
x_err = []
y_err = [] 

fptr = open("0.1phi0_100RH.dat", "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data = result.split( )
    for i in range(0, len(data)):
        if i == 0:
            theta_vals.append(float(data[i]))
        elif i == 1:
            R_vals.append(float(data[i]))
        elif i == 2:
            x_err.append(7.85e-6) # initiall setting the x-error bars equal to 7.85e-3
        elif i == 3:
            y_err.append(8e-3) # initially setting the y-error bars equal to 1
       
fptr.close()

def func(x, a): # the model function that we pass into curve_fit() - in this case a quadratic curve
        return a * (x ** 2) + 6365.5

# Initial guess.
wini = np.array([2150])

chi_squared(func, theta_vals, R_vals, x_err, y_err, wini) # x_err, y_err, wini)