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
    
#tablaExiste('Producto')

def insertarProducto(codigo, nombre, precio):
    cursor.execute('''INSERT INTO PRODUCTO (codigo, nombre, precio) VALUES (?,?,?) ''',(codigo,nombre,precio))
    conexion.commit()
    print(f'''Producto agregado:
          [{codigo}]{nombre} : ${precio}''')

#insertarProducto('XXA', 'Detergente', 2300) 
#insertarProducto('XXB', 'Jabon', 1000) 
#insertarProducto('XXC', 'Desinfectante', 1100) 

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
            query = f'''UPDATE producto SET {key} = '{diccionario[key]}' WHERE idproducto = {id} '''#.format(key, diccionario[key], id)
            cursor.execute(query)
    conexion.commit()

#print(seleccionarProductos())
#actualizarProducto(2,{'codigo':'XYZ','nombre':'Jabon en polvo','precio':900})
#print(seleccionarProductos())

def borrarProducto(id):
    cursor.execute(f'''DELETE FROM producto WHERE idproducto = {id} ''')
    conexion.commit()

#borrarProducto(2)
#print(seleccionarProductos())

