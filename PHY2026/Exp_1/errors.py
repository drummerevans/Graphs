import numpy as np
import math
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

XX_Cyg_errs = []
Cal1_errs = []
Cal2_errs = [] 
Cal3_errs = [] 

fptr = open("uncal_errors.txt", "r", newline=None)

list_of_results = fptr.readlines()

data  = []
    
for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)):
        if i == 0:
            XX_Cyg_errs.append(str(datum[i]))
        elif i == 1:
            Cal1_errs.append(str(datum[i]))
        elif i == 2:
            Cal2_errs.append(str(datum[i]))
        elif i == 3:
            Cal3_errs.append(str(datum[i]))

XX_Cyg_errs2 = []
for num in XX_Cyg_errs:
    XX_Cyg_errs2.append(float(num))

def calibrate(uncal_errs):
    A1_errs = []
    for num in uncal_errs:
        if num != "INDEF":
            num = float(num) 
        A1_errs.append(num)
    return A1_errs

F_errs = calibrate(Cal1_errs)
G_errs = calibrate(Cal2_errs)
H_errs = calibrate(Cal3_errs)

squared_average = []

for i in range(0, len(F_errs)):
    row = []
    if F_errs[i] != "INDEF":
        row.append(math.pow(float(F_errs[i]), 2))
    if G_errs[i] != "INDEF":
        row.append(math.pow(float(G_errs[i]), 2))
    if H_errs[i] != "INDEF":
        row.append(math.pow(float(H_errs[i]), 2))
    item_amount = len(row)
    if item_amount != 0:
        av = 0
        for num in row:
            av += num
        av /= math.pow(item_amount, 2)
        squared_average.append(av)
    else:
        squared_average.append(np.nan)

XX_Cyg_errs2_squared = []
for i in range(0, len(XX_Cyg_errs2)):
    XX_Cyg_errs2_squared.append(math.pow(float(XX_Cyg_errs2[i]), 2))

XX_Cyg_errs2_squared = np.array(XX_Cyg_errs2_squared)
squared_average = np.array(squared_average)

XX_Cyg_Calibrated_Errs = XX_Cyg_errs2_squared + squared_average

print(XX_Cyg_Calibrated_Errs)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(np.sqrt(np.abs(XX_Cyg_Calibrated_Errs)))

final_array_errors_result = np.sqrt(np.abs(XX_Cyg_Calibrated_Errs))

fptr2 = open("XX_cal_errs.txt", "w")

# print(err_vert)
for item in final_array_errors_result:
    fptr2.write(str(item) + "\n")

fptr2.close()

fptr.close()