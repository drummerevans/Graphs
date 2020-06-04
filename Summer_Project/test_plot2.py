import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

KPOINTS = ["3x3x3", "5x5x5", "6x6x6", "8x8x8", "9x9x9"]
TOTEN = [-21.75251597, -21.73927897, -21.75626693, -21.73912656, -21.74579104]

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm"
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

plt.plot(KPOINTS, TOTEN, Marker = "+", color = "b", markeredgewidth = 1, markerfacecolor = "r", linestyle = "None")

plt.xlabel("KPOINTS", fontsize = 12)
plt.ylabel("TOTEN, (ev)", fontsize = 12)

# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("ENCUT_Trials2.pdf") # change the name of the output graph pdf file here!