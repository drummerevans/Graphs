import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

# declaring empty lists for the calibrated values
x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

fptr = open("five_slits.txt", "r", newline=None)

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
        elif i == 3:
            err_vert.append(float(datum[i]))

fptr.close()

plt.rc('font', family = 'serif', serif = 'cmr10')
plt.rcParams['mathtext.fontset'] = "cm" 
# plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales 
plt.rcParams["axes.linewidth"] = 1.0

# plt.title("XX Cygni Uncalibrated Magnitudes", fontsize = 12, fontweight = "bold")
plt.xlabel("Position $x$ (m)", fontsize = 12)
plt.ylabel("Intensity $I$", fontsize = 12)
# plt.legend(loc = "lower right", title = "Legend", fontsize = 10)
plt.axis([-0.1, 0.1, 0.00, 1.05])
# plt.xlim(-0.5, 3.0)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(12.5, 11.5)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.errorbar(x_vals, y_vals, err_vert, err_horiz, fmt = "r.", capsize = 4, elinewidth = 0.1, markeredgewidth = 0.3, markerfacecolor = "none", markersize = 7, LineStyle = "none")
# plt.errorbar(x_vals, y_vals, err_vert, fmt = "r.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")
# plt.plot(x_vals, y_vals, "r.", markeredgewidth = 0.4)

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("Five_Slits.pdf") # change the name of the output graph pdf file here!