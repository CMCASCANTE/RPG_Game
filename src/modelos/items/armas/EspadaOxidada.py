from .Arma import Arma


class EspadaOxidada(Arma):

    def __init__(
        self,
        nombre="Espada Oxidada",
        descripcion="Oxidada pero funcional",
        fuerza=10,
    ):
        super().__init__(nombre, descripcion, fuerza=fuerza)
