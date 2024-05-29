"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

def pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

a = float(input('Proporcione el pago sin impuestos: '))
b = float(input('Proporcione el monto del impuesto: '))
total = pago(a, b)
print(f'Tu pago total es de {total}')
