import pandas as pd
import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics


radio_data = pd.read_csv("tom3kmA.csv", index_col = False) # ADS-B data


# ADS-B assignments
radio_t = radio_data["TIMESTAMP"].tolist()
radio_roll = radio_data["ROLL"].tolist()

new_times = []
for i in range(0, len(radio_t)):
    new_times.append(radio_t[i] - 628)

radio_time_roll = pd.DataFrame(list(zip(new_times, radio_roll)), columns = ["time", "roll"])
radio_time_roll.to_csv("radio_dat.csv", sep = "\t", header = False, index = False)


# frame_roll = pd.DataFrame(list(zip(times1, roll)), columns = ["time", "roll"])
# frame_roll.to_csv("ADSB_roll.csv", sep = "\t", header = False, index = False)


plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm"
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["axes.unicode_minus"] = False

# plt.axis([-0.25, 2.5, 46.0, 50.0])
# plt.xlim(-2.5, 1.5)
#plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
#plt.ylim(46.0, 50.0)
#plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
#plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(new_times, radio_roll, Marker = None, color = "g", markeredgewidth = 0.3, markerfacecolor = "r", markersize = None, LineStyle = "-", linewidth ="0.5", label = "Radio Data")

plt.xlabel("Time (s)", fontsize = 12)
plt.ylabel("Roll Angle ($\\degree$)", fontsize = 12)
plt.legend(loc = "upper right", title = None, fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("ADSB_roll.pdf") # change the name of the output graph pdf file here!r