from conexion import Conexion
from producto import Producto
from logger_base import log

class ProductoDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    #SELECT * FROM PRODUCTO
    '''
    _SELECCIONAR = 'SELECT * FROM Producto ORDER BY idproducto'
    _INSERTAR = 'INSERT INTO Producto(codigo, nombre, precio) VALUES(?, ?, ?)'
    _ACTUALIZAR = 'UPDATE Producto SET codigo=?, nombre=?, precio=? WHERE idproducto=?'
    _ELIMINAR = 'DELETE FROM Producto WHERE idproducto=?'

        
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            cursor = conexion.cursor()
            try:
                print(" ")
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = [] 
                for registro in registros:
                    producto = Producto(registro[0], registro[1], registro[2], registro[3])
                    productos.append(producto)
                return productos
            except Exception as e:
                log.error(f'''
                        Al obtener la tabla ocurrio una excepcion [{e}]
                        Crea una tabla con la Opcion 6''')
            finally: 
                cursor.close()
        
    @classmethod
    def insertar(cls, producto):
        with Conexion.obtenerConexion() as conexion:
            cursor = Conexion.obtenerCursor()
            valores = (producto.codigo, producto.nombre, producto.precio)
            try:
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'Producto insertado: {producto}')
                return cursor.rowcount # cantidad de registros insertados
            except Exception as e:
                log.error(f'''
                        Al insertar ocurrio una excepcion [{e}]
                        Crea una tabla con la Opcion 6''')
            finally: 
                cursor.close()
                
    @classmethod
    def actualizar(cls, producto):
        with Conexion.obtenerConexion() as conexion:
            cursor = Conexion.obtenerCursor()
            valores = (producto.codigo, producto.nombre, producto.precio, producto.idproducto)
            try:
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'Producto actualizada: {producto}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'''
                        Al actualizar ocurrio una excepcion [{e}]
                        Crea una tabla con la Opcion 6''')    
            finally: 
                cursor.close()
    
    @classmethod
    def eliminar(cls, producto):
        with Conexion.obtenerConexion() as conexion:
            cursor = Conexion.obtenerCursor()
            valores = (producto.idproducto,)
            try:
                cursor.execute(cls._ELIMINAR, valores)
                conexion.commit()
                log.debug(f'Objeto eliminado: {producto}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'''
                        Al eliminar ocurrio una excepcion [{e}]
                        Crea una tabla con la Opcion 6''')
            finally: 
                cursor.close()
                   
            
            

if __name__ == '__main__':
    #Insertar
    #p2 = Producto(codigo='XXB', nombre='Galleta Ritz', precio='3')
    #p_insertadas = ProductoDAO.insertar(p2)
    #log.debug(f'Productos insertados: {p_insertadas}')
    
    # Actualizar
    #p2 = Producto(2,'XXQ','Ajinomen','10')
    #p_actualizadas = ProductoDAO.actualizar(p2)
    #log.debug(f'Prodructos actualizados: {p_actualizadas}')
    
    # Eliminar
    #p3= Producto(idproducto=1)
    #p_eliminadas = ProductoDAO.eliminar(p3)
    #log.debug(f'Productos eliminados: {p_eliminadas}')
    
    #try:
    #    for producto in p3:
    #        log.debug(producto)
    #except Exception as e:
    #    log.error('Crea TABLA ')
    
    # Seleccionar objetos
    productos = ProductoDAO.seleccionar()
    try:
        for producto in productos:
            log.debug(producto)
    except Exception as es:
        log.error('Crea TABLA ')