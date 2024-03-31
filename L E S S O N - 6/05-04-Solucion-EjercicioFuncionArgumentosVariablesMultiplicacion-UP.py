"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
# Definicion de la funcion para multiplicar valores
def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        # resultado = resultado * numero
        resultado *= numero
    return resultado

# Llamada de la funcion
print(multiplicar_valores(3,5,15,3))