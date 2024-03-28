"""
#42. Sentencia if/Else en Pytohn

condicion = True # or 10 , False = '' , False = 'hola'

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion no reconocida')
"""
#----
"""
#43. Ejecucion Modo Debug (Paso a Paso) en Sentencia if/Else
"""
#----
"""
#44. Ejercicio - Conversion de Numero a Texto en Python
n = int(input('Proporciona un valor entre 1 y 3: '))
nT = ''
if n == 1:
    nT = 'Numero uno'
elif n == 2:
    nT = 'Numero dos'
elif n == 2:
    nT = 'Numero dos'
else:
    nT = 'Valor fuera de rango'

print(f'Numero proporcionado: {n} - {nT}')
"""
#----
"""
#45. Sintaxis if else simplificada (Operador Ternario)

c = True
# if c:
#     print('Condicion verdadera')
# else:
#     print('Condicion falsa')

print('Condicion verdadera') if c else print('Condicion falsa')
"""
#----
"""
#46. Ejercicio - Calcular la Estacion segun el Mes proporcionado
mes = int(input('Proporciona mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estacion es: {estacion}')
"""
#----
"""
#47. Ejercicio a desarrollar:Etapas de Vida segun Edad
e = int(input('Proporciona tu edad: '))
eT = None
if 0 <= e < 10:
    eT = 'La infancia es increible...'
elif 10 <= e < 20:
    eT = 'Muchos cambios y mucho estudio...'
elif 20 <= e < 30:
    eT = 'Amor y comienza el trabajo...'
else:
    eT = 'Etapa de vida no reconocida'

print(f'Tu edad es {e}, {eT}')
#----
#48. SOL
"""
#----

#49. Ej P - Sistema de Calificaciones
nota = int(input('Ingresa tu nota del 0 al 10: '))
calificacion = None
if nota == 10 or nota == 9:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'F'
else:
    calificacion = 'valor incorrecto, Proporcion un valor entre 0 y 10:'

print(calificacion)
#50. SOL