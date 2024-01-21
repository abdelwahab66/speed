import random

print("your pass is : ")

d = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$^&*"

password = ""

for i in range(16):
    password += random.choice(d)

print(password)
