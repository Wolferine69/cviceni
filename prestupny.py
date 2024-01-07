year = int(input("Jaký rok chcete zkontrolovat? "))
month = int(input("Zadej mecis ke kontrole: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
def prestupny (rok):
    """Vrati jestli je rok prestupy"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("přestupný")
            else:
                return("nepřestupný")
        else:
            return("přestupný")
    else:
        return("nepřestupný")   #nemusi byt zavorky

def dnu(mesic):
    if rok == "přestupný" and mesic==2:
        return 29
    else:
        return days_in_month[mesic-1]

rok = prestupny(year)
pocet_dnu = dnu(month)

print(f"Zadal jste {rok} rok takze mesic ma {pocet_dnu} dnu")