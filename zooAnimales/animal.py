class Animal:
    totalAnimales = 0
    
    def __init__(self, nombre =  "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal.totalAnimales += 1

    def movimiento (self):
        return "desplazamiento"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        mam  = Mamifero.cantidadMamiferos()
        av = Ave.cantidadAves()
        pe = Pez.cantidadPeces()
        an = Anfibio.cantidadAnfibios()
        rep = Reptil.cantidadReptiles()

        return f'''Mamiferos : {mam}\nAves : {av}\nReptiles : {rep}\nPeces : {an}\nAnfibios : {an}'''

    def __str__(self):
        if len(self._zona) != 0:
            nombre = self._zona.__getitem__(0).getNombre()
            cadena = f", la zona en la que me ubico es {nombre}, en el {self._zona[0].getZoo().getNombre()}"
            return cadena
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    def toString(self):
        if len(self._zona) != 0:
            nombre = self._zona.__getitem__(0).getNombre()
            cadena = f", la zona en la que me ubico es {nombre}, en el {self._zona[0].getZoo().getNombre()}"
            return cadena
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre 

    def setEdad (self, edad):
        self._edad = edad

    def getEdad (self):
        return self._edad
    
    def setHabitat (self, habitat):
        self._habitat = habitat

    def getHabitat (self):
        return self._habitat
    
    def getGenero (self):
        return self._genero
    
    def setGenero (self, genero):
        self._genero = genero 

    def setZona(self, zona):
        self._zona.append(zona)

    def getZona(self):
        return self._zona

    @classmethod
    def getCantidadAnimales (cls):
        return Animal.totalAnimales
