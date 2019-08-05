import numpy as np
from Chi_Squared_Sqrt import chi_squared

x_vals = []
y_vals = []
y_err = [] 

fptr = open("test2.txt", "r", newline = None)

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
        return a * x + b * np.sqrt(x)

# Initial guess.
wini = np.array([30.0, 60.4])

chi_squared(func, x_vals, y_vals, y_err, wini)