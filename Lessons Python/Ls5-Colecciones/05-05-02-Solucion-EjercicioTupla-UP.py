# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

# Definir la lista
lista = []
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

# Imprimimos la lista
print(lista)

