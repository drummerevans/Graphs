import numpy as np
import os

theta_vals_data = []
R_vals_data = []
theta_errs_data = []
R_errs_data = []

data_values = input("Input the data file you wish to read in: ")
fptr = open(data_values, "r", newline=None) # opening the R data values 'test_data.dat'

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            theta_vals_data.append(float(datum[i]))
        elif i == 1:
            R_vals_data.append(float(datum[i]))
        elif i == 2:
            theta_errs_data.append(float(datum[i]))
        elif i == 3:
            R_errs_data.append(float(datum[i]))


fptr.close()

R_vals_model = []

model_data = input("Enter in the file with the RH model data: ")
fptr2 = open(model_data, "r", newline=None) # opening the interpolated R values 'test_model.dat'

list_of_results2 = fptr2.readlines()

data  = []

for result in list_of_results2:
    datum = result.split( )
    for i in range(0, len(datum)):
        R_vals_model.append(float(datum[i]))
        
fptr2.close()


data_values = np.array(R_vals_data) # creating an array for the R data values
N = len(data_values)

data_errors = np.array(R_errs_data) # creating an array for the R errors

model = np.array(R_vals_model) # creating a 2D array for the model (interpolated) values
shape = (101, N)
model_values = model.reshape(shape) 


residual_values = []
ls_values = []
for i in range(0, len(model_values)):

    residual = 0
    ls_value = 0
    for j in range(0, N):
        # print(data_values[j])
        # print(model_values[i][j])
        residual = data_values[j] - model_values[i][j]
        ls_value += (residual ** 2) # remember to divide by errors when we get data!
        if j == (N - 1):
            residual_values.append(residual)
            ls_values.append(ls_value)


min_value = min(ls_values)

# min_values = ([(i, (float(ls_values[i]))) for i in range(0, len(ls_values)) if ls_values[i] == min_value])
# print("The RH and corresponding minimum value is:", min_values)

for i in range(0, len(ls_values)): # prints out the minimum values and index number
    if ls_values[i] == min_value:
        print("The minimum value is: {:f} " .format(ls_values[i]))
        print("The corresponding (index number) RH is: {:d} " .format(i))

output_file = input("Enter in the file name you wish to write ls values to: ") # e.g. 'ls_test.dat'
my_file = open(output_file, "w")

for number in ls_values:
    my_file.write(str(number))
    my_file.write("\n")

output_file2 = input("Enter in the file name you wish to write residuals to: ")
my_file2 = open(output_file2, "w")

for res in residual_values:
    my_file2.write(str(res))
    my_file2.write("\n")
    
my_file.close()
my_file2.close()