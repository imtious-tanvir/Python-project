import numpy as np

a = np.array([
    [12, 8, 4],
    [3, 17, 14],
    [9, 8, 10]
])

b = np.array([
    [5, 19, 3],
    [6, 15, 9],
    [7, 8, 16]
])

add = np.add(a, b)
sub = np.subtract(a, b)
mul = np.dot(a, b)
print("Matrix Numerical Operation")
print(f"{a}+{b}={add}")
print(f"{a}-{b}={sub}")
print(f"{a}*{b}={mul}")
