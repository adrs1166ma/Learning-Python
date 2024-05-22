from logger_base import log

class Producto:
    def __init__(self, idproducto=None, codigo=None, nombre=None, precio=None):
        self._idproducto = idproducto
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'''
            ID Producto: {self._idproducto}, codigo: {self._codigo},
            Nombre: {self._nombre}, Precio: {self._precio}
        '''

    @property
    def idproducto(self):
        return self._idproducto
    @idproducto.setter
    def idproducto(self, idproducto):
        self._idproducto = idproducto
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

if __name__ == '__main__':
    p1 = Producto(1, 'XXA', 'Ace', '29')
    log.debug(p1)

    # Simular un insert
    p2 = Producto(codigo='XXC', nombre='Ore', precio='2.50')
    log.debug(p2)

    # Simular un delete
    p3 = Producto(idproducto=1)
    log.debug(p3)