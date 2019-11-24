import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics


# declaring empty lists for the data values
theta_data = []
R_data = []
theta_errs = [] 
R_errs = []


data_file = input("Now enter in the file with the data points to read from: ")
fptr6 = open(data_file)

list_of_results6 = fptr6.readlines()

data6  = []

for result in list_of_results6:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            theta_data.append(float(datum[i]))
        elif i == 1:
            R_data.append(float(datum[i]))
        # elif i == 2:
        #     theta_errs.append(float(datum[i]))
        # elif i == 3:
        #     R_errs.append(float(datum[i]))

fptr6.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-0.005, 0.075)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(6365, 6384)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(3))
plt.gca().tick_params(width = 1.0, labelsize = 9)


plt.plot(theta_data, R_data, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "Data Values")

plt.xlabel("$\\theta$ (rad)", fontsize = 12)
plt.ylabel("R (km)", fontsize = 12)
plt.legend(loc = "lower right", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("aug26_scatter_0.5_plot.pdf") # change the name of the output graph pdf file here!