import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics
import pandas as pd
import os

filenames = os.listdir(os.curdir)
filenames = os.listdir(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3150\Planes") # use this for Windows
file_list = []

[file_list.append(filename) for filename in filenames]

for i in range(1, 37):
    datai = pd.read_csv(file_list[i], index_col = False)

# data1 = pd.read_csv("plane1.csv", index_col = False) # optical data
# data2 = pd.read_csv("plane2.csv", index_col = False) # optical data
# data3 = pd.read_csv("plane3.csv", index_col = False) # optical data
# data4 = pd.read_csv("plane4.csv", index_col = False) # optical data
# data5 = pd.read_csv("plane5.csv", index_col = False) # optical data
# data6 = pd.read_csv("plane6.csv", index_col = False) # optical data
# data7 = pd.read_csv("plane7.csv", index_col = False) # optical data
# data8 = pd.read_csv("plane8.csv", index_col = False) # optical data
# data9 = pd.read_csv("plane9.csv", index_col = False) # optical data
# data10 = pd.read_csv("plane10.csv", index_col = False) # optical data
# data11 = pd.read_csv("plane11.csv", index_col = False) # optical data
# data12 = pd.read_csv("plane12.csv", index_col = False) # optical data
# data13 = pd.read_csv("plane13.csv", index_col = False) # optical data
# data14 = pd.read_csv("plane14.csv", index_col = False) # optical data
# data15 = pd.read_csv("plane15.csv", index_col = False) # optical data
# data16 = pd.read_csv("plane16.csv", index_col = False) # optical data
# data17 = pd.read_csv("plane17.csv", index_col = False) # optical data
# data18 = pd.read_csv("plane18.csv", index_col = False) # optical data
# data19 = pd.read_csv("plane19.csv", index_col = False) # optical data
# data20 = pd.read_csv("plane20.csv", index_col = False) # optical data
# data21 = pd.read_csv("plane21.csv", index_col = False) # optical data
# data22 = pd.read_csv("plane22.csv", index_col = False) # optical data
# data23 = pd.read_csv("plane23.csv", index_col = False) # optical data
# data24 = pd.read_csv("plane24.csv", index_col = False) # optical data
# data25 = pd.read_csv("plane25.csv", index_col = False) # optical data
# data26 = pd.read_csv("plane26.csv", index_col = False) # optical data
# data27 = pd.read_csv("plane27.csv", index_col = False) # optical data
# data28 = pd.read_csv("plane28.csv", index_col = False) # optical data
# data29 = pd.read_csv("plane29.csv", index_col = False) # optical data
# data30 = pd.read_csv("plane30.csv", index_col = False) # optical data
# data31 = pd.read_csv("plane31.csv", index_col = False) # optical data
# data32 = pd.read_csv("plane32.csv", index_col = False) # optical data
# data33 = pd.read_csv("plane33.csv", index_col = False) # optical data
# data34 = pd.read_csv("plane34.csv", index_col = False) # optical data
# data35 = pd.read_csv("plane35.csv", index_col = False) # optical data
# data36 = pd.read_csv("plane36.csv", index_col = False) # optical data
# data37 = pd.read_csv("plane37.csv", index_col = False) # optical data

# # print(theta_errs_data)
# filenames = os.listdir(os.curdir)
# filenames = os.listdir(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3150\Planes") # use this for Windows
# file_list = []

# [file_list.append(filename) for filename in filenames]

for i in range(1, 37):

    xi = datai["x"].tolist()
    yi = datai["y"].tolist()

for i in range(1, 37):
    xic = []
    yic = []

    for j in range(0, len(xi[j])):
        xic.append(x[j] + w[j] / 2)
        yic.append(y[j] - h[j] / 2)



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