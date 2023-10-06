import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for _ in range(nr_letters):
    password.append(random.choice(letters))

for _ in range(nr_symbols):
    password.append(random.choice(symbols))

for _ in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
final_password = ''.join(password)

print(f"Your password is: {final_password}")
