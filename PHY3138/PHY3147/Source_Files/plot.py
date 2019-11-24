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

# declaring empty lists for the wet 0.25 values
theta_vals3 = []
R_vals3 = []
n_vals3 = [] 
z_vals3 = []

# declaring empty lists for the wet 0.5 values
theta_vals4 = []
R_vals4 = []
n_vals4 = [] 
z_vals4 = []

# declaring empty lists for the wet 0.5 values
theta_vals5 = []
R_vals5 = []
n_vals5 = [] 
z_vals5 = []

# declaring empty lists for the data values
theta_data = []
R_data = []
theta_errs = [] 
R_errs = []

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

file2 = input("Enter in the second file you would like to read data from: ")
fptr2 = open(file2)

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

# fptr3 = open("0.505phi0_038RH.dat")

# list_of_results3 = fptr3.readlines()

# data3  = []

# for result in list_of_results3:
#     datum = result.split( )
#     for i in range(0, len(datum)):
#         if i == 0:
#             theta_vals3.append(float(datum[i]))
#         elif i == 1:
#             R_vals3.append(float(datum[i]))
#         elif i == 2:
#             n_vals3.append(float(datum[i]))
#         elif i == 3:
#             z_vals3.append(float(datum[i]))

# fptr4 = open("0.1phi0_50RH.dat")

# list_of_results4 = fptr4.readlines()

# data4  = []

# for result in list_of_results4:
#     datum = result.split( )
#     for i in range(0, len(datum)):
#         if i == 0:
#             theta_vals4.append(float(datum[i]))
#         elif i == 1:
#             R_vals4.append(float(datum[i]))
#         elif i == 2:
#             n_vals4.append(float(datum[i]))
#         elif i == 3:
#             z_vals4.append(float(datum[i]))


# fptr5 = open("0.1phi0_75RH.dat")

# list_of_results5 = fptr5.readlines()

# data5  = []

# for result in list_of_results5:
#     datum = result.split( )
#     for i in range(0, len(datum)):
#         if i == 0:
#             theta_vals5.append(float(datum[i]))
#         elif i == 1:
#             R_vals5.append(float(datum[i]))
#         elif i == 2:
#             n_vals5.append(float(datum[i]))
#         elif i == 3:
#             z_vals5.append(float(datum[i]))

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
        elif i == 2:
            theta_errs.append(float(datum[i]))
        elif i == 3:
            R_errs.append(float(datum[i]))

fptr6.close()
# fptr5.close()
# fptr4.close()
# fptr3.close()
fptr2.close()
fptr.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.axis([-0.1, 2.5, 12.4, 11.4])
plt.xlim(-0.005, 0.075)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.ylim(6365, 6384)
plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(3))
plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(theta_vals, R_vals, Marker = ".", color = "r", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "0% RH")
# plt.plot(theta_vals3, R_vals3, Marker = ".", color = "g", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "38% RH")
# plt.plot(theta_vals4, R_vals4, Marker = ".", color = "g", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "50% RH")
# plt.plot(theta_vals5, R_vals5, Marker = ".", color = "c", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "75% RH")
plt.plot(theta_vals2, R_vals2, Marker = ".", color = "b", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "100% RH")
plt.plot(theta_data, R_data, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none", label = "Data Values")

plt.xlabel("$\\theta$ (rad)", fontsize = 12)
plt.ylabel("R (km)", fontsize = 12)
plt.legend(loc = "lower right", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("aug26_0.505_late.pdf") # change the name of the output graph pdf file here!