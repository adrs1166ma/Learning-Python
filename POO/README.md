# Crear diagrama de clases con la herramienta gratuita de:

> www.umletino.com/umletino.html

#pass : no va tener ningun contenido aun
Diagrama de clases de tipo UML
Unified Modeling Language
Utilizada para documentar Clases, Objetos, etc

los *args van antes del **kwargs

*args(argumentos)
**kwargs(diccionario)


no se debe modificar los _ guiones bajos

en 02-07-00
FORMATO DE TEXTO
print('Creación objetos'.center(30,'-'))    

----

MRO - Method Order Resolution en Python

para hacer una clase con test
crear class
def init
encapsular
get y set


vlaidaciones es darle un rango a las clases u objetos
tambien en los get y set

al agregar una clase abstracta, obligamos a las hijas a tener esa misma clase,
y la clase que tenga el metodo abstacto  toda la clase se vuelve abstracta 


06-01 
para acceder a la variable de clase solo es necesario:
print(MiClase.variable_clase)

por otro lado para acceder a la variable de instancia se debe crear un `objeto`
tal que asi:
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)

la variable clase tambien se comparten con todos los objetos creados

06-02
las clases son objetos

06-03
metodo estatico
no se conecta con los atributos o variables

06-04
el metodo estatico no tiene informacion directa con la clase
simplemente se asocia con la clase misma

y el metodo clase si resive info en si misma

06-05
contexto 
tanto el metodo estatico `@staticmethod` 
y metodo clase `@classmethod` 
se motraran si las llamamos con el metodo de instancia
osea, la normal

dinamico : cuando se crea objetos de cierta clase
estatico : cuando se define la clase

06-06
una constante se define en MAYUSCULAS y con guiones bajos
tambien se puede utilizar dentro de una clase como variable clase

para importar tambien podemos poner coma si es del mismo 
y `as` = como para renombrala

06-06
incrementar valor como un primary key por id de persona

06-07 
mejorar la logica atravez del metodo clase



