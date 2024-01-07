import os
aukce = {}
next = "ano"
vyherce=""
prihoz=0

print("Vitejte v tiche aukci")

while next.lower() == "ano":
    jmeno = input("Jake je vase jmeno?: ")
    castka = input("Jaka je vase nabidka v dolarech?: ")
    next = input("Je dalsi nabizejici? (ano/ne): ")
    os.system("cls")

    aukce[jmeno]=castka

for zaznam in aukce:
    if int(aukce[zaznam]) > prihoz:
        vyherce=zaznam
        prihoz = int(aukce[zaznam])
    elif int(aukce[zaznam]) == prihoz:
        vyherce +=" a "
        vyherce +=zaznam


print(f"Vyherce aukce se stava {vyherce} s prihozem {prihoz}. Gratulujeme!")