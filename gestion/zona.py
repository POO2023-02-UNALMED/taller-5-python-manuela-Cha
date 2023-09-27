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
        c_animales = 0
        for animal in self._animales:
            if animal != None:
                c_animales += 1
        return c_animales 

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo

    def getZoo(self):
        return self._zoo

    


            
            
