import numpy as np
import os

theta_vals = []
R_vals = []
theta_errs = []
R_errs = [] 

RH_humidity = input("Enter in the .dat RH file name: ")

# filenames = os.listdir("/Users/matthewevans/Documents/cprogramming/Graphs/PHY3138/PHY3147/0.1phi0_files")

# for filename in filenames:
    

fptr = open(filename, "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data = result.split( )
    for i in range(0, len(data)):
        if i == 0:
            theta_vals.append(float(data[i]))
        elif i == 1:
            R_vals.append(float(data[i]))
        elif i == 2:
            theta_errs.append(7.85e-6) # initiall setting the x-error bars equal to 7.85e-3
        elif i == 3:
            R_errs.append(8e-3) # initially setting the y-error bars equal to 1
    
fptr.close()

def least_square_diff(y_results, g_results, sigma_results):

        chi_vals = []
        for i in range(0, len(y_results)):
            chi_vals.append(((y_results[i] - g_results[i]) / sigma_results[i]) ** 2)
            print("Value of chi squared for data point",  i + 1,  "is", chi_vals[i])

        chi_squared = 0
        for i in range(0, len(chi_vals)):
            chi_squared += chi_vals[i]

        return chi_squared


print(least_square_diff(R_vals, R_data, R_errs))