from abc import ABC
from modelos.entidades.LogicaEntidad import LogicaEntidad

import random


# Clase base para todos los personajes, tanto jugadores como npcs
class Entidad(ABC, LogicaEntidad):
    def __init__(self, nombre, vida, esencia, fuerza, defensa):
        # Atributos básicos
        self.nombre = nombre
        self.vida_max = vida
        self.vida_actual = vida
        self.fuerza = fuerza
        self.defensa = defensa
        # Atributo para poder lanzar habilidades
        self.esencia_max = esencia
        self.esencia_actual = esencia

        # Equipables
        self.arma_equipada = None
        self.armadura_equipada = None
        # Aquí guardaremos los objetos y habilidades
        self.inventario = []
        self.habilidades = []

    # Propiedad que calcula el daño total
    @property
    def daño_total(self):
        bono = self.arma_equipada.bonificador_fuerza if self.arma_equipada else 0
        return (
            random.randint(self.fuerza + 1, self.fuerza + bono) if bono else self.fuerza
        )

    # Propiedad que calcula la defensa total
    @property
    def defensa_total(self):
        bono = (
            self.armadura_equipada.bonificador_defensa if self.armadura_equipada else 0
        )
        return self.defensa + bono

    # Propiedad para comprobar si el personaje tiene puntos de vida
    @property
    def esta_vivo(self):
        return self.vida_actual > 0
