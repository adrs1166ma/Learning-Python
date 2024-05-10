class Orden:
    cO = 0
    def __init__(self, computadoras):
        Orden.cO += 1
        self._idO = Orden.cO
        self._computadoras = computadoras
    def agregar(self, computadora):
        self._computadoras.append(computadora)
    def __str__(self):
        pc_str = ''
        for computadora in self._computadoras:
            pc_str += computadora.__str__()
        return (
                f"Orden: {self._idO}, "
                f"computadoras: {pc_str}"
        )



