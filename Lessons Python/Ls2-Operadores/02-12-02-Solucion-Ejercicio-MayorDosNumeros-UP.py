"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual número es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
"""
numero1 = int(input("Proporciona el Número 1:"))
numero2 = int(input("Proporciona el Número 2:"))

if numero1 > numero2:
    print("Número 1 es mayor")
else:
    print("Número 2 es mayor")
