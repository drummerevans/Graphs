import numpy as np
import math
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

fptr = open("air_resistance.txt", "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data.append(float(result))

def histogram(data_values, bin_number, graph_name):
    plt.rcParams["font.family"] = "Times New Roman" 
    plt.rcParams["axes.linewidth"] = 1.0

    A = plt.hist(data_values, bin_number, facecolor = "m", alpha = 0.75, edgecolor = "k", label = "Bin") # plots a histogram with five bins

    plt.title("Histogram", fontsize = 12, fontweight = "bold")
    plt.xlabel("Bin Value", fontsize = 12)
    plt.ylabel("Probability Per Unit Time", fontsize = 12)
    # plt.axis([0.42, 0.47, 0, 80])
    plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
    plt.gca().tick_params(width = 1.0, labelsize = 10)
    plt.savefig(graph_name)
    return A

X = histogram(data, 5, "hist.pdf")
# print(A) # returns the amount of values in each bin, shown in first array in terminal
values = X[0] # amount of values in each bin

bin_vals = []
for i in range(0, len(values)):
    bin_vals.append(int(values[i]))

print("The amount of values in each bin is:", (bin_vals))

fptr.close()