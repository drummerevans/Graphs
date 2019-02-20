import numpy as np
from wave_speed_plot import chi_squared

x_vals = []
y_vals = []
y_err = [] 

fptr = open("speed_data.txt", "r", newline = None)

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
wini = np.array([0.4, 1.8])

chi_squared(func, x_vals, y_vals, y_err, wini)