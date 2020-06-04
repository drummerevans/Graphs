import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

ENCUT = [300, 500, 600, 800, 1000]
TOTEN = [-21.72560395, -21.74143776, -21.74295140, -21.74303493, -21.74306937]

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm"
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

plt.plot(ENCUT, TOTEN, Marker = "+", color = "r", markeredgewidth = 1, markerfacecolor = "r", linestyle = "None")

plt.xlabel("ENCUT, (eV)", fontsize = 12)
plt.ylabel("TOTEN, (ev)", fontsize = 12)

# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("ENCUT_Trials.pdf") # change the name of the output graph pdf file here!