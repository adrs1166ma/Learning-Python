opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar catálogo películas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4): '))
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None
else:
    print('Salimos del programa...')
