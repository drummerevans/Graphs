import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics
import os
import pandas as pd

# print(theta_errs_data)
filenames = os.listdir(os.curdir)
filenames = os.listdir(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3150\Planes") # use this for Windows
file_list = []

[file_list.append(filename) for filename in filenames]

print(file_list)

for filename in file_list:
    fpath = os.path.join(r"/Users/matthewevans/Documents/cprogramming/Graphs/PHY3138/PHY3150/Planes", filename) # reads files from another directory
    fptr = open(fpath, "r", newline = None)
    list_of_results = fptr.readlines()
    
    data = []
    x = []
    y = []
    w = []
    h = []


    for result in list_of_results:
        data = result.split( )
        for i in range(0, len(data)):
            if i == 0:
                x.append(float(data[i]))
            elif i == 1:
                y.append(float(data[i]))
            elif i == 2:
                w.append(float(data[i])) # initially setting the x-error bars equal to 7.85e-3
            elif i == 3:
                h.append(float(data[i])) # initially setting the y-error bars equal to 1
        
    fptr.close()
      
    for i in range(0, len(theta_vals_data)):
        found_flag = 0
        R_model = 0
        theta_model = 0
        for j in range(0, len(theta_vals)):
            if theta_vals[j] >= theta_vals_data[i] and found_flag == 0:
                # print("Filename is", filename)                
                # print("Model theta values either side are: {:f} {:f}" .format(theta_vals[j-1], theta_vals[j]))
                # print("Data theta value is {:f}" .format(theta_vals_data[i]))
                # print("R vals data i {:f}" .format(R_vals_data[i]))
                # print("R vals model {:f}" .format(R_vals[j]))

                R_model = R_vals[j-1] + ((R_vals[j] - R_vals[j-1]) / (theta_vals[j] - theta_vals[j-1])) * (theta_vals_data[i] - theta_vals[j-1])
                R_model_vals.append(R_model)

                theta_model = theta_vals[j]
                theta_model_vals.append(theta_model)
               
                found_flag = 1

data = []
for filename in file_list:

    data[i] = pd.read_csv(filename, index_col = False) # optical data

    # x[i]c = []
    # y[i]c = []

    # x[i]c.append(x1[i] + w1[i] / 2)
    # y[i]c.append(y1[i] - h1[i] / 2)


# def plotter(source_file, col1, col2):

#     # file1 = input("Enter in the first file you would like to read data from: ")
#     fptr = open(source_file, "r", newline=None)

#     list_of_results = fptr.readlines()

#     data  = []

#     for result in list_of_results:
#         datum = result.split( )
#         for i in range(0, len(datum)):
#             if i == 0:
#                 col1.append(float(datum[i]))
#             elif i == 1:
#                 col2.append(float(datum[i]))

#     fptr.close()




# # declaring empty lists for the data values
# timestamp = []
# altitude = []
# file_name = input("Enter in the file you would like to read data from: ")
# plotter(file_name, timestamp, altitude)

# # declaring empty lists for the data values
# timestamp2 = []
# altitude2 = []
# file_name2 = input("Enter in the file2 you would like to read data from: ")
# plotter(file_name2, timestamp2, altitude2)

# # declaring empty lists for the data values
# timestamp3 = []
# altitude3 = []
# file_name3 = input("Enter in the file3 you would like to read data from: ")
# plotter(file_name3, timestamp3, altitude3)

# # declaring empty lists for the data values
# timestamp4 = []
# altitude4 = []
# file_name4 = input("Enter in the file4 you would like to read data from: ")
# plotter(file_name4, timestamp4, altitude4)

# # declaring empty lists for the data values
# timestamp5 = []
# altitude5 = []
# file_name5 = input("Enter in the file5 you would like to read data from: ")
# plotter(file_name5, timestamp5, altitude5)


# plt.rc('font', family = 'serif', serif = 'cmr10') 
# plt.rcParams['mathtext.fontset'] = "cm" 
# plt.rcParams["axes.linewidth"] = 1.0
# plt.rcParams["axes.unicode_minus"] = False

# # plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-1000, 50)
# # plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(0, 10000)
# # plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
# #plt.gca().tick_params(width = 1.0, labelsize = 9)

# plt.plot(timestamp, altitude, Marker = ".", color = "r", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "EI3842_1203")
# plt.plot(timestamp2, altitude2, Marker = ".", color = "b", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8207_1228")
# plt.plot(timestamp3, altitude3, Marker = ".", color = "g", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8241_1213")
# plt.plot(timestamp4, altitude4, Marker = ".", color = "m", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "FR8297_1143")
# plt.plot(timestamp5, altitude5, Marker = ".", color = "k", markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "-", label = "U2402_1218")

# plt.xlabel("Timestamp $(s)$", fontsize = 12)
# plt.ylabel("Altitude $(')$", fontsize = 12)
# plt.legend(loc = "lower left", title = None, fontsize = 10)
# # plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# # plt.plot(x_vals2, y_vals2, 'b+')
# plt.savefig("altitude_plot.pdf") # change the name of the output graph pdf file here!