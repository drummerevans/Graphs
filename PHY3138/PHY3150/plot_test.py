import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

def plotter(source_file, col1, col2):

    # file1 = input("Enter in the first file you would like to read data from: ")
    fptr = open(source_file, "r", newline=None)

    list_of_results = fptr.readlines()

    data  = []

    for result in list_of_results:
        datum = result.split( )
        for i in range(0, len(datum)):
            if i == 0:
                col1.append(float(datum[i]))
            elif i == 1:
                col2.append(float(datum[i]))

    fptr.close()


# declaring empty lists for the data values
altitude = []
roll_ang = []

file_name = input("Enter in the file you would like to read data from: ")
plotter(file_name, altitude, roll_ang)

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

# plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-0.005, 0.075)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(6365, 6380)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
#plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(altitude, roll_ang, Marker = ".", color = "r", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "Data Points")

plt.xlabel("Altitude ($'$)", fontsize = 12)
plt.ylabel("Roll Angle ($\\degree$)", fontsize = 12)
plt.legend(loc = "lower right", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("roll_plot.pdf") # change the name of the output graph pdf file here!