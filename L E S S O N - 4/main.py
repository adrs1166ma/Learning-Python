"""
#51. Ciclo While en Python

# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')

contador = 0
while contador < 3:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print('Fin ciclo while')
"""
# ----
"""
#52. Ejercicio Propuesto - Imprimir numeros del 0 al 5
c = 0
max = 5
while c <= max:
    print(c)
    c += 1
else:
    print("")

#----
#53. SOL
"""
# ----
"""
#54. Ej P - Ciclo While Descendente
c = 5
min = 1
while c >= min:
    print(c)
    c -= 1
#----
#55. SOL
"""
# ----
"""
#56. Ciclo for en Python
cadena = 'Hola'
#----------------------------------------------interar = recorrer cada elemento
for letra in cadena:   #----------------------- in = dentro (de cada de elemento)
    print(letra)
else:
    print('Fin ciclo for')
"""
# ----
"""
#57. Palabra breack en Python
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break #----------------------------------------BREAK
else:
    print('Fin ciclo for')
"""
# ----

# 58. Palabra continue en Python

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')
#

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
# ----
