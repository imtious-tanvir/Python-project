import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']
password_list = []
password = ''

print("WELCOME TO PYPASSWORD GENARATOR!")
ip_letter = int(input('How many letters you want to wish:\n'))
ip_number = int(input('How many numbers you want to wish:\n'))
ip_symbols = int(input('How many symbols you want to wish:\n'))

for char in range(ip_letter):
    random_letters = random.choice(letters)
    password_list.append(random_letters)

for char in range(ip_number):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

for char in range(ip_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

random.shuffle(password_list)
for char in password_list:
    password += char
print(password)