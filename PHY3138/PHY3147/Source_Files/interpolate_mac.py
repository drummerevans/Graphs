import numpy as np
import os

theta_vals_data = []
R_vals_data = []
theta_errs_data = []
R_errs_data = []

data_fptr = open("test_data.dat", "r", newline=None) # opening the file with the observed data

data_result_list = data_fptr.readlines() # creating a list containing observed data results

# data  = []
for result in data_result_list:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            theta_vals_data.append(float(datum[i]))
        elif i == 1:
            R_vals_data.append(float(datum[i]))
        elif i == 2:
            theta_errs_data.append(7.85e-6) # initially setting the x-error bars equal to 7.85e-3
        elif i == 3:
            R_errs_data.append(8e-3) # initially setting the y-error bars equal to 1

data_fptr.close()
print(theta_errs_data)
filenames = os.listdir(os.curdir)
filenames = os.listdir(r"/Users/matthewevans/Documents/cprogramming/Graphs/PHY3138/PHY3147/phi0_0.1_files") # use this for Mac
file_list = []


for filename in filenames:
    file_list.append(filename)
    

file_list.pop(101) # removing the last element of the list - which is the program itself!
print(file_list)
LS_val_array = [] # declaring an empty list to contain all the generated least sqaures difference values for each relative humidity (RH)

for filename in file_list:
    fpath = os.path.join(r"/Users/matthewevans/Documents/cprogramming/Graphs/PHY3138/PHY3147/phi0_0.1_files", filename) # reads files from another directory
    fptr = open(fpath, "r", newline = None)
    list_of_results = fptr.readlines()
 
    data = []
    R_model = [] # a list of interpolated R values
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


      
    for i in range(0, len(theta_vals_data)):
        found_flag = 0
        for j in range(0, len(theta_vals)):
            if theta_vals[j] >= theta_vals_data[i] and found_flag == 0:
                print("Filename is", filename)                
                print("Model theta values either side are: {:f} " .format(theta_vals[j-1]) .format(theta_vals[j]))
                print("Data theta value is {:f}" .format(theta_vals_data[i]))
                print("R vals data i {:f}" .format(R_vals_data[i]))
                print("R vals model {:f}" .format(R_vals[j]))

                # R_model = R[j-1] + ((R[j] - R[j-1]) / (theta[j] - theta[j-1])) * (theta[i] - theta[j-1])

                found_flag = 1
        