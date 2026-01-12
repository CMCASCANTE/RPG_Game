from .Entidad import Entidad


class Enemigo(Entidad):

    def __init__(self, nombre, vida, esencia, fuerza, defensa):
        super().__init__(nombre, vida, esencia, fuerza, defensa)
