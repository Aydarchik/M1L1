import random

letters = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
lword = int(input('какую длину пароля вы хотите?'))
password = ''
for i in range(lword):
    password += random.choice(letters)

print(password)
