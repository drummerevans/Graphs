import pandas as pd
import numpy as np

data = pd.read_csv("optical_data7.csv", index_col = False) # optical data
radio_data = pd.read_csv("tom3kmA.csv", index_col = False) # ADS-B data

# optical assignments
rows1 = data.iloc[0::2]
rows2 = data.iloc[1::2]

x1 = rows1["x"].tolist()
y1 = rows1["y"].tolist()
f1 = rows1["frame"].tolist()
w1 = rows1["w"].tolist()
h1 = rows1["h"].tolist()

x2 = rows2["x"].tolist()
y2 = rows2["y"].tolist()
f2 = rows2["frame"].tolist()
w2 = rows2["w"].tolist()
h2 = rows2["h"].tolist()

# ADS-B assignments
radio_t = radio_data["TIMESTAMP"].tolist()
radio_roll = radio_data["ROLL"].tolist()

new_times = []
for i in range(0, len(radio_t)):
    new_times.append(radio_t[i] - 628)

radio_time_roll = pd.DataFrame(list(zip(new_times, radio_roll)), columns = ["time", "roll"])
radio_time_roll.to_csv("radio_dat.csv", sep = "\t", header = False, index = False)


# optical filtering
times1 = []
times2 = []
x1c = []
y1c = []
x2c = []
y2c = []
for i in range(0, len(f1)):
    times1.append(f1[i]/25)
    times2.append(f2[i]/25)
    x1c.append(x1[i] + w1[i] / 2)
    y1c.append(y1[i] - h1[i] / 2)
    x2c.append(x2[i] + w2[i] / 2)
    y2c.append(y2[i] - h2[i] / 2)

frame = []
roll = []
counter = 0
for i in range(0, len(x1)):
    # if y1c[i] - y2c[i] != 0:
    counter += 1
    frame.append(counter)
    # roll.append(np.arctan((x1[i]-x2[i])/(y1[i]-y2[i])))
    roll.append((180/np.pi)*np.arctan(y1c[i]-y2c[i])/(x1c[i]-x2c[i]))


new_rows1 = pd.DataFrame(list(zip(x1, y1, w1, h1)), columns = ["x", "y", "w", "h"])
new_rows2 = pd.DataFrame(list(zip(x2, y2, w2, h2)), columns = ["x", "y", "w", "h"])

new_rows1.to_csv("left_wing.csv", sep = "\t", header = False, index = False)
new_rows2.to_csv("right_wing.csv", sep = "\t", header = False, index = False)

frame_roll = pd.DataFrame(list(zip(times1, roll)), columns = ["time", "roll"])
frame_roll.to_csv("optical_roll7.csv", sep = "\t", header = False, index = False)

