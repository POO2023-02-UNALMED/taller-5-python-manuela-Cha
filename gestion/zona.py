class Zona:
    def __init__(self, nombre = "", zoo = None, animales = []):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales():
        return len(self._animales)

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo

    def getZoo(self):
        return self._zoo

    


            
            
