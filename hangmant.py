import random

slova = ["harry", "ron", "brumbal", "albus", "hermiona", "draco", "ronald"]
slovo = list(random.choice(slova))
zivoty = 6
print(slovo)

skryte = []
for podtrzitko in slovo:
    skryte.append("_")
print ("".join(skryte))

while "_" in skryte and zivoty !=0:
    tip = input("Zadejte hadane pismeno: ").lower()
    for index in range(0, len(slovo)):
        if tip == slovo[index]:
            skryte[index]=slovo[index]
    if tip not in slovo:
            zivoty -=1
    print("Pocet zivotu:", zivoty)
    print ("".join(skryte))

if "_" not in skryte:
     print("Vyhrali jste!!")
else:
     print("Dosli vam zivoty:(")