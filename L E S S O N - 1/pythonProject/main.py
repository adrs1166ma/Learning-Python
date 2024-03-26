"""
x: int = 10  # " :str o :int " es como un comentario o indicador
print(x)
print(type(x))

x = True  # Cuidado con poner todo minusculas
print(x)
print(type(x))
## vd 13. Tipos de Datos en Python


# Tipo int
x = 10
print(x)
print(type(x))

# Tipo float
x = 14.5
print(type(x))

# Tipo String
x = "Hola Mundo"
print(type(x))

# Tipo bool
x = True
print(type(x))
x = False
print(type(x))
## vd 14. Resumen Tipos de Datos en Python
"""
##------------------------------------------------------------------------
"""

# Cadena (String) y concatenar


miGrupoFavorito = "Grupo5"
print("Mi grupo favorito es: " + miGrupoFavorito)

miGrupoFavorito = "Grupo5" + " " + "The best Salsa Band"
print("Mi grupo favorito es: " + miGrupoFavorito)

miGrupoFavorito = "Grupo5"
comentario = "The best Salsa Band"

print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)

## vd 15. Menjo de Cadenas en Python
##------------------------------------------------------------------------

print("Mi grupo favorito es:", miGrupoFavorito, comentario)

# Error string
n1 = "1"  # "uno" x  tiene que ser un valor valido
n2 = "2"

print("Concatenacion:", n1 + n2)

print("Suma:", int(n1) + int(n2))

# Good
n1 = 1
n2 = 2
print(n1 + n2)

## vd 16. Mas Temas de Manejo de Cadenas


"""
##------------------------------------------------------------------------
"""

# Tipos bool (bool) nos permite tomar decision, ya sea False or True
miVariable = False
print(miVariable)

miVariable = 4 > 2
print(miVariable)

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")
## vd 17. Tipos de Boleanos (bool) en Python


"""
##------------------------------------------------------------------------

"""
#Funcion input para procesar la entrada del usuario


resultado = input("Escribe un mensaje: ") #la funcion input regresa un str
print("El valor proporsionado:", resultado)
print("Fin del programa")
## vd 18. Procesar Entrada del Usuario (Funcion input)
"""
##------------------------------------------------------------------------

"""
#COMBERTIR A ENTERO - INT

n1 = int(input("Escribe el primer numero: "))
n2 = int(input("Escribe el segundo numero: "))
r = n1 + n2
print("El resultado de la suma es:", r)

## vd 19. Conversion de la Entrada de Datos en python
"""
##------------------------------------------------------------------------

"""
# Califica tu dia del 1 al 10
r = int(input("Como estuvo tu dia del (1 al 10): "))
print("Mi dia estuvo de:", r)

## vd 20. E J E R C I C I O : Califica tu Dia
## vd 21. Sol
"""
##------------------------------------------------------------------------

# Se solicita incluir la siguiente info acerca de un libro:
# titulo
# autor
# debes imprimir la info en el siguiente formato:
# Proporciona el titulo:
# Proporciona el autor:
# <titulo> fue escrito por <autor>

t = input("Proporciona el titulo:")
a = input("Proporciona el autor:")

print(t, "fue escrito por", a)

## vd 22. E J E R C I C I O : Detalles de un Libro
## vd 23. sol
