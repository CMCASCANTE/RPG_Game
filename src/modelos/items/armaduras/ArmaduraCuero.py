from .Armadura import Armadura


class ArmaduraCuero(Armadura):
    def __init__(
        self, nombre="Armadura de cuero", descripcion="Simple y robusta", defensa=5
    ):
        super().__init__(nombre, descripcion, defensa=defensa)
