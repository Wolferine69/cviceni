itslovnik = {
    "string":"text",
    "float": "desetinne cislo"
}

print(itslovnik["string"])
itslovnik[1] = "cislo"
print(itslovnik)

for key in itslovnik:
    print(key)
    print (" ")
    print(itslovnik[key])
    print ("-------")



denik = {
    "Spain": {"mesta":["Madrid", "Leon"],"navstevy":5},
    "France":{"mesta":["Paris", "Nice"], "navstevy":3}
}

print(denik)
print(denik["France"]["mesta"][1], denik["France"]["navstevy"])