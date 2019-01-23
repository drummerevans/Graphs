import numpy as np
from Chi_Squared_Line import chi_squared
from Chi_Squared_Line2 import chi_squared2

x_vals = []
y_vals = []
x_err = []
y_err = [] 

x_vals2 = []
y_vals2 = []
x_err2 = []
y_err2 = [] 

fptr = open("data_1.txt", "r", newline = None)
fptr2 = open("data_2.txt", "r", newline = None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    data = result.split( )
    for i in range(0, len(data)):
        if i == 0:
            x_vals.append(float(data[i]))
        elif i == 1:
            y_vals.append(float(data[i]))
        elif i == 2:
            x_err.append(float(data[i]))
        elif i == 3:
            y_err.append(float(data[i]))

list_of_results2 = fptr2.readlines()

data_2  = []

for result in list_of_results2:
    data_2 = result.split( )
    for i in range(0, len(data_2)):
        if i == 0:
            x_vals2.append(float(data_2[i]))
        elif i == 1:
            y_vals2.append(float(data_2[i]))
        elif i == 2:
            x_err2.append(float(data_2[i]))
        elif i == 3:
            y_err2.append(float(data_2[i]))
       
fptr.close()
fptr2.close()

def func(x, a): # the model function that we pass into curve_fit() - in this case a straight line
        return a * x

# Initial guess.
wini = np.array([0.053])

def func2(x2, a2): # the model function that we pass into curve_fit() - in this case a straight line
        return a2 * x2

# Initial guess.
wini2 = np.array([0.053])

print(x_vals)
print(x_vals2)

chi_squared(func, x_vals, y_vals, x_err, y_err, wini)
chi_squared2(func2, x_vals2, y_vals2, x_err2, y_err2, wini2)