def factorial(number):
    total = 1
    for num in range(1, number + 1):
        total *= num
    print(number, "factorial is", total)

number = int(input("Enter a number: "))
factorial(number)

