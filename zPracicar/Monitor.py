class Monitor:
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño
    def __str__(self):
        return f'id [{self._idMonitor}] de marca {self._marca} con tamaño {self._tamaño}'

if __name__ == '__main__':
    b = Monitor('shupapi', 'xxx')
    print(b)