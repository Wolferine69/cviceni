MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
 
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}

def report(data):
    print(f"Voda: {data["water"]}")
    print(f"Mléko: {data["milk"]}")
    print(f"Kafe: {data["coffee"]}")

def espresso(data,druh):
    if druh["ingredients"]["water"]<=data["water"] and druh["ingredients"]["milk"]<=data["milk"] and druh["ingredients"]["coffee"]<=data["coffee"]:
        print("Na vas napoj mame dostatek ingredienci.")
        zaplaceno=platba()
        druh["cost"]
        print("Cena espressa je:",druh["cost"])
        if zaplaceno>=druh["cost"]:
            print("Napoj se pripravuje.")
            print("Zde jsou penize zpet:", zaplaceno - druh["cost"])
        else:
            print("Vlozili jste malo penez.")
            print("Zde jsou penize zpet:", zaplaceno)
            return
        data["water"]-=druh["ingredients"]["water"]
        data["milk"]-=druh["ingredients"]["milk"]
        data["coffee"]-=druh["ingredients"]["coffee"]
        return (data)
    else:
        raise StopIteration

def latte(data,druh):
    if druh["ingredients"]["water"]<=data["water"] and druh["ingredients"]["milk"]<=data["milk"] and druh["ingredients"]["coffee"]<=data["coffee"]:
        print("Na vas napoj mame dostatek ingredienci.")
        zaplaceno=platba()
        druh["cost"]
        print("Cena latte je:",druh["cost"])
        if zaplaceno>=druh["cost"]:
            print("Napoj se pripravuje.")
            print("Zde jsou penize zpet:", zaplaceno - druh["cost"])
        else:
            print("Vlozili jste malo penez.")
            print("Zde jsou penize zpet:", zaplaceno)
            return
        data["water"]-=druh["ingredients"]["water"]
        data["milk"]-=druh["ingredients"]["milk"]
        data["coffee"]-=druh["ingredients"]["coffee"]
        return (data)
    else:
        raise StopIteration
 
def cappuccino(data,druh):
    if druh["ingredients"]["water"]<=data["water"] and druh["ingredients"]["milk"]<=data["milk"] and druh["ingredients"]["coffee"]<=data["coffee"]:
        print("Na vas napoj mame dostatek ingredienci.")
        zaplaceno=platba()
        druh["cost"]
        print("Cena cappucicina je:",druh["cost"])
        if zaplaceno>=druh["cost"]:
            print("Napoj se pripravuje.")
            print("Zde jsou penize zpet:", zaplaceno - druh["cost"])
        else:
            print("Vlozili jste malo penez.")
            print("Zde jsou penize zpet:", zaplaceno)
            return
        data["water"]-=druh["ingredients"]["water"]
        data["milk"]-=druh["ingredients"]["milk"]
        data["coffee"]-=druh["ingredients"]["coffee"]
        return (data)
    else:
        raise StopIteration
    
def platba():
    print("Prosim, vlozte mince 1, 2, 5, 10, 20, 50")
    zaplaceno=int(input("Kolik 1 Kc chcete vlozit?: "))
    zaplaceno+=(int(input("Kolik 2 Kc chcete vlozit?: "))*2)
    zaplaceno+=(int(input("Kolik 5 Kc chcete vlozit?: "))*5)
    zaplaceno+=(int(input("Kolik 10 Kc chcete vlozit?: "))*10)
    zaplaceno+=(int(input("Kolik 20 Kc chcete vlozit?: "))*20)
    zaplaceno+=(int(input("Kolik 50 Kc chcete vlozit?: "))*50)
    return zaplaceno

mapovani_funkci = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}

while True:
    choice=input("Co byste si dal? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report(resources)
    elif choice in mapovani_funkci:
        vybrana_funkce = mapovani_funkci[choice]
        try:
            resources = vybrana_funkce(resources,MENU[choice])
        except StopIteration:
            print("Nemame dostatek ingredienci na tento napoj.")
            break
    else:
        print("Neplatny vstup!")
        break