class Orden:
    
    contador_ordenes = 0
    
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        #Recibe la lista de objetos de tipo Computadora
        self.__computadoras = computadoras        

    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora) 
    
    def __str__(self):
        computadoras_str = ""
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()
        
        return (
            f"Orden: {self.__id_orden}, " 
            f"computadoras: {computadoras_str}"
            )