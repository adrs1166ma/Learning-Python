class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1._nombre = 'Juan Carlos'         # ATRIBUTO ENCAPSULADO   - -   SUGERENCIA DE NO USAR ESTO
persona1.mostrar_detalle()

#.__   DOBLE GUION PARA SER MAS ESTRITOS EN NO CAMBIARLO  --  no se usa comunmente