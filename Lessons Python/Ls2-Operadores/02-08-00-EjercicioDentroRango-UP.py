valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

#dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')