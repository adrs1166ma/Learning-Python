## 24. Operadores Aritmeticos en Python
# ----------------------------------------------------------------------------------
"""
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('Resultado suma:', suma)
print(f'Resultado suma: {suma}') #interpolacion - incluir variables en una cadena


## 25. parte 2
#----------------------------------------------------------------------------------

resta = operandoA - operandoB
print(f'Resultado de la resta: {resta}')
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicacion: {multiplicacion}')
division = operandoA / operandoB
print(f'Resultado division: {division}')
division = operandoA // operandoB
print(f'Resultado division (int): {division}')
modulo = operandoA % operandoB
print(f'Resultado residuo division (modulo): {modulo}')
exponente = operandoA ** operandoB
print(f'Resultado exponente: {exponente}')
"""

## 26. Ejercicio Propuesto - Rectangulo  | 27. SOL
# ----------------------------------------------------------------------------------
"""
Instrucciones de la tarea
- En el ejercicio se solicita calcular el area y el perimetro de un Rectangulo,
para ello deberemos crear las siguientes variables:

alto (int)
ancho (int)

- El usuario debe proporcionar los valores de largo y ancho,
y despues se debe imprimir el resultado en el siguiente formato
"""
# a = int(input("Proporciona el alto del rectangulo: "))
# b = int(input("Proporciona el ancho del rectangulo: "))
# area = a * b
# perimetro = (a + b) * 2
# print(f'Area: {area}')
# print(f'Perimetro: {perimetro}')


## 28. Operadores de Asignacion en Python
# ----------------------------------------------------------------------------------
"""
miVariable = 10
print(miVariable)

miVariable = miVariable + 1
print(miVariable)

#incremetnro con reasignacion
miVariable += 1
print(miVariable)

# miVariable = mi Variable - 2
miVariable -= 2
print(miVariable)

#miVariale = miVariable * 3
miVariable *= 3
print(miVariable)

miVariable /= 2
print(miVariable)
"""

## 29. Operadores de Comparacion en Python
# ----------------------------------------------------------------------------------
"""
a = 4
b = 2

r = a == b
print(f'Resultado == : {r}')

r = a != b
print(f'Resultado != : {r}')

r = a > b
print(f'Resultado > : {r}')

r = a >= b
print(f'Resultado >= : {r}')

r = a < b
print(f'Resultado < : {r}')

r = a <= b
print(f'Resultado <= : {r}')
"""

## 30. Ejercicio Numero Par o Impar en Python
# ----------------------------------------------------------------------------------
"""
a = int(input('Por favor ingrese un numero: '))
if a % 2 == 0 :
    print(a, 'es un numero par')
else:
    print(a, 'no es un numero par')
"""

## 31. Ejercicio Determina si es Mayor de Edad
# ----------------------------------------------------------------------------------
"""
eAdulto = 18
e = int(input('Escribe tu edad: '))
print(f'Tu edad es {e}')

if e >= eAdulto:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')
"""

## 32. Operadores Logicos en Python
# ----------------------------------------------------------------------------------
# AND -> a and b, los 2 tienen que ser True para ser True
# OR -> a or b, al menos uno ya es True
"""
a = True
b = False

r = a and b
print(r)

r = a or b
print(r)

r = not a
print(r)
"""

## 33. Ejercicio - Valor dentro de Rango
# ----------------------------------------------------------------------------------
"""
n = int(input('Ingresa numero: '))
print('Rango de 0 a 5')
#dentroRango = (n >= 0) and (n <= 5)
if n >= 0 and n <= 5 :
    print(f'el numero {n} esta dentro del rango')
else:
    print(f'el numero {n} no esta dentro del rango')
"""

## 34. Ejercicio - Operador or
# ----------------------------------------------------------------------------------
"""
vacaciones = False
diaDescanso = True

if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')


## 35. Ejercicio - Operador not
# ----------------------------------------------------------------------------------
if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')
"""

## 36. Ejercicio - Rango entre 20´s y 30´s
# ----------------------------------------------------------------------------------
"""
edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    print("Dentro de rango 20's o 30's") # el para intidar que el es un caracter especial
    if veintes:
        print("Dentro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
else:
    print("No esta dentor de los 20's ni 30's'")




## 37. Sintaxis Simplificada Operador And
# ----------------------------------------------------------------------------------

if  (20 <= edad < 30) or (30 <= edad < 40):
    print("Dentro de rango 20's o 30's")
else:
    print("No esta dentor de los 20's ni 30's'")
"""

## 38. Ejercicio Propuesto - El mayor de dos numeros | 39. SOL
# ----------------------------------------------------------------------------------
"""
n1 = int(input('Proporciona el numero 1: '))
n2 = int(input('Proporciona el numero 2: '))

if n1 > n2:
    print(f'el numero mayor es n1: {n1}')
else:
    print(f'el numero mayor es n2: {n2}')
"""



## 40. Ejercicio a desarrollar: tienda de Libros | 41. SOL
# ----------------------------------------------------------------------------------

print('Proporcione los siguientes datos del libro: ')

n = input('Proporciona el nombre: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el Precio: '))
free = input('Indica si el envio es gratuito (True/False): ')

if free == 'True':
    free = True
elif free == 'False':
    free = False
else:
    free = 'Valor incorrecto, debe escribir True/False'

print(f'''
    Nombre: {n}
    Id : {id}
    Precio: {precio}
    Envio Gratuito?: {free}
''')

