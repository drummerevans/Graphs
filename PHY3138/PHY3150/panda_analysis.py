import numpy as np
import pandas as pd
import math
import time
from datetime import datetime

raw_data = pd.read_csv("test14.csv") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'

# aug26_data = raw_data.sort_values("TIMESTAMP") # sorted into a time ordered DataFrame


# new_long = []
# new_lat = []
# for i in range(0, len(longtiude)):
#     if (longtiude[i]) and (latitude[i]) != 0.0:
#         new_long.append(longtiude[i])
#         new_lat.append(latitude[i])

# df2 = pd.DataFrame(list(zip(new_long, new_lat)), columns = ["Long", "Lat"])
# df2.to_csv("long_lat_test.csv", sep = "\t", header = False, index = False)

ID = raw_data["REG"].tolist()
raw_time = raw_data["VALIDITY_TIME"].tolist()
roll = raw_data["ROLL"].tolist()
latitude = raw_data["LAT"].tolist()
longitude = raw_data["LONG"].tolist()


new_time = []
roll_rate = []
# converts the times to seconds
for i in range(0, len(raw_time)):
    if ID[i] == "EXS6KA  ":
        new_time.append(sum(x * int(t) for x, t in zip([3600, 60, 1], raw_time[i].split(":"))))
        roll_rate.append(roll[i])


new_long = []
new_lat = []
for i in range(0, len(longitude)):
    if (longitude[i] and (latitude[i])) != 0.0:
        if ID[i] == "EXS6KA  ":
            # print("TRUE")
            new_long.append(longitude[i])
            new_lat.append(latitude[i])

df2 = pd.DataFrame(list(zip(new_time, roll_rate)), columns = ["Time", "Roll"])
df2.to_csv("roll_rate4.csv", sep = "\t", header = False, index = False)

df2 = pd.DataFrame(list(zip(new_long, new_lat)), columns = ["Long", "Lat"])
df2.to_csv("long_lat_test4.csv", sep = "\t", header = False, index = False)