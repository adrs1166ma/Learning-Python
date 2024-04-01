#override = sobreescribir
#al no tener ese metodo, nos mandara la info de referencia de memoria de donde se ubica el objeto
#para esto tenemos que mandar una representacion en texto de cada uno de los objetos
#el primer metro str no es necesario volverla a escribir ya que se volvera a sobre escribir en todas las clases hijas
#solo que no tendra acceso a la info de las clases hijas
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado[Sueldo: {self.sueldo}] {super().__str__()} '
    # supes() nos permite acceder a atributos y metodos definidos de la clase padre