import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

# declaring empty lists for the calibrated values
theta_vals = []
R_vals = []
n_vals = [] 
z_vals = [] 

fptr = open("dry_test.dat", "r", newline=None)

list_of_results = fptr.readlines()

data  = []

for result in list_of_results:
    datum = result.split( )
    for i in range(0, len(datum)): # starting at 4 in order to ignore the top 'title' row (with names) in the data file
        if i == 0:
            theta_vals.append(float(datum[i]))
        elif i == 1:
            R_vals.append(float(datum[i]))
        elif i == 2:
            n_vals.append(float(datum[i]))
        elif i == 3:
            z_vals.append(float(datum[i]))



#trundles = [i ** 3 for i in range(1, 11)]
# fptr2 = open("cyg_ucerrors.txt", "w")

# print(err_vert)
# for item in err_vert:
#     fptr2.write(str(item) + "\n")

# fptr2.close()

fptr.close()

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")
plt.xlabel("$\\theta$", fontsize = 12)
plt.ylabel("R", fontsize = 12)
# plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
# plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-0.5, 3.0)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(12.5, 11.5)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 9)


plt.errorbar(z_vals, R_vals, fmt = "b.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("dry_test_plot.pdf") # change the name of the output graph pdf file here!