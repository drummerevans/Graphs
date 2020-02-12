import numpy as np
with open('test8a.txt') as f:
   a = f.read()
b = a.split("\r\n")
c=b[0].split(",")
np.float(c[13])