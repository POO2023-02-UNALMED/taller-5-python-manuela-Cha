class Zoologico:

    def __init__(self, nombre = "", ubicacion = "", zonas = []):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas 


    def agregarZonas(zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        total_animales = 0
        for zona in self._zonas:
            total_animales += zona.cantidadAnimales()
