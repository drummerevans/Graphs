import numpy as np
# from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

def least_squares_fit(x, y, err_y):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    plt.rcParams["axes.linewidth"] = 1.0 

    arr_size = int(len(x))
    N = arr_size - 1 # N = x(arr_size - 1) # where N is the final element in the array (of x vals)
                        # we have to -1 as elements in array start count at 0 NOT 1

    p = np.polyfit(x, y, 1) # finds the coefficients for the 'best' fitting function
  
    f = np.polyval(p, x) # these are the 'y-values' of the fitting function
    sigma = statistics.stdev(f - y) # standard deviation of quantity 'f - y' amount of (vertical) deviation between the model and the data points

    # plt.figure(figsize = (8, 6))
    plt.errorbar(x, y, err_y, fmt = "k", capsize = 3, elinewidth = 0.6, MarkerSize = 2, markeredgewidth = 0.6, LineStyle = "none")
    # the last argument for the two lines below, is for the legend
    plt.plot(x, y, Marker = "+", MarkerSize = 4, MarkerEdgeColor = "k", MarkerFaceColor = "k", LineWidth = 0.6, LineStyle = "none")
    plt.plot(x, f, LineWidth = 0.6, Linestyle = "-", Color = "g", label = "Model") # 'line of best fit'

    # plt.title("Least Squares Fit", fontsize = 12, fontweight = "bold")
    plt.xlabel("Frequency " r"$\nu$(MHz)" , fontsize = 10)
    plt.ylabel("Magnetic Field $B$(mT)", fontsize = 10)
    plt.axis([0, 140, 0, 5])
    # plt.xlim(-1, 6)
    # ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    # plt.ylim(-2, 2)
    # ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    # plt.gca().ticklabel_format(axis='y',style='sci',scilimits=(1,4), useOffset=False)
    # plt.gca().yaxis.get_major_formatter().set_powerlimits((0, 1))
    # plt.gca().xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1e'))
    plt.gca().yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))
    plt.gca().tick_params(width = 1.0, labelsize = 8)
  
    plt.savefig("Electron_plot1.pdf")

    print("Gradient is: {:e}" .format(p[0]))
    print("y-intercept is: {:e}" .format(p[1]))
    print("Sigma is: {:e}" .format(sigma))
    
    # The next two lines are for linear i.e. straight line fits only
    grad_err = (2 * sigma) / (x[N] - x[0])
    print("Gradient error is: {:e}" .format(grad_err))