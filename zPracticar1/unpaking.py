numeros = [1,2,3,4]

print (numeros)
print (*numeros)
print (*numeros,'-')

def suma(a,b,c):
    e = a + b
    print(f'este weon saco = {e} y la rptta es {c}')

suma(*numeros)