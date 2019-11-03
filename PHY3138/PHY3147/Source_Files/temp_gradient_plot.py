import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

altitudes = [] # in km
[(altitudes.append(i)) for i in range(0, 51, 1)]

temperatures = []

def temp(base_temp, beta, height, base_height):
    Temp = base_temp + beta * (height - base_height)
    return Temp

for altitude in altitudes:
    if altitude <= 11:
        T = temp(288.15, -6.50, altitude, 0)
        temperatures.append(T)
    elif altitude > 11 and altitude <= 20:
        T = temp(216.65, 0, altitude, 11)
        temperatures.append(T)
    elif altitude > 20 and altitude <= 32:
        T = temp(216.65, 1.00, altitude, 20)
        temperatures.append(T)
    elif altitude > 32 and altitude <= 47:
        T = temp(228.65, 2.80, altitude, 32)
        temperatures.append(T)
    else:
        T = temp(270.65, 0, altitude, 47)
        temperatures.append(T)

tropopause = []
[(tropopause.append(11)) for i in range(0, 101, 1)]

values = []
[values.append(i) for i in range(200, 301, 1)]

plt.rc('font', family = 'serif', serif = 'cmr10') 
plt.rcParams['mathtext.fontset'] = "cm" 
plt.rcParams["axes.linewidth"] = 1.0

# plt.axis([-0.1, 2.5, 12.4, 11.4])
plt.xlim(0, 50)
# plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.ylim(200, 300)
# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.5))
plt.gca().tick_params(width = 1.0, labelsize = 9)

plt.plot(altitudes, temperatures, LineStyle = "-", color = "r")
plt.plot(tropopause, values, LineStyle = "--", color = "k", linewidth = 0.75, label = "Tropopause")

plt.xlabel("Altitude (km)", fontsize = 12)
plt.ylabel("Temperature (K)", fontsize = 12)
plt.legend(loc = "lower right", title = "Legend", fontsize = 10)
# plt.title("XX Cygni Calibrated Magnitudes", fontsize = 12, fontweight = "bold")

# # plt.plot(x_vals2, y_vals2, 'b+')
plt.savefig("temperature_gradient.pdf") # change the name of the output graph pdf file here!