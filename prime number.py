number = int(input("Enter a number: "))
div = 0
factor = []
for num in range(1, number+1):
    if number % num == 0:
        div += 1
        factor.append(num)
if div == 2:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
    print(number,"factors are ",factor)