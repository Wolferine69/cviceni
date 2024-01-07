example = "Testovaci veta ve ktere budeme hledat!"
search = "e"
where = ""

index = 0
index_helper = 0
x=0

while x !=-1:
    index = example[index_helper:].find(search)
    where = where + str(index+index_helper) + " "
    index_helper = index + index_helper + 1
    x = index


print(where)