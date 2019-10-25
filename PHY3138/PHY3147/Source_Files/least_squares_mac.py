import numpy as np
import os

theta_vals_data = []
R_vals_data = []
n_vals_data = []
z_vals_data = [] 

fptr = open("test_data.dat", "r", newline=None) # opening the R data values

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
            n_vals_data.append(float(datum[i]))
        elif i == 3:
            z_vals_data.append(float(datum[i]))


fptr.close()

R_vals_model = []

fptr2 = open("test_model.txt", "r", newline=None) # opening the interpolated R values

list_of_results2 = fptr2.readlines()

data  = []

for result in list_of_results2:
    datum = result.split( )
    for i in range(0, len(datum)):
        R_vals_model.append(float(datum[i]))
        
fptr2.close()


data_values = np.array(R_vals_data) # creating an array for the data values
N = len(data_values)

model = np.array(R_vals_model) # creating a 2D array for the model (interpolated) values
shape = (101, N)
model_values = model.reshape(shape) 


ls_values = []
for i in range(0, len(model_values)):

    ls_value = 0
    for j in range(0, N):
        # print(data_values[j])
        # print(model_values[i][j])
        ls_value += ((data_values[j] - model_values[i][j]) ** 2) # remember to divide by errors when we get data!
        if j == (N - 1):
            ls_values.append(ls_value)


print(ls_values)
print(len(ls_values))

my_file = open("ls_test.txt", "w")

for number in ls_values:
    my_file.write(str(number))
    my_file.write("\n")
    
my_file.close() 