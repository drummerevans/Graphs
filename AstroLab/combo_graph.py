import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

# declaring empty lists for the calibrated values
x_vals = []
y_vals = []
err_horiz = [] 
err_vert = [] 

# declaring empty lists for the uncalibrated values
x_vals2 = []
y_vals2 = []
err_horiz2 = [] 
err_vert2 = [] 

fptr = open("calibrated_mags.txt", "r", newline=None)

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



fptr2 = open("initial_results.txt") 

uncalibrated_results = fptr2.readlines()

data2  = []

for result in uncalibrated_results:
    datum2 = result.split( )
    for i in range(0, len(datum2)):
        if i == 0:
            x_vals2.append(float(datum2[i]))
        elif i == 1:
            y_vals2.append(float(datum2[i]))
        elif i == 2:
            err_vert2.append(float(datum2[i]))


#trundles = [i ** 3 for i in range(1, 11)]
# fptr2 = open("cyg_ucerrors.txt", "w")

# print(err_vert)
# for item in err_vert:
#     fptr2.write(str(item) + "\n")

# fptr2.close()

fptr2.close()
fptr.close()

print(y_vals2)

plt.rcParams["font.family"] = "Times New Roman" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.title("XX Cygni Magnitudes", fontsize = 12, fontweight = "bold")
plt.xlabel("Time/hours", fontsize = 12)
plt.ylabel("Apparent Magnitude", fontsize = 12)

plt.axis([0, 2.5, 14.0, 11.0])
# plt.xlim(-0.5, 3.0)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(12.5, 11.5)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 10)


plt.errorbar(x_vals, y_vals, err_vert, fmt = "b+", capsize = 3, elinewidth = 0.8, markeredgewidth = 0.8, LineStyle = "none")
plt.errorbar(x_vals, y_vals2, err_vert2, fmt = "r+", capsize = 3, elinewidth = 0.8, markeredgewidth = 0.8, LineStyle = "none")
# plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("Combination_Graph.pdf") # change the name of the output graph pdf file here!