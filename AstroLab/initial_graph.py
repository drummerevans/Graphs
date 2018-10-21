import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

fptr = open("initial_results.txt", "r", newline=None)

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
            err_vert.append(float(datum[i]))

trundles = [i ** 3 for i in range(1, 11)]

fptr2 = open("cyg_ucerrors.txt", "w")

print(err_vert)
for item in err_vert:
    fptr2.write(str(item) + "\n")

fptr2.close()

fptr.close()




# plt.errorbar(x_vals, y_vals, err_vert, fmt = "r+", capsize = 3, elinewidth = 0.8, markeredgewidth = 0.8, LineStyle = "none")
plt.plot(x_vals, y_vals, 'r+')
plt.savefig("First_graph1.pdf")