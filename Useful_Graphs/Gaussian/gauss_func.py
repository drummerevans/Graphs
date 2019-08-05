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

standard_dev = 0.00573 # add in sigma here
mean_val = 0.434038; # add in the mean value here
print_file = "Gaussian_Module_Test.pdf"

def gauss(sigma, results, mean_val, print_file):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales  
    plt.rcParams["axes.linewidth"] = 1.0
    
    f_vals = []
    for result in results:
        f = 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((result - mean_val) **2 / (2 * sigma ** 2)))
        f_vals.append(f)
    plt.plot(results, f_vals, Marker = "+", MarkerSize = 10, MarkerEdgeColor = "r", markerfacecolor = "r", linewidth = 0.9, LineStyle = "-", Color = "b")
    
    # plt.figure(figsize = (8, 6))
  
    plt.axis([0.42, 0.47, 0, 70]) # set axis limts here 
    plt.title("Gaussian Function", fontsize = 12, fontweight = "bold") # add a title if needed
    plt.xlabel("x values", fontsize = 12)
    plt.ylabel(" y values", fontsize = 12)
    plt.gca().tick_params(width = 1.0, labelsize = 10)

    plt.savefig(print_file)

gauss(standard_dev, data, mean_val, "Gaussian Graph.pdf")
fptr.close()