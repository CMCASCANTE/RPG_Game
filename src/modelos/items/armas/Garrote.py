from .Arma import Arma


class Garrote(Arma):

    def __init__(
        self,
        nombre="Garrote",
        descripcion="Garrote de madera",
        fuerza=5,
    ):
        super().__init__(nombre, descripcion, fuerza=fuerza)
