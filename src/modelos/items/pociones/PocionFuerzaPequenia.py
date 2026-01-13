from .Pocion import Pocion


class PocionFuerzaPequenia(Pocion):

    def __init__(
        self,
        nombre="Poción de fuerza pequeña",
        descripcion="Otorga 5 de fuerza permanentes",
        tipo="aumento",
        atributo="fuerza",
        cantidad=5,
    ):
        super().__init__(nombre, descripcion, tipo, atributo, cantidad)

    def usar(self, entidad):
        entidad.fuerza += self.cantidad
        return {"tipo": self.tipo, "atributo": self.atributo, "cantidad": self.cantidad}
