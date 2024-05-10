from dE import *
class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclados += 1
        self._idTeclados = Teclado.contadorTeclados
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'id [{self._idTeclados}] {DispositivoEntrada.__str__(self)}'

if __name__ == '__main__':
    b = Teclado('mierda', 'gampi' )
    print(b)