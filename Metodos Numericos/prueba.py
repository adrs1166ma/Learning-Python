import numpy as np

x = [1,2,3,4,5]
y = [4,6,9,12,14]
xint = 8.0

n = len(x)
L = np.zeros(n)
print(L)
print('')
for i in range(0,n):
    L[i] = 1.0
    print(L)
    cont_grado = 0
    for j in range(0,n):
        if i != j:
            cont_grado += 1
            L[i] = L[i] * (xint - x[j])/(x[i] - x[j])
            print(f'({xint} - {x[j]})', end=' ')
            print(f'({x[i]} - {x[j]})')
            #print(f'({xint} - {x[j]})/({x[i]} - {x[j]})', end=' ')
print(f'es de grado {cont_grado}°')
yint = np.sum(L*y)
print(yint)