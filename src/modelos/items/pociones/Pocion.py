from ..Item import Item


class Pocion(Item):
    def __init__(self, nombre, descripcion, tipo):
        super().__init__(nombre, descripcion)
        self.tipo = tipo

    def usar(self, entidad):
        raise NotImplementedError
