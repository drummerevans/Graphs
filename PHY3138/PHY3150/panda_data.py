import numpy as np
import pandas as pd
import math
import time
from datetime import datetime

raw_data = pd.read_csv("fivefloor.avionics.csv", sep = " ") # reads in values from a csv with spaces (not commas) to a DataFrame 'raw_data'


roll = raw_data["ROLL"].tolist()
r_track = raw_data["RTRACK"].tolist()
altitude = raw_data["ALTITUDE"]
gs = raw_data["GS"].tolist()
air_speed = raw_data["AS"].tolist()

new_roll = []
new_r_track = []
new_altitude = []
new_gs = []
new_air_speed = []
new_gtan = []



for i in range(0, len(roll)):
    if (roll[i] == 0 and r_track[i] == 0):
        if air_speed[i] != 0:
            new_roll.append(roll[i])
            new_r_track.append(r_track[i])
            new_altitude.append(altitude[i])
            new_gs.append(gs[i])
            new_air_speed.append(air_speed[i])
            new_gtan.append(((9.81 * np.tan(roll[i] * (np.pi / 180))) / (air_speed[i] * 0.514444)) * 180/(np.pi))
    if (roll[i] != 0 and r_track[i] != 0):
        if air_speed[i] != 0:
            new_roll.append(roll[i])
            new_r_track.append(r_track[i])
            new_altitude.append(altitude[i])
            new_gs.append(gs[i])
            new_air_speed.append(air_speed[i])
            new_gtan.append(((9.81 * np.tan(roll[i] * (np.pi / 180))) / (air_speed[i] * 0.514444)) * 180/(np.pi))


temp_df2 = pd.DataFrame(list(zip(new_roll, new_gtan, new_r_track, new_gs, new_air_speed, new_altitude)), columns = ["ROLL", "G_TAN", "RTRACK", "GS", "AS", "ALTITUDE"])
df2 = temp_df2.dropna() # removes rows with NaN values from the DataFrame
# df2.to_csv("fivefloor_extracted2.csv", sep = ",", header = True, index = False) # use for TopCat to give headers and comma separated file
df2.to_csv("fivefloor_extracted3.csv", sep = "\t", header = False, index = False)