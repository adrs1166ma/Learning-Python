# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
list = []
for i in tupla:
    if i < 5:
        list.append(i)
else:
    print(list)
