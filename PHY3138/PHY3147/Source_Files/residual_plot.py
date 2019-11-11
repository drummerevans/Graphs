import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

# declaring empty lists for the dry 0.00 values
theta_vals = []
R_vals = []
n_vals = [] 
z_vals = []

# declaring empty lists for the residuals
residuals = []


file1 = input("Enter in the first file you would like to read data from: ")
fptr = open(file1, "r", newline=None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            theta_vals.append(float(datum[i]))
        elif i == 1:
            R_vals.append(float(datum[i]))
        elif i == 2:
            n_vals.append(float(datum[i]))
        elif i == 3:
            z_vals.append(float(datum[i]))

fptr.close()

file2 = input("Enter in the first file you would like to read the residuals from: ")
fptr2 = open(file2, "r", newline=None)

list_of_results2 = fptr2.readlines()

data2  = []

for result2 in list_of_results2:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            residuals.append(float(datum[i]))
       

fptr2.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-0.005, 0.075)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(6365, 6384)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(3))
plt.gca().tick_params(width = 1.0, labelsize = 9)


plt.plot(residuals, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "Residuals")

plt.xlabel("$\\theta$ (rad)", fontsize = 12)
plt.ylabel("data - model", fontsize = 12)
plt.legend(loc = "lower right", title = "Legend", fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("aug26_0.575phi0_residuals.pdf") # change the name of the output graph pdf file here!