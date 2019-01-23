import numpy as np
from chi_square_exp import chi_squared3

x_vals = []
y_vals = []
y_err = [] 

fptr = open("part2_data.txt", "r", newline = None)

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
        return a * np.exp(bx) + c

# Initial guess.
wini = np.array([2, 0.5, 0.05])

print(x_vals)

chi_squared3(func, x_vals, y_vals, y_err, wini)