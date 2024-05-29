edad = int(input('Proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif  10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio...'
elif  20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida NO reconocida'
print(f'Tu edad es: {edad}, {mensaje}')