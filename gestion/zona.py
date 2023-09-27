class Zona:
    def __init__(self, nombre = "", zoo = None, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    def agregarAnimales(self, animal):
        if self._animales == None:
            self._animales = []
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        if self._animales == None:
            c_animales = 0
        else:
            c_animales = len(self._animales)
        return c_animales 

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo

    def getZoo(self):
        return self._zoo

    


            
            
