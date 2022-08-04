number1 = input("Enter 1st number: ")
number2 = input("Enter 2nd number: ")

try:
    division = int(number1)/int(number2)
    print(division)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
print("Thank You")