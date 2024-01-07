import random
import os

pokracovat = "yes"

def difficulty():
  difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  
while pokracovat == "yes":
    secret_number = random.randint(1, 100)
    print(f"Hádané číslo je {secret_number}")
    print("Vítejte ve hře guess secret number. Porazte počítač.")
    print("Myslím si číslo od 1 do 100")
    pokusy = difficulty()

    while pokusy>0:
        print("Vas pocet zbyvajicich pokusu je:", pokusy)
        tip = int(input("Tipnete si cislo: "))
        if  tip<secret_number:
            print("Prilis nizke")
        elif tip>secret_number:
            print("Prilis vysoke")
        else:
           break
        pokusy-=1

    if tip==secret_number:
        print("Vyhrali jste, pocitac prohral:)")
    else:
        print("Prohrali jste, pocitac vyhral:(")
    pokracovat = input("Napiste yes pro pokracovani, no pro konec: ")
    os.system("cls")