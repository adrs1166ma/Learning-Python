class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan', 'Perez', 28)
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
