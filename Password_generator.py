import random

print("Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*(),./'

number = input("Number of passwords: ")
number = int(number)

length = input("Lenght of the password: ")
length = int(length)

print("Your passwords are: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)