import numpy as np
import os

theta_vals_data = []
R_vals_data = []
theta_errs_data = []
R_errs_data = []

data_values = input("Input the data file you wish to read in: ")
data_fptr = open(data_values, "r", newline=None) # opening the file with the observed data e.g. 'test_data.dat'

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
# print(theta_errs_data)
filenames = os.listdir(os.curdir)
filenames = os.listdir(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3147\phi0_0.105err_early") # use this for Mac
file_list = []

[file_list.append(filename) for filename in filenames]

# file_list.pop(101) # removing the last element of the list - which is the program itself!
# print(file_list)
LS_val_array = [] # declaring an empty list to contain all the generated least sqaures difference values for each relative humidity (RH)

R_model_vals = [] # a list of interpolated R values

for filename in file_list:
    fpath = os.path.join(r"C:\Users\Matt\Documents\cprogramming\Python\Graphs\PHY3138\PHY3147\phi0_0.105err_early", filename) # reads files from another directory
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
      
    for i in range(0, len(theta_vals_data)):
        found_flag = 0
        R_model = 0
        for j in range(0, len(theta_vals)):
            if theta_vals[j] >= theta_vals_data[i] and found_flag == 0:
                # print("Filename is", filename)                
                # print("Model theta values either side are: {:f} {:f}" .format(theta_vals[j-1], theta_vals[j]))
                # print("Data theta value is {:f}" .format(theta_vals_data[i]))
                # print("R vals data i {:f}" .format(R_vals_data[i]))
                # print("R vals model {:f}" .format(R_vals[j]))

                R_model = R_vals[j-1] + ((R_vals[j] - R_vals[j-1]) / (theta_vals[j] - theta_vals[j-1])) * (theta_vals_data[i] - theta_vals[j-1])
                R_model_vals.append(R_model)
               
                found_flag = 1

N = len(data_result_list)

model_data = input("Enter in the file where the RH interpolated values should be stored: ")
my_file = open(model_data, "w") # opening the interpolated R values data file e.g. 'test_model.dat'
counter = 0
for number in R_model_vals:
    if counter % N == 0 and counter != 0:
        my_file.write("\n")
    my_file.write(str(number))
    my_file.write(" ")
    
    counter += 1

my_file.close() 