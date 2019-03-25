import numpy as np
import scipy.optimize as optimization
from scipy.interpolate import *
import matplotlib.pyplot as plt
import matplotlib.ticker
import statistics

def chi_squared2(funct, x, y, x_errors, y_errors, w_initial):
    plt.rc('font', family = 'serif', serif = 'cmr10')
    plt.rcParams['mathtext.fontset'] = "cm" 
    # plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['axes.unicode_minus'] = False # ensures that minus signs appear on the axes scales 
    plt.rcParams["axes.linewidth"] = 1.0

    chi_arr, chi_cov = optimization.curve_fit(funct, x, y, w_initial, y_errors, absolute_sigma=True) # produces the coefficient values for the 'best fit' line to data points
    u = chi_arr
    print("The first coefficient of the chi squared fit is:", end = " ")
    print("{:f}" .format(u[0]))
    # print("The second coefficient of the chi squared fit is:", end = " ")
    # print("{:f}" .format(u[1]))
    # print("The third coefficient of the chi squared fit is:", end = " ")
    # print("{:f}" .format(u[2]))

    def misfit_gvals(x_results):
        g_results = []
        for x_result in x_results:
            g = (np.sinc((0.04e-3 * x_result) / (u[0] * 0.5)))**2 # input slit width and separation here!
            g_results.append(g)
        return g_results

    g_vals = misfit_gvals(x)
    # print(g_vals) # printing the chi squared 'y' values that lie on the straight line model

    g_nums = []
    for i in range(0, len(g_vals)):
        g_nums.append(g_vals[i] - y[i])


    sigma = statistics.stdev(g_nums) # standard deviation of quantity 'g_vals - y'
    print("Sigma for chi squared fit is: {:f}" .format(sigma))

    arr_size = int(len(x))
    N = arr_size - 1 # N = x(arr_size - 1) # where N is the final element in the array (of x vals)
                        # we have to -1 as elements in array start count at 0 NOT 1
    
    # The next two lines are for linear i.e. straight line fits only
    # grad_err = (2 * sigma) / (x[N] - x[0])
    # print("Gradient error for chi squared fit is: {:f}\n" .format(grad_err))
    
    def misfit_chivals(y_results, g_results, sigma_results):

        chi_vals = []
        for i in range(0, len(y_results)):
            chi_vals.append(((y_results[i] - g_results[i]) / sigma_results[i]) ** 2)
            # print("Value of chi squared for data point",  i + 1,  "is", chi_vals[i])
        
        chi_squared = 0
        for i in range(0, len(chi_vals)):
            chi_squared += chi_vals[i]

        return chi_squared

    print("The best fitting parameters and covariance matrix are: \n", chi_arr)
    print("The covariance matrix is: \n", chi_cov)
    print("The resulting errors on the fitting parameters are: \n", np.sqrt(np.diag(chi_cov)))

    Chi_Squared_Value = misfit_chivals(y, g_vals, y_errors)
    print("\nThe value of Chi Squared is:", end = " ")
    print(Chi_Squared_Value)



    # plt.figure(figsize = (8, 6))
    # plt.errorbar(x, y, y_errors, x_errors, fmt = "r.", capsize = 3, elinewidth = 0.3, markeredgewidth = 0.3, LineStyle = "none")
    plt.errorbar(x, y, y_errors, x_errors, fmt = "r.", capsize = 4, elinewidth = 0.1, markeredgewidth = 0.3, markerfacecolor = "none", markersize = 7, LineStyle = "none")
    # the last argument for the two lines below, is for the legend
    plt.plot(x, y, Marker = ".", MarkerSize = 0.5, MarkerEdgeColor = "r", MarkerFaceColor = "r", markeredgewidth = 0.3, LineStyle = "none")
    plt.plot(x, g_vals, LineWidth = 0.9, LineStyle = "--", Color = "k", label = "Single Slit Envelope") #, label = "Chi Squared Fit") # 'chi squared line of best fit'
    # plt.plot(x_vals, f_vals, LineWidth = 0.9, LineStyle = "-", Color = "b", label = "Least Squares Fit") # 'least sqaures line of best fit
    # plt.title("Least Squares Fit vs Chi Squared Fit", fontsize = 12, fontweight = "bold")
    plt.xlabel("Position $x$ (m)", fontsize = 12)
    plt.ylabel("Intensity $I$", fontsize = 12)
    plt.legend(loc = "upper right", title = "Legend", fontsize = 10)
    plt.axis([-0.09, 0.09, 0.00, 1.05])
    # plt.xlim(-0.08, 0.08)
    # plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.01))
    # plt.ylim(-0.1, 0.40)
    # plt.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.05))

    plt.gca().tick_params(width = 1.0, labelsize = 10)
  
    plt.savefig("Chi_Squared_Cosinc.pdf")