#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice
#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla
# frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#eliminar la tupla
del frutas
print(frutas)