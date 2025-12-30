from ..Item import Item


class Pocion(Item):
    def __init__(self, nombre, descripcion):
        super().__init__(nombre, descripcion)

    def usar(self, entidad):
        raise NotImplementedError
