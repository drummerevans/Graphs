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
timestamp = []
altitude = []
file_name = input("Enter in the file you would like to read data from: ")
plotter(file_name, timestamp, altitude)

# declaring empty lists for the data values
timestamp2 = []
altitude2 = []
file_name2 = input("Enter in the file2 you would like to read data from: ")
plotter(file_name2, timestamp2, altitude2)

# declaring empty lists for the data values
timestamp3 = []
altitude3 = []
file_name3 = input("Enter in the file3 you would like to read data from: ")
plotter(file_name3, timestamp3, altitude3)

# declaring empty lists for the data values
timestamp4 = []
altitude4 = []
file_name4 = input("Enter in the file4 you would like to read data from: ")
plotter(file_name4, timestamp4, altitude4)

# declaring empty lists for the data values
timestamp5 = []
altitude5 = []
file_name5 = input("Enter in the file5 you would like to read data from: ")
plotter(file_name5, timestamp5, altitude5)


plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

# plt.axis([-0.1, 2.5, 12.4, 11.4])
plt.xlim(-1000, 50)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.ylim(0, 10000)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
#plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(timestamp, altitude, Marker = ".", color = "r", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "EI3842_1203")
plt.plot(timestamp2, altitude2, Marker = ".", color = "b", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8207_1228")
plt.plot(timestamp3, altitude3, Marker = ".", color = "g", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8241_1213")
plt.plot(timestamp4, altitude4, Marker = ".", color = "m", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8297_1143")
plt.plot(timestamp5, altitude5, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "U2402_1218")

plt.xlabel("Timestamp $(s)$", fontsize = 12)
plt.ylabel("Altitude $(')$", fontsize = 12)
plt.legend(loc = "lower left", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("altitude_plot.pdf") # change the name of the output graph pdf file here!