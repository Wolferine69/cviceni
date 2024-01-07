import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

heslo = []
pismena = int(input("Kolik chcete pismen?\n"))
cisla = int(input("Kolik chcete cislic?\n"))
special = int(input("Kolik chcete specialnich znaku?\n"))

for pismeno in range(0,pismena):
    heslo.append(random.choice(letters))

for cislo in range(0,cisla):
    heslo.append(random.choice(numbers))

for spec in range(0,special):
    heslo.append(random.choice(special_char))

print (heslo)
random.shuffle(heslo)
print ("".join(heslo))