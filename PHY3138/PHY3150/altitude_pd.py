import numpy as np
import pandas as pd
import math

# below is to be used with the "bankhol.csv" file

raw_data = pd.read_csv("U2402_1218.csv") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'

# new_data = raw_data.sort_values("TIME") # sorted into a time ordered DataFrame

time = raw_data["Adjusted Timestamp"].tolist()
altitude = raw_data["Altitude"].tolist()

df2 = pd.DataFrame(list(zip(time, altitude)), columns = ["Adjusted_Timestamp", "Altitude"])
df2.to_csv("plane5.csv", sep = "\t", header = False, index = False)