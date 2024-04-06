print('Proporcione los siguientes datos del libro: ')
nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('Proporciona el valor de libro: '))
envioGratuito = input('Indica si es envío gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío Gratuito?: {envioGratuito}
''')