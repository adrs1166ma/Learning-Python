import numpy as np

x = [1, 2, 3, 4, 5]
y = [4, 6, 9, 12, 14]
xint = 8.0

n = len(x)
L = np.zeros(n)
cont_grado = 0
for i in range(n):
    L[i] = 1.0
    numerador = ''
    denominador = ''
    cont_grado += 1
    for j in range(n):
        if i != j:
            # Construye la parte del numerador y el denominador
            numerador += f'({xint} - {x[j]})'
            denominador += f'({x[i]} - {x[j]})'
            L[i] = L[i] * (xint - x[j]) / (x[i] - x[j])
    # Imprime las fracciones alineadas
    print(numerador)
    print('-' * max(len(numerador), len(denominador)),end=f' = {L[i]}\n')
    print(denominador)
    print('\n')

print(*L, sep='] + [')
yint = np.sum(L * y)
#60 -420 1134 -1260 490
print(f'El resultado es = {yint}\n')
print(f'Es de grado {cont_grado}°\n')
