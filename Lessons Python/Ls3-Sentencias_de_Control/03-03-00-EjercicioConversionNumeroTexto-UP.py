numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Número proporcionado: {numero} - {numeroTexto}')
