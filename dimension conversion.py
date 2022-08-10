import numpy as np

one_arr = np.random.randint(1, 25, 12)
print(f"One Dimension array is = {one_arr}")
two_arr = one_arr.reshape(2, 6)
print(f"Two Dimension array is = {two_arr}")
three_arr = one_arr.reshape(2, 2, 3)
print(f"Three Dimension array is = {three_arr}")
again_one_arr_from_three = three_arr.flatten()
print(f"Again One Dimension from three is = {again_one_arr_from_three}")
again_one_arr_from_two = two_arr.flatten()
print(f"Again One Dimension from two is = {again_one_arr_from_two}")