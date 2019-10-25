import numpy as np
import os

theta_vals = []
R_vals = []
theta_errs = []
R_errs = [] 

# filenames = os.listdir("/Users/matthewevans/Documents/cprogramming/Graphs/PHY3138/PHY3147/phi0_0.1_files") # use this for Mac
# print(os.getcwd())
filenames = os.listdir(os.curdir) # use this for Windows
filenames = os.listdir(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3147\phi0_0.1_files") # use this for Windows
file_list = []


for filename in filenames:
    file_list.append(filename)
    

file_list.pop(101) # removing the last element of the list - which is the program itself!
LS_val_array = [] # declaring an empty list to contain all the generated least sqaures difference values for each relative humidity (RH)

for filename in file_list:
    fpath = os.path.join(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3147\phi0_0.1_files", filename)
    fptr = open(fpath, "r", newline = None)
    list_of_results = fptr.readlines()
 
    data = []
    theta_vals = []
    R_vals = []
    theta_errs = []
    R_errs = [] 

    for result in list_of_results:
        data = result.split( )
        for i in range(0, len(data)):
            if i == 0:
                theta_vals.append(float(data[i]))
            elif i == 1:
                R_vals.append(float(data[i]))
            elif i == 2:
                theta_errs.append(7.85e-6) # initially setting the x-error bars equal to 7.85e-3
            elif i == 3:
                R_errs.append(8e-3) # initially setting the y-error bars equal to 1
        
    fptr.close()

    def least_square_diff(y_results, g_results, sigma_results):

            chi_vals = []
            for i in range(0, len(y_results)):
                chi_vals.append(((y_results[i] + g_results[i]) / sigma_results[i]) ** 2)
                # print("Value of chi squared for data point",  i + 1,  "is", chi_vals[i])

            chi_squared = 0

            for i in range(0, len(chi_vals)):
                chi_squared += chi_vals[i]

            return chi_squared
    
    LS_val = least_square_diff(R_vals, R_vals, R_errs)
    LS_val_array.append(LS_val)
    print(LS_val)

print(LS_val_array)

min_val = min(LS_val_array) # finds the smallest least squares difference value
index_min_val = (np.argmin(LS_val_array)) # finds the element in the list for the smallest value

print("The smallest least squares value is, {:f}" .format(min_val))
print("The relative humidity this corresponds to is {:d}%" .format(index_min_val))

for filename in file_list:
    if index_min_val == file_list.index(filename):
        print("The file this corresponds to is", filename) # prints the RH file that gives the smallest LS value