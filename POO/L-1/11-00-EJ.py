#EJ 11
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

b = int(input("Proporciona la base: "))
a = int(input("Proporciona la altura: "))
rectangulo1 = Rectangulo(b, a)
print(f'Area rectangulo: {rectangulo1.area()}')



