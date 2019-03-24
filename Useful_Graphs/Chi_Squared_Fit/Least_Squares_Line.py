import numpy as np
import scipy.optimize as optimization
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

def least_squares(funct, x, y, x_errors, y_errors, w_initial):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales  
    plt.rcParams["axes.linewidth"] = 1.0

    ls_arr, ls_cov = optimization.curve_fit(funct, x, y, w_initial, absolute_sigma=True) # there is no argument for sigma here as using the LS method
    w = ls_arr
    print("\nThe gradient of the least squares fit is:", end = " ")
    print("{:f}" .format(w[0]))
    print("The y-intercept of the least squares fit is:", end = " ")
    print("{:f}" .format(w[1]))

    def misfit_fvals(x_results):
        f_results = []
        for x_result in x_results:
            f = w[0] * x_result + w[1]
            f_results.append(f)
        return f_results

    f_vals = misfit_fvals(x)
    # print(f_vals) # printing the chi squared 'y' values that lie on the straight line model

    f_nums = []
    for i in range(0, len(f_vals)):
        f_nums.append(f_vals[i] - y[i])

    sigma = statistics.stdev(f_nums) # standard deviation of quantity 'f_vals - y'
    print("Sigma for least squares fit is: {:f}" .format(sigma))

    arr_size = int(len(x))
    N = arr_size - 1 # N = x(arr_size - 1) # where N is the final element in the array (of x vals)
                        # we have to -1 as elements in array start count at 0 NOT 1
    
    # The next two lines are for linear i.e. straight line fits only
    grad_err = (2 * sigma) / (x[N] - x[0])
    print("Gradient error for least squares fit is: {:f}\n" .format(grad_err))

    print("The best fitting parameters and covariance matrix are: \n", ls_arr)
    print("The covariance matrix is: \n", ls_cov)
    print("The resulting errors on the fitting parameters are: \n", np.sqrt(np.diag(ls_cov)))

    # plt.figure(figsize = (8, 6))
    plt.errorbar(x, y, y_errors, x_errors, fmt = "r+", capsize = 3, elinewidth = 0.8, markeredgewidth = 0.8, LineStyle = "none")
    # the last argument for the two lines below, is for the legend
    plt.plot(x, y, Marker = "+", MarkerSize = 10, MarkerEdgeColor = "r", MarkerFaceColor = "r", markeredgewidth = 0.8, LineStyle = "none", label = "Data Points")
    plt.plot(x, f_vals, LineWidth = 0.9, LineStyle = "-", Color = "b", label = "Least Squares Fit") # 'least sqaures line of best fit
    # plt.plot(x, g_vals, LineWidth = 0.9, LineStyle = "-", Color = "m", label = "Chi Squared Fit") # 'chi squared line of best fit'
    plt.title("Least Squares Fit vs Chi Squared Fit", fontsize = 12, fontweight = "bold")
    plt.xlabel("x values", fontsize = 12)
    plt.ylabel(" y values", fontsize = 12)
    plt.legend(loc = "lower right", title = "Legend", fontsize = 10)
    # plt.axis([0, 5.0, 0, 12])
    plt.xlim(0, 6)
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
    plt.ylim(0, 14)
    plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))

    plt.gca().tick_params(width = 1.0, labelsize = 10)
  
    plt.savefig("Chi_Squared_Fit.pdf")