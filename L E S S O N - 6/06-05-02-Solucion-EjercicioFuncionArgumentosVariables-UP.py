"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""


# Definimos nuestra funcion para sumar valores
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado


# Llamada a la funcion
print(sumar_valores(3, 5, 9, 4, 6))
