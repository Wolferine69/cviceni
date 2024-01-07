from data import data
import random

def vyber (ucetS=None):
    while True:
        ucet = random.choice(data)
        if ucet != ucetS:
            return ucet

skore = 0
ucetA=vyber()

while True:
    ucetB=vyber(ucetA)

    print(f"Porovnejte A: {ucetA['name']}, {ucetA['description']}, z {ucetA['country']}")
    print(f"Porovnejte B: {ucetB['name']}, {ucetB['description']}, z {ucetB['country']}")

    print(f"Testovaci vypis - ucet 1: {ucetA['follower_count']}")
    print(f"Testovaci vypis - ucet 2: {ucetB['follower_count']}")

    volba=input("Kdo ma vice sledujicich na instagramu? ").lower()

    if (ucetA['follower_count']>ucetB['follower_count'] and volba=="a") or (ucetA['follower_count']<ucetB['follower_count'] and volba=="b"):
        skore+=1
    else:
        break

    print(f"Uhadli jste. Vase skore je {skore}")
    ucetA=ucetB

print(f"To je spatne. Vase konecne skore je {skore}")