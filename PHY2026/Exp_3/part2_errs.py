l = float(input("Input l " ))
w = float(input("Input w "))
d = float(input("Input d "))
temp_diff = float(input("Input temp average"))

p = 8.96 * (10**3)
c = 384

Q_err1 = ((((w * d * temp_diff)**2 + (l * d * temp_diff)**2 + (l * w * temp_diff)**2)* (4e-10) + (w * d * l)**2 * 0.1**2))**0.5
print(Q_err1)
Q_err = (Q_err1) * p * c

print("Error in Q is: ", Q_err)