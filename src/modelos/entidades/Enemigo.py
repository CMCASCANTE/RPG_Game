from .Entidad import Entidad


import random


class Enemigo(Entidad):

    def __init__(self, nombre, vida, fuerza, defensa):
        super().__init__(nombre, vida, fuerza, defensa)

    def seleccionar_accion(self, objetivos):
        # IA Simple: Ataca siempre al primer objetivo vivo (el jugador)
        import random

        return random.choice(objetivos)
