
# definir tipo de dato

# def sumar(a:int = 0, b:int = 0) -> int:
def sumar(a = 0, b = 0):
    return a + b

resultado = sumar()
print(f'Resultado sumar: {resultado}')

print(f'Resultado sumar: {sumar(2,8)}')

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'María', 'Ernesto')
listarNombres('Laura', 'Carlos')

#Recordar que una tupla es inmutable
