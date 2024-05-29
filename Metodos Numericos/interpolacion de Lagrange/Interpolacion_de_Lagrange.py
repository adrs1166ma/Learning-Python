import numpy as np


def InterLagrange(x,y,xint):
    n = len(x)
    L = np.zeros(n)
    for i in range(0,n):
        L[i] = 1.0
        for j in range(0,n):
            if i != j:
                L[i] = L[i] * (xint - x[j])/(x[i] - x[j])

    yint = np.sum(L*y)
    print(yint)
    return yint

x = [1,2,3,4,5]
y = [4,6,9,12,14]
xint = 8.0

val_inter = InterLagrange(x,y,xint)
print(f'El valor de y usando un valor de x igual a {xint:.2f} es {val_inter:.2f}')