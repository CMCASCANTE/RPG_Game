from ..ItemEquipable import ItemEquipable


class Armadura(ItemEquipable):
    def __init__(self, nombre, descripcion, defensa):
        # Una armadura principalmente da defensa
        super().__init__(nombre, descripcion, bonificador_defensa=defensa)
