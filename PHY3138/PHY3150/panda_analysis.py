import numpy as np
import pandas as pd
import math
import time
from datetime import datetime

raw_data = pd.read_csv("tom3kmA.csv") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'

# aug26_data = raw_data.sort_values("TIMESTAMP") # sorted into a time ordered DataFrame


# new_long = []
# new_lat = []
# for i in range(0, len(longtiude)):
#     if (longtiude[i]) and (latitude[i]) != 0.0:
#         new_long.append(longtiude[i])
#         new_lat.append(latitude[i])

# df2 = pd.DataFrame(list(zip(new_long, new_lat)), columns = ["Long", "Lat"])
# df2.to_csv("long_lat_test.csv", sep = "\t", header = False, index = False)

latitude = raw_data["LATITUDE"].tolist()
longitude = raw_data["LONGITUDE"].tolist()


new_long = []
new_lat = []
for i in range(0, len(longitude)):
    new_long.append(longitude[i])
    new_lat.append(latitude[i])

df2 = pd.DataFrame(list(zip(new_long, new_lat)), columns = ["Long", "Lat"])
df2.to_csv("tom3kmA_long_lat.csv", sep = "\t", header = False, index = False)