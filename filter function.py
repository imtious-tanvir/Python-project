import numpy as np
number = np.random.randint(1, 25 , 5)
print("Values are: ",number)

odd_numbers = list(filter((lambda n : n % 2 == 1),number))
even_numbers = list(filter((lambda n : n % 2 == 0),number))
print("Odd numbers are in the list of numbers",odd_numbers)
print("Even numbers are in the list of numbers",even_numbers)