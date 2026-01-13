from ..Item import Item


class Pocion(Item):
    def __init__(self, nombre, descripcion, tipo, atributo, cantidad):
        super().__init__(nombre, descripcion)
        self.tipo = tipo
        self.atributo = atributo
        self.cantidad = cantidad

    def usar(self, entidad):
        raise NotImplementedError
