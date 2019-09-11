import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter # needed to specify the precision of the axes labels i.e. to 1 d.p in this case
import statistics

# declaring empty lists for the uncalibrated values of XX Cygni
x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

# declaring empty lists for the calibration stars
x_vals2 = []
y_vals2 = []
err_horiz2 = [] 
err_vert2 = []

x_vals3 = []
y_vals3 = []
err_horiz3 = [] 
err_vert3 = [] 

x_vals4 = []
y_vals4 = []
err_horiz4 = [] 
err_vert4 = [] 

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



fptr2 = open("uncal1.txt") 

uncalibrated_results1 = fptr2.readlines()

data2  = []

for result in uncalibrated_results1:
    datum2 = result.split( )
    for i in range(0, len(datum2)):
        if i == 0:
            x_vals2.append(float(datum2[i]))
        elif i == 1:
            y_vals2.append(float(datum2[i]))
        elif i == 2:
            err_vert2.append(float(datum2[i]))

fptr3 = open("uncal2.txt") 

uncalibrated_results2 = fptr3.readlines()

data3  = []

for result in uncalibrated_results2:
    datum3 = result.split( )
    for i in range(0, len(datum3)):
        if i == 0:
            x_vals3.append(float(datum3[i]))
        elif i == 1:
            y_vals3.append(float(datum3[i]))
        elif i == 2:
            err_vert3.append(float(datum3[i]))


fptr4 = open("uncal3.txt") 

uncalibrated_results3 = fptr4.readlines()

data4  = []

for result in uncalibrated_results3:
    datum4 = result.split( )
    for i in range(0, len(datum4)):
        if i == 0:
            x_vals4.append(float(datum4[i]))
        elif i == 1:
            y_vals4.append(float(datum4[i]))
        elif i == 2:
            err_vert4.append(float(datum4[i]))

#trundles = [i ** 3 for i in range(1, 11)]
# fptr2 = open("cyg_ucerrors.txt", "w")

# print(err_vert)
# for item in err_vert:
#     fptr2.write(str(item) + "\n")

# fptr2.close()

fptr4.close()
fptr3.close()
fptr2.close()
fptr.close()


plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams["axes.linewidth"] = 1.0

# plt.title("XX Cygni Magnitudes", fontsize = 12, fontweight = "bold")
plt.xlabel("Time/hours", fontsize = 12)
plt.ylabel("Apparent Magnitude", fontsize = 12)

# plt.axis([-0.1, 2.5, 15.0, 10.0])
plt.xlim(-0.1, 2.5)
plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.ylim(15.5, 9.5)
plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1.0))
plt.gca().tick_params(width = 1.0, labelsize = 9)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f')) # sets the precision of the y axis labels to 1 decimal place

plt.errorbar(x_vals, y_vals, err_vert, fmt = "r.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")
plt.errorbar(x_vals, y_vals2, err_vert2, fmt = "g.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")
plt.errorbar(x_vals3, y_vals3, err_vert3, fmt = "m.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")
plt.errorbar(x_vals4, y_vals4, err_vert4, fmt = "y.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")
# plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("Combination_Graph.pdf") # change the name of the output graph pdf file here!