from .Item import Item


class ItemEquipable(Item):
    def __init__(
        self, nombre, descripcion, bonificador_fuerza=0, bonificador_defensa=0
    ):
        super().__init__(nombre, descripcion)
        self.bonificador_fuerza = bonificador_fuerza
        self.bonificador_defensa = bonificador_defensa
