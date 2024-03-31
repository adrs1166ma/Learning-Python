#atributos con nuestros objetos
#self : uno mismo      __ = dunder / double underscore
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def desplegar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


persona1 = Persona('Juan', 28)
persona1.desplegar()
persona2 = Persona('Karla', 30)
persona2.desplegar()
