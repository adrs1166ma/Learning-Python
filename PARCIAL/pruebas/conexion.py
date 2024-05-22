import sys
from logger_base import log
import sqlite3 as bd

class Conexion:
    _DATABASE = 'Mancilla_almacen'
    _conexion = None
    _cursor = None
    _TABLA = 'Producto'
     
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener al conexion {e}')
                sys.exit()
        else:
            return cls._conexion
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
    
    @classmethod
    def crearTabla(cls):
        with Conexion.obtenerConexion() as conexion:
            cursor = conexion.cursor()
            #cursor.execute(f'''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{cls._TABLA}' ''')
            
            try:
                cursor.execute(f'''CREATE TABLE PRODUCTO (idproducto INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nombre TEXT, precio REAL) ''')
                log.debug(f'Tabla "{cls._TABLA}"creada')
            except Exception as e:
                log.error(f'''
                        La tabla ya esta creada: [{e}]
                        ''')
            finally: 
                cursor.close()
                
            
        
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    Conexion.crearTabla()
                
             