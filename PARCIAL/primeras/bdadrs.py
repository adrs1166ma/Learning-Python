import sqlite3 as bd

conexion = bd.connect('Mancilla_almacen')
cursor = conexion.cursor()

def tablaExiste(nombreTabla):
    cursor.execute(f'''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nombreTabla}' ''')
    if cursor.fetchone()[0] == 1:
        return True
    else:
        cursor.execute(f'''CREATE TABLE PRODUCTO (idproducto INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nombre TEXT, precio REAL) ''')
        print(f'tabla creada')
        return False

tablaExiste('Producto')     # Creación de la tabla Producto

def insertarProducto(codigo, nombre, precio):
    cursor.execute('''INSERT INTO PRODUCTO (codigo, nombre, precio) VALUES (?,?,?) ''',(codigo,nombre,precio))
    conexion.commit()
    print(f'''Producto agregado:
        [{codigo}]{nombre} : ${precio}''')

def seleccionarProductos():
    cursor.execute('''SELECT * FROM PRODUCTO ''')
    lista = []
    for filaEncontrada in cursor.fetchall():
        lista.append(filaEncontrada)
    return lista

def actualizarProducto(id, diccionario):
    valoresValidos = ['codigo','nombre','precio']
    for key in diccionario.keys():
        if key not in valoresValidos:
            raise Exception('Esa columna no existe')
        else:
            query = f'''UPDATE producto SET {key} = '{diccionario[key]}' WHERE idproducto = {id} '''
            cursor.execute(query)
    conexion.commit()

def borrarProducto(id):
    cursor.execute(f'''DELETE FROM producto WHERE idproducto = {id} ''')
    conexion.commit()

def menuPrincipal():
    while True:
        print("\n[ Menú Opciones ]")
        print("1. Registrar")
        print("2. Eliminar")
        print("3. Editar")
        print("4. Listar")
        print("5. Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            insertarProducto(codigo, nombre, precio)
        elif opcion == 2:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            borrarProducto(id)
        elif opcion == 3:
            id = int(input("Ingrese el ID del producto a editar: "))
            codigo = input("Ingrese el nuevo código del producto (opcional): ")
            nombre = input("Ingrese el nuevo nombre del producto (opcional): ")
            precio = input("Ingrese el nuevo precio del producto (opcional): ")
            diccionario = {}
            if codigo:
                diccionario['codigo'] = codigo
            if nombre:
                diccionario['nombre'] = nombre
            if precio:
                diccionario['precio'] = precio
            actualizarProducto(id, diccionario)
        elif opcion == 4:
            productos = seleccionarProductos()
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n[ Lista de Productos ]")
                for producto in productos:
                    print(f"ID: {producto[0]} | Código: {producto[1]} | Nombre: {producto[2]} | Precio: ${producto[3]}")
        elif opcion == 5:
            print("¡Gracias por usar este programa!")
            conexion.close()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menuPrincipal()
