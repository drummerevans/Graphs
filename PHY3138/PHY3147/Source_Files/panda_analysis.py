import numpy as np
import pandas as pd
import math

# below is to be used with the "bankhol.csv" file

raw_data = pd.read_csv("bankhol.csv") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'

aug26_data = raw_data.sort_values("TIMESTAMP") # sorted into a time ordered DataFrame

times = aug26_data["TIMESTAMP"].tolist()
sin_obs = aug26_data["obs"].tolist()
r_vals = aug26_data["r"].tolist()
theta_vals = aug26_data["ARCANG"].tolist()

obs_vals = []
for i in range(0, len(sin_obs)):
    obs = 0
    obs = np.arcsin(sin_obs[i]) * (180 / np.pi)
    obs_vals.append(obs)

obs1 = float(input("Enter in the lower bound of observed angle you would like to investigate: "))
obs2 = float(input("Now enter in the upper bound of observed angle: "))

selected_r_vals = []
selected_theta_vals = []
selected_obs_vals = []
for i in range(0, len(times)):
    if (times[i] <= 11340) and (obs1 <= obs_vals[i] <= obs2):
        selected_r_vals.append(r_vals[i])
        selected_theta_vals.append(theta_vals[i])
        selected_obs_vals.append(obs_vals[i])

average = np.mean(selected_obs_vals)
print("The mean of the selected observed angle range is: {:f}" .format(average))

std_dev = np.std(selected_obs_vals, ddof = 1)
print("The std dev of selected observed angle range is: {:f}" .format(std_dev))

mean_err = std_dev / (math.sqrt(len(selected_obs_vals)))
print("The error on the mean of the selected observed angle is: {:f}" .format(mean_err))


df2 = pd.DataFrame(list(zip(selected_theta_vals, selected_r_vals)), columns = ["theta", "r"])
df2.to_csv("aug26_0.5_data.csv", sep = "\t", header = False, index = False)