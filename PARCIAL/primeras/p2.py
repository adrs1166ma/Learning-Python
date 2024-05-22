import sqlite3 as bd
import textwrap

# ... (Funciones tablaExiste, insertarProducto, actualizarProducto, borrarProducto) ...

conexion = bd.connect('Mancilla_almacen')
cursor = conexion.cursor()

def tablaExiste(nombreTabla):
    cursor.execute(f'''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{nombreTabla}' ''')
    try:
        if cursor.fetchone()[0] == 1:
            return True
        else:
            cursor.execute(f'''CREATE TABLE PRODUCTO (idproducto INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nombre TEXT, precio REAL) ''')
            print(f'tabla creada')
            return False
    except Exception as e:
        return f'se encontro una excep: {e}'

tablaExiste('Producto')     # Creación de la tabla Producto


def insertarProducto(codigo, nombre, precio):
    cursor.execute('''INSERT INTO PRODUCTO (codigo, nombre, precio) VALUES (?,?,?) ''',(codigo,nombre,precio))
    conexion.commit()
    print(f'''Producto agregado:
        [{codigo}]{nombre} : ${precio}''')

#def seleccionarProductos():
#    cursor.execute('''SELECT * FROM PRODUCTO ''')
#    lista = []
#    for filaEncontrada in cursor.fetchall():
#        lista.append(filaEncontrada)
#    return lista
def seleccionarProductos():
    cursor.execute('''SELECT * FROM PRODUCTO ''')
    titulos = ['ID', 'Código', 'Nombre', 'Precio']
    ancho_columnas = [5, 10, 10, 8]  # Ajustamos el ancho de la columna "Precio"

    print(f"\n| {''.join(['-' * ancho for ancho in ancho_columnas])} |")
    print(f"| {''.join([titulo.ljust(ancho) for titulo, ancho in zip(titulos, ancho_columnas)])} |")
    print(f"| {''.join(['-' * ancho for ancho in ancho_columnas])} |")

    for producto in cursor.fetchall():
        fila_formateada = [str(producto[0]).ljust(ancho_columnas[0]),
                           producto[1].ljust(ancho_columnas[1]),
                           textwrap.fill(producto[2], ancho_columnas[2]),
                           str(producto[3]).rjust(ancho_columnas[3])]
        print(f"| {''.join([dato for dato in fila_formateada])}")
    print(f"| {''.join(['-' * ancho for ancho in ancho_columnas])} |")

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
            seleccionarProductos()
            
        elif opcion == 5:
            print("¡Gracias por usar este programa!")
            conexion.close()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menuPrincipal()