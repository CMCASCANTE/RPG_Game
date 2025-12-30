from ..ItemEquipable import ItemEquipable


class Arma(ItemEquipable):
    def __init__(self, nombre, descripcion, fuerza):
        # Un arma principalmente da fuerza
        super().__init__(nombre, descripcion, bonificador_fuerza=fuerza)
