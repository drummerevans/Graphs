import numpy as np
import math
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics
from gaussian import gauss

fptr = open("air_resistance.txt", "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data.append(float(result))

standard_dev = 0.00573 # add in sigma here
mean_val = 0.434038; # add in the mean value here
print_file = "Gaussian_Module_Test.pdf"

gauss(standard_dev, data, mean_val, print_file)

A = plt.hist(data, 5, facecolor = "m", alpha = 0.75, edgecolor = "k") # plots a histogram with five bins

plt.savefig("gauss_hist.pdf")
print(A) # returns the amount of values in each bin, shown in first array in terminal

values = A[0] # amount of values in each bin

bin_vals = []
for i in range(0, len(values)):
    bin_vals.append(int(values[i]))

print("The amount of values in each bin is:", (bin_vals))

fptr.close()