from .Pocion import Pocion


class PocionFuerzaPequenia(Pocion):

    def __init__(
        self,
        nombre="Poción de fuerza pequeña",
        descripcion="Otorga 5 de fuerza permanentes",
    ):
        super().__init__(nombre, descripcion)
        self.aumento_fuerza = 5

    def usar(self, entidad):
        entidad.fuerza += self.aumento_fuerza
        print(f"🔥 ¡La fuerza de {entidad.nombre} aumentó en {self.aumento_fuerza}!")
