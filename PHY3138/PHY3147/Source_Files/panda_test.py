import numpy as np
import pandas as pd

data = [["B", 29], ["T", 25], ["Fred", 26], ["Gareth", 20]]

df = pd.DataFrame(data, columns = ["Name", "Age"])

print(df)

sort_by_age = df.sort_values("Age")

print(sort_by_age)

age_values = sort_by_age["Age"].tolist()
names = sort_by_age["Name"].tolist()

print(age_values)
print(names)

for i in range(0, len(age_values)):
    if age_values[i] > 20 and age_values[i] < 29:
        print(age_values[i], names[i])


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
for i in range(0, len(times)):
    if (times[i] <= 11340) and (obs_vals[i] >= obs1 and obs_vals[i] <= obs2):
        selected_r_vals.append(r_vals[i])
        selected_theta_vals.append(theta_vals[i])


df2 = pd.DataFrame(list(zip(selected_theta_vals, selected_r_vals)), columns = ["theta", "r"])
df2.to_csv("my_times.csv", header = False, index = False)