class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def volumen(self):
        return self.ancho * self.alto * self.profundo
a = int(input('el ancho: '))
a1 = int(input('el alto: '))
p = int(input('lo profundo: '))
cubo1 = Cubo(a,a1,p)
print(f'Su volumen es {cubo1.volumen()} m3')