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

# declaring empty lists for the wet 1.00 values
theta_vals2 = []
R_vals2 = []
n_vals2 = [] 
z_vals2 = []

fptr = open("0.1phi0_0RH.dat", "r", newline=None)

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


fptr2 = open("0.1phi0_100RH.dat")

list_of_results2 = fptr2.readlines()

data2  = []

for result in list_of_results2:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            theta_vals2.append(float(datum[i]))
        elif i == 1:
            R_vals2.append(float(datum[i]))
        elif i == 2:
            n_vals2.append(float(datum[i]))
        elif i == 3:
            z_vals2.append(float(datum[i]))

fptr2.close()
fptr.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.axis([-0.1, 2.5, 12.4, 11.4])
plt.xlim(-0.005, 0.075)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
plt.ylim(6365, 6380)
plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(theta_vals, R_vals, Marker = ".", color = "r", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "0% RH")
plt.plot(theta_vals2, R_vals2, Marker = ".", color = "b", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "100% RH")

plt.xlabel("$\\theta$ (rad)", fontsize = 12)
plt.ylabel("R (km)", fontsize = 12)
plt.legend(loc = "lower right", title = "Legend", fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("phi0_0.1_plot.pdf") # change the name of the output graph pdf file here!