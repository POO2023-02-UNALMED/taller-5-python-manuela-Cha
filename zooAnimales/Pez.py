import Animal
class Pez (Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    total_peces = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "",  cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas 
        Pez._listado.append(self)
        Pez.total_peces += 1

    @classmethod
    def cantidadPeces (cls):
        return cls.total_peces
    
    @classmethod
    def crearSalmon(cls, nombre = "", edad = 0, habitat = "", genero = ""):
        cls.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao (cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @classmethod
    def getListado (cls):
        return cls._listado

    def setColorEscamas (self, color):
        self._colorEscamas = color

    def getColorEscamas (self):
        return self._colorEscamas
    
    
    def setCantidadAletas(self, cantidad ):
        self._cantidadAletas = cantidad 
    
    def getCantidadAletas(self):
        return self._cantidadAletas
