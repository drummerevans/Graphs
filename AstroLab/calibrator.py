import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

XX_Cyg = []
Cal1 = []
Cal2 = [] 
Cal3 = [] 

fptr = open("uncal_mags.txt", "r", newline=None)

list_of_results = fptr.readlines()

data  = []
    
for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            XX_Cyg.append(str(datum[i]))
        elif i == 1:
            Cal1.append(str(datum[i]))
        elif i == 2:
            Cal2.append(str(datum[i]))
        elif i == 3:
            Cal3.append(str(datum[i]))

def calibrate(uncal, cal_val):
    A1 = []
    for num in uncal:
        if num != "INDEF":
            num = float(num) - cal_val # calibrating the values of the observed magnitudes for the calibration stars
        A1.append(num)
    return A1

F_vals = calibrate(Cal1, 10.886)
G_vals = calibrate(Cal2, 13.183)
H_vals = calibrate(Cal3, 10.406)


average = []

for i in range(0, len(F_vals)):
    row = []
    if F_vals[i] != "INDEF":
        row.append(float(F_vals[i]))
    if G_vals[i] != "INDEF":
        row.append(float(G_vals[i]))
    if H_vals[i] != "INDEF":
        row.append(float(H_vals[i]))
    item_amount = len(row)
    if item_amount != 0:
        av = 0
        for num in row:
            av += num
        av /= item_amount
        average.append(av)
    else:
        average.append(np.nan)
    
print(average)

fptr.close()