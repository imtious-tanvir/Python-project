import numpy as np
def mul_five_times(num):
    return num * 5

values = np.random.randint(1, 10, 5)
result = []
print("Primary list ",values)

for value in values:
    result.append(mul_five_times(value))
print("After multiplication with 5",result)

result = list(map(mul_five_times, values))
print("After multiplication with 5",result)