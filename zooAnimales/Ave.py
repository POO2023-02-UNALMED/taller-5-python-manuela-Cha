import Animal
class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    total_aves = 0

    def __init__(self, colorPlumas):
        super().__init__(nombre = "", edad = 0, habitat = "", genero = "")
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        Ave.total_aves += 1

    classmethod
    def cantidadAves (cls):
        return cls.total_aves
    
    classmethod
    def crearHalcon(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.halcones += 1
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    classmethod
    def crearAguila(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.aguilas += 1
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    @classmethod
    def getListado (cls):
        return cls._listado
      #aqui voy 

    def setPelaje (self, pelaje):
        self._pelaje = pelaje

    def isPelaje (self):
        return self._pelaje 
    
    
    def set_patas(self, patas):
        self._patas =  patas
    
    def getPatas(self):
        return self._patas 
