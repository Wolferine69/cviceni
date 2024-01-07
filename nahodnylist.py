import random

jmena = input ("Napis jmena oddele carkou\n")

list_jmena = jmena.split(", ")

print("Platit bude: ",list_jmena[random.randint(0, len(list_jmena)-1)])