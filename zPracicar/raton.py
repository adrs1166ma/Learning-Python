from dE import *
class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(tipoEntrada, marca)
    def __str__(self):
        return f'id [{self._idRaton}] {DispositivoEntrada.__str__(self)}'

if __name__ == '__main__':
    c = Raton('pura', 'mierda')
    d = Raton('pura', 'mierda')
    print(c)
    print(d)