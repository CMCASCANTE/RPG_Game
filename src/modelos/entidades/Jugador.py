from .Entidad import Entidad


class Jugador(Entidad):
    # Constructor del jugador
    def __init__(self, nombre, vida, esencia, fuerza, defensa, clase):
        super().__init__(nombre, vida, esencia, fuerza, defensa)
        # Clase del jugador
        self.clase = clase
