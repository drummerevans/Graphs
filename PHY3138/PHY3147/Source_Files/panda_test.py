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