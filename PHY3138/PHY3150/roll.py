import numpy as np
import pandas as pd
import math

# below is to be used with the "bankhol.csv" file

raw_data = pd.read_csv("final_test.csv") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'

# new_data = raw_data.sort_values("TIME") # sorted into a time ordered DataFrame

altitude = raw_data["ALTITUDE"].tolist()
roll_ang = raw_data["ROLL"].tolist()

df2 = pd.DataFrame(list(zip(altitude, roll_ang)), columns = ["ALTITUDE", "ROLL"])
df2.to_csv("roll_data.csv", sep = "\t", header = False, index = False)