"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
def ce_a_fa(t):
    t_fa=(t * 9/5) + 32
    return t_fa
def fa_a_ce(t):
    t_ce=(t - 32) * (5/9)
    return t_ce

a = float(input('Ingrese grados celsius: '))
b = float(input('Ingrese grados fahrenheit: '))
x = ce_a_fa(a)
y = fa_a_ce(b)

print(f'La temperatura en grados fahrenheit es {x}')
print(f'La temperatura en grados celsius es {y}')