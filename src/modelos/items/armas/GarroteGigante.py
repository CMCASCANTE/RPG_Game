from .Arma import Arma


class GarroteGigante(Arma):

    def __init__(
        self,
        nombre="Garrote Gigante",
        descripcion="Garrote de madera Enorme",
        fuerza=7,
    ):
        super().__init__(nombre, descripcion, fuerza=fuerza)
