from .Entidad import Entidad
from modelos.items.items import Arma, Armadura


class Jugador(Entidad):
    # Constructor del jugador
    def __init__(self, nombre, vida, fuerza, defensa, clase):
        super().__init__(nombre, vida, fuerza, defensa)
        # Clase del jugador
        self.clase = clase
        # Aquí guardaremos los objetos como Pocion
        self.inventario = []

    # Método para equipar armas y armaduras
    def equipar(self, item):
        if isinstance(item, Arma):
            self.arma_equipada = item
        if isinstance(item, Armadura):
            self.armadura_equipada = item
