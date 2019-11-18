import numpy as np
import pandas as pd

# below is to be used with the "bankhol.csv" file

for i in range(0, len(age_values)):
    if age_values[i] > 20 and age_values[i] < 29:
        print(age_values[i], names[i])

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


df2 = pd.DataFrame(list(zip(times, obs_vals)), columns = ["Times", "Obs_Ang"])
df2.to_csv("my_times.csv", header = False, index = False)