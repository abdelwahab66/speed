import random
import string

# here to turn all into list
all = string.ascii_letters + string.digits + string.punctuation + " "
all = list(all)

key = all.copy()
random.shuffle(key)

plat = input("enter your txt : ")
deplat = ""

for letter in plat:
    id = all.index(letter)
    deplat += key[id]

print(f"your txt is : {deplat}")

# de

deplat = input("enter your txt : ")
plat = ""

for letter in deplat:
    id = key.index(letter)
    plat += all[id]

print(f"your txt is : {plat}")
