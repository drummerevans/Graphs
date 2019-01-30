import numpy as np

# declaring empty lists for the calibrated values
x_vals = []
y_vals = []
err_vert = [] 

fptr = open("five_ohm.txt", "r", newline=None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            x_vals.append(float(datum[i]))
        elif i == 1:
            y_vals.append(float(datum[i]))
        elif i == 2:
            err_vert.append(float(datum[i]))

fptr.close()

print("The work done is: ")
print(np.trapz(y_vals, dx = (15))) # input array of y values, and intervals at which they were taken

print("The error in the work is: ")

work_err_list = []
work_err = 0

for i in range(len(err_vert)):
    if i == 0:
        work_err_list.append((err_vert[i] ** 2) / 4)
    if i == 16:
        work_err_list.append((err_vert[i] ** 2) / 4)
    else:
        work_err_list.append(err_vert[i] ** 2)
    work_err += work_err_list[i]

print(work_err)
final_err = 15 * (work_err ** 0.5)

print(final_err)