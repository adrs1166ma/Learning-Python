from logger_base import log
from producto import Producto
from producto_dao import ProductoDAO
from conexion import Conexion


def menu():
    while True:
        print("\n[ Menú Opciones ]".center(30,'-'))
        print("1. Registrar")
        print("2. Eliminar")
        print("3. Editar")
        print("4. Listar")
        print("5. Verificar Tabla")
        print("6. Salir")
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1: # Registrar
            c = input("Ingrese el código del producto: ")
            n = input("Ingrese el nombre del producto: ")
            p = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(codigo=c,nombre=n,precio=p)
            productos_insertados = ProductoDAO.insertar(nuevo_producto)
            log.debug(f'Productos insertados: {productos_insertados}')
        
        elif opcion == 2: # Eliminar
            idP = int(input("Ingrese el ID del producto a eliminar: "))
            borrar_producto = Producto(idproducto=idP)
            productos_eliminados = ProductoDAO.eliminar(borrar_producto)
            log.debug(f'Productos eliminados: {productos_eliminados}')
        
        elif opcion == 3: # Editar
            idP = int(input("Ingrese el ID del producto a editar: "))
            c = input("Ingrese el nuevo código del producto (opcional): ")
            n = input("Ingrese el nuevo nombre del producto (opcional): ")
            p = input("Ingrese el nuevo precio del producto (opcional): ")
            editar_producto = Producto(idP,c,n,p)
            productos_actualizados = ProductoDAO.actualizar(editar_producto)
            log.debug(f'Prodructos actualizados: {productos_actualizados}')
        
        elif opcion == 4: # Listar
            productos = ProductoDAO.seleccionar()
            try:
                for producto in productos:
                    log.debug(producto)
            except Exception as es:
                log.error('Crea TABLA ')
        
        elif opcion == 5: # verificar tabla existe
            log.info('tablas disponibles: {cls._TABLA}')
            Conexion.crearTabla()
            
        elif opcion == 6: # Salir
            print("¡Gracias por usar este programa!")
            
            break
        else:
            print("Opción no válida. Intente nuevamente.")
menu()