# archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
print(archivo.readline())
print(archivo.readline())
