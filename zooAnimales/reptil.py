from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    total_reptiles = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "",  largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola 
        Reptil._listado.append(self)
        Reptil.total_reptiles += 1

    @classmethod
    def cantidadReptiles (cls):
        return cls.total_reptiles
    
    @classmethod
    def crearIguana(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.iguanas += 1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente (cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @classmethod
    def getListado (cls):
        return cls._listado

    def setColorEscamas (self, color):
        self._colorEscamas = color

    def getColorEscamas (self):
        return self._colorEscamas
    
    
    def setLargoCola(self, largo):
        self._largoCola =  largo 
    
    def getLargoCola(self):
        return self._largoCola
