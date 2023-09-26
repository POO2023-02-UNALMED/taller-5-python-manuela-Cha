class Zoologico:
    nombre = ""
    ubicacion = ""
    zonas = []
    totalAnimales = 0

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion


    def agregarZonas(zona):
        Zoologico.zonas.append(zona)

    def cantidadTotalAnimales(self):
        for zona in zonas:
