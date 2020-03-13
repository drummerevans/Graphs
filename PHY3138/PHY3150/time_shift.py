import pandas as pd
import numpy as np

radio_data = pd.read_csv("radio_roll_trial.csv", index_col = False)

# ADS-B assignments
radio_t = radio_data["TIMESTAMP"].tolist()
radio_roll = radio_data["ROLL"].tolist()

new_times = []
for i in range(0, len(radio_t)):
    new_times.append(radio_t[i] - 628)

radio_time_roll = pd.DataFrame(list(zip(new_times, radio_roll)), columns = ["time", "roll"])
radio_time_roll.to_csv("calibrated_times.csv", sep = "\t", header = False, index = False)