import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

fptr = open("pdump.list", "r", newline=None)

list_of_results = fptr.readlines()

data  = []

for time in range(0, 7780, 30):
    x_vals.append(time)
    
for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            y_vals.append(float(datum[i]))
        elif i == 1:
            err_vert.append(float(datum[i]))

fptr.close()