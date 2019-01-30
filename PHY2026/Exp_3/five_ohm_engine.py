import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

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


#trundles = [i ** 3 for i in range(1, 11)]
# fptr2 = open("cyg_ucerrors.txt", "w")

# print(err_vert)
# for item in err_vert:
#     fptr2.write(str(item) + "\n")

# fptr2.close()

fptr.close()

plt.rc('font', family = 'serif', serif = 'cmr10')
plt.rcParams['mathtext.fontset'] = "cm" 
# plt.rcParams["font.family"] = "Times New Roman" 
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales

# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")
plt.xlabel("Time (s)", fontsize = 12)
plt.ylabel("Power (W)", fontsize = 12)
# plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
# plt.axis([-0.1, 2.5, 12.4, 11.4])
# plt.xlim(-0.5, 3.0)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
# plt.ylim(12.5, 11.5)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 9)
plt.gca().ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.gca().yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))


plt.errorbar(x_vals, y_vals, err_vert, fmt = "r.", capsize = 6, elinewidth = 0.8, markeredgewidth = 0.3, markerfacecolor = "k", markersize = 4.5, LineStyle = "none")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("five_ohm1.pdf") # change the name of the output graph pdf file here!

print("The work done is: ")
print(np.trapz(y_vals, dx = (240/17))) # input array of y values, and intervals at which they were taken

print("The error in the work is: ")

work_err_list = []
work_err = 0

for i in range(len(err_vert)):
    work_err_list.append(err_vert[i] * x_vals[i])
    work_err += work_err_list[i]

print(work_err)

