class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan', 'Perez', 28) # crear obejo con su constructor
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)