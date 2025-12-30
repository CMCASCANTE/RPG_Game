from .Enemigo import Enemigo
from modelos.items.items import Garrote


class Orco(Enemigo):

    def __init__(self, nombre="Orco", vida=20, fuerza=10, defensa=3):
        super().__init__(nombre, vida, fuerza, defensa)
        self.arma_equipada = Garrote()
