from .Jugador import Jugador


class JugadorGuerrero(Jugador):

    def __init__(self, nombre, vida=100, fuerza=8, defensa=5, clase="Guerrero"):
        super().__init__(nombre, vida, fuerza, defensa, clase)
