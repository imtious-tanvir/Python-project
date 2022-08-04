number_x = int(input("Enter 1st number "))
number_y = int(input("Enter 2nd number "))
number_z = int(input("Enter 3rd number "))

if number_x > number_y and number_x > number_z:
    print(number_x,"is maximum number")
elif number_y > number_x and number_y > number_z:
    print(number_y,"is maximum number")
else:
    print(number_z, "is maximum number")