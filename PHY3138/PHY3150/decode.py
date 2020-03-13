import numpy as np
import pandas as pd
import math

# reads in values from a csv with a Byte Order Mark (BOM) and decodes it
raw_data = pd.read_csv("test14_1.csv", encoding = 'UTF-16') 

# dropping ALL duplicte values 
# raw_data.drop_duplicates() 
print(raw_data.head())

# sends the decoded file to a csv
new_data = raw_data.to_csv("decoded_test14.csv", index = False) 