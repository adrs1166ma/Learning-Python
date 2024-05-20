from logger_base import log
class Persona:
    def __init__(self, idP=None, nombre=None, apellido=None, email=None):
        self._idP = idP
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            ID Persona: {self._idP}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
        '''

    @property
    def idP(self):
        return self._idP
    @idP.setter
    def idP(self, idP):
        self._idP = idP
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    p1 = Persona(1, 'Juan', 'Perez', 'jperez@gmail.com')
    log.debug(p1)

    # Simular un insert
    p2 = Persona(nombre='Ana', apellido='Jimnez', email='ffwa@gmail.com')
    log.debug(p2)

    # Simular un delete
    p3 = Persona(idP=1)
    log.debug(p3)