# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
"""
5  * 4 
4  * 3 
3  * 2 
2  * 1 

f(n-1) =:n 4
f(n-2) =:n 3
f(n-3) =:n 2
f(n-4) : 1 x


(n)    5  *  4 = 5 * 24 = 120
(n-1) 4  *  3 = 4 * 6 = 24
(n-2) 3  *  2 = 3 * 2 = 6
(n-3) 2  *  1 = 2
"""
numero = 5
resultado = factorial(numero)

print(f'El factorial de {numero} es {resultado}')