"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
# Si esta entre 9 y 10 imprimir: A
if 9 <= calificacion <= 10:
    print("A")
# Si esta entre  8 y menor a 9 imprimir: B
elif 8 <= calificacion < 9:
    print("B")
# Si esta entre 7 y menor a 8 imprimir: C
elif 7 <= calificacion < 8:
    print("C")
# Si esta entre 6 y menor a 7 imprimir: D
elif 6 <= calificacion < 7:
    print("D")
# Si esta entre 0 y menor a 6 imprimir: F
elif 0 <= calificacion < 6:
    print("F")
# Si no esta en el rago, imprimir: Valor desconocido
else:
    print("Valor desconocido")
