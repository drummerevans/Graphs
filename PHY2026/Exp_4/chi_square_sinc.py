import numpy as np
from Chi_Squared_Sinc import chi_squared

x_vals = []
y_vals = []
x_err = []
y_err = [] 

fptr = open("single_1.0mm_0.04.txt", "r", newline = None)

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

def func(x, a): # the model function that we pass into curve_fit() - in this case a straight line
        # return a * (x ** 2) + b * x + c
        return (np.sinc(a * (0.04e-3 / 0.5) * x))**2

# Initial guess.
wini = np.array([1.5e6])

chi_squared(func, x_vals, y_vals, x_err, y_err, wini)