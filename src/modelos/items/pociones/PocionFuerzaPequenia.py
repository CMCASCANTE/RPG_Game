from .Pocion import Pocion


class PocionFuerzaPequenia(Pocion):

    def __init__(
        self,
        nombre="Poción de fuerza pequeña",
        descripcion="Otorga 5 de fuerza permanentes",
        tipo="fuerza",
    ):
        super().__init__(nombre, descripcion, tipo)
        self.aumento_fuerza = 5

    def usar(self, entidad):
        entidad.fuerza += self.aumento_fuerza
        return self.aumento_fuerza
