import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

def least_squares_fit(x, y, err_x, err_y):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    plt.rcParams["axes.linewidth"] = 1.0 

    arr_size = int(len(x))
    N = arr_size - 1 # N = x(arr_size - 1) # where N is the final element in the array (of x vals)
                        # we have to -1 as elements in array start count at 0 NOT 1

    p = np.polyfit(x, y, 1) # finds the coefficients for the 'best' fitting function
  
    f = np.polyval(p, x) # these are the 'y-values' of the fitting function
    sigma = statistics.stdev(f - y) # standard deviation of quantity 'f - y'

    # plt.figure(figsize = (8, 6))
    plt.errorbar(x, y, err_y, err_x, fmt = "k+", capsize = 1, elinewidth = 0.6, MarkerSize = 2, markeredgewidth = 0.6, LineStyle = "none")
    # the last argument for the two lines below, is for the legend
    # plt.plot(x, y, Marker = "+", MarkerSize = 4, MarkerEdgeColor = "k", MarkerFaceColor = "k", LineWidth = 0.8, LineStyle = "none")
    plt.plot(x, f, LineWidth = 0.6, Linestyle = "-", Color = "b", label = "Model") # 'line of best fit'

    # plt.title("Least Squares Fit", fontsize = 12, fontweight = "bold")
    plt.xlabel('$\\sqrt{d^2 + l^2}/mm$', fontsize = 10)
    plt.ylabel("$l/mm$", fontsize = 10)
    plt.axis([350, 850, 100, 250])
    # plt.xlim(-1, 6)
    # ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    # plt.ylim(-2, 2)
    # ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    plt.gca().tick_params(width = 1.0, labelsize = 8)
  
    plt.savefig("Blue_Plot.pdf")

    print("Gradient is: {:f}" .format(p[0]))
    print("y-intercept is: {:f}" .format(p[1]))
    print("Sigma is: {:f}" .format(sigma))
    
    # The next two lines are for linear i.e. straight line fits only
    grad_err = (2 * sigma) / (x[N] - x[0])
    print("Gradient error is: {:f}" .format(grad_err))