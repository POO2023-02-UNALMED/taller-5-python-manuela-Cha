import Animal
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    total_mamiferos = 0

    def __init__(self, pelaje, patas):
        super().__init__(nombre = "", edad = 0, habitat = "", genero = "")
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        Mamifero.total_mamiferos += 1

    @classmethod
    def cantidadMamiferos (cls):
        return cls.total_mamiferos
    
    @classmethod
    def crearCaballo(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.leones += 1
        caballo = Mamifero(nombre, edad, "selva", genero, True, 4)
    
    @classmethod
    def getListado (cls):
        return cls._listado

    def setPelaje (self, pelaje):
        self._pelaje = pelaje

    def isPelaje (self):
        return self._pelaje 
    
    
    def set_patas(self, patas):
        self._patas =  patas
    
    def getPatas(self):
        return self._patas 
