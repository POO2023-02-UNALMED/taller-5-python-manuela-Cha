class zoologico:

    def __init__(self, nombre = "", ubicacion = "", zonas = []):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas 

    def setNombre (self, nombre):
        self._nombre = nombre 

    def getNombre (self):
        return self._nombre


    def setUbicacion (self, ubi):
        self._ubicacion = ubi

    def getUbicacion (self):
        return self._ubicacion


    def agregarZonas(zona):
        self._zonas.append(zona)

    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        total_animales = 0
        for zona in self._zonas:
            total_animales += zona.cantidadAnimales()
