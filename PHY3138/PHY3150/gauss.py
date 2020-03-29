import numpy as np
import math
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

fptr = open("optical_roll7.csv", "r", newline = None)

list_of_results = fptr.readlines()

times  = []
roll = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            times.append(float(datum[i]))
        elif i == 1:
            roll.append(float(datum[i]))

mean_val = np.mean(roll)
standard_dev = np.std(roll, ddof = 1)

new_roll = sorted(roll)
print(new_roll)

print("The mean is: {:f}\n" .format(mean_val))
print("The standard deviation is: {:f}\n" .format(standard_dev))


def gauss(sigma, results, mean_value, print_file):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales  
    plt.rcParams["axes.linewidth"] = 1.0
    
    f_vals = []
    for result in results:
        f = 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((result - mean_value) **2 / (2 * sigma ** 2)))
        # f = np.exp(-np.power(result - mean_value, 2.) / (2 * np.power(sigma, 2.)))
        f_vals.append(f)
    plt.plot(results, Marker = ".", MarkerSize = 1, MarkerEdgeColor = "r", markerfacecolor = "r", LineStyle = " ", label = "Optical Data")
    plt.plot(results, f_vals, Marker = ".", MarkerSize = 1, MarkerEdgeColor = "r", markerfacecolor = "r", linewidth = 0.9, LineStyle = "-", Color = "b")

    # plt.figure(figsize = (8, 6))
  
    plt.axis([-1.0, 1.25, 0, 0.9]) # set axis limts here 
    # plt.title("Gaussian Function", fontsize = 12, fontweight = "bold") # add a title if needed
    plt.xlabel("Roll Angle ($\\degree$)", fontsize = 12)
    plt.ylabel("Frequency", fontsize = 12)
    plt.legend(loc = "lower right", title = None, fontsize = 10)
    plt.gca().tick_params(width = 1.0, labelsize = 10)

    plt.savefig(print_file)

gauss(standard_dev, new_roll, mean_val, "Gaussian Graph7.pdf")
fptr.close()