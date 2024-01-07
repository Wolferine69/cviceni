import os
def calculator (x,y,operator):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator == "/":
        return x/y
    else :
        return "Neplatna operace!"

cont="ne"

while cont=="ne":
    cont="ano"
    first_number = int(input("Zadejte prvni cislo: "))
    
    while cont=="ano":
        operation = input("+\n-\n*\n/\nZvolte jednu z uvedenych operaci: ")
        second_number = int(input("Zadejte druhe cislo: "))
        vysledek=calculator(first_number,second_number,operation)
        print(f"Vysledek je: {vysledek}")
        if vysledek != "Neplatna operace!":
            first_number=vysledek
        cont=input("Chcete pokracovat v kalkulaci? ano/ne/konec:")
    os.system("cls")

# Calculator


import os


def sum(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
   
    num1 = float(input("Jaká je první číslo? "))


    lets_continue = "ano"


    while lets_continue == "ano":
        for symbol in operations:
            print(symbol)


        user_symbol = input("Zvolte jednu z operací výše: ")
        num2 = float(input("Jaké je další číslo? "))


        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)


        print(f"{num1} {user_symbol} {num2} = {result}")
        lets_continue = input("Napište ano, pokud chcete pokračovat. Napište ne, pokud chcete kalkulátor spustit znovu ")
        if lets_continue == "ano":
            num1 = result
        else:
            # lets_continue = "ne"
            os.system("clear")
            calculator()


calculator()
