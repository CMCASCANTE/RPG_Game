from .Armadura import Armadura


class ArmaduraPieles(Armadura):
    def __init__(
        self, nombre="Armadura de pieles", descripcion="Amasijo de pieles", defensa=3
    ):
        super().__init__(nombre, descripcion, defensa=defensa)
