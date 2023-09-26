import Animal
class Anfibio (Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    total_anfibios = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPiel = "", venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Anfibio.total_anfibios += 1

    @classmethod
    def cantidadAnfibios (cls):
        return cls.total_Anfibios
    
    @classmethod
    def crearRana(cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra (cls, nombre = "", edad = 0, habitat = "", genero = "" ):
        cls.salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @classmethod
    def getListado (cls):
        return cls._listado

    def setVenenoso (self, venenoso):
        self._venenoso = venenoso

    def isVenenoso (self):
        return self._venenoso 
    
    
    def setColorPiel(self, color):
        self._colorPiel =  color
    
    def getColorPiel(self):
        return self._colorPiel
