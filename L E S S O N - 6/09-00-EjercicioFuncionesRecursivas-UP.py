"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

Si se pasan valores negativos no imprime nada
"""

def num_des(numero):
    if numero < 1:
        return 1
    else:
        print(numero)
        return num_des(numero - 1)



numero = int(input('Ingresa num para desenderlo: '))
num_des(numero)

