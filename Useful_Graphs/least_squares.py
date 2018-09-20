import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics
from LS_Polynomials.LS_Poly import least_squares_fit

x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

fptr = open("test_data.txt", "r", newline=None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            x_vals.append(float(datum[i]))
        elif i == 1:
            y_vals.append(float(datum[i]))
        elif i == 2:
            err_horiz.append(float(datum[i]))
        else:
            err_vert.append(float(datum[i]))

fptr.close()

print(x_vals)

# x_vals = np.array([0, 1, 2, 3, 4, 5])
# y_vals = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
# err_horiz = np.array([0.2, 0.1, 0.5, 0.3, 0.1, 0.2]) 
# err_vert = np.array([0.2, 0.1, 0.5, 0.3, 0.1, 0.2]) 

least_squares_fit(x_vals, y_vals, err_horiz, err_vert) # calling the function to plot the graph