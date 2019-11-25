import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

long_data = []
lat_data = []

data_file = input("Enter in the file with the data points to read from: ")
fptr6 = open(data_file)

list_of_results6 = fptr6.readlines()

data6  = []

for result in list_of_results6:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            long_data.append(float(datum[i]))
        elif i == 1:
            lat_data.append(float(datum[i]))
       

fptr6.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

# plt.axis([-0.25, 2.5, 46.0, 50.0])
plt.xlim(-2.5, 1.5)
plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.ylim(46.0, 50.0)
plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(long_data, lat_data, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "Data Values")

plt.xlabel("Longitude ($\\degree$)", fontsize = 12)
plt.ylabel("Latitude ($\\degree$)", fontsize = 12)
plt.legend(loc = "lower right", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("aug26_0.105_long_lat.pdf") # change the name of the output graph pdf file here!