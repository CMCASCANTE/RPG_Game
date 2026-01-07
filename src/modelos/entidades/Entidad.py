from abc import ABC, abstractmethod

import random


# Clase base para todos los personajes, tanto jugadores como npcs
class Entidad(ABC):
    def __init__(self, nombre, vida, fuerza, defensa):
        # Atributos básicos
        self.nombre = nombre
        self.vida_max = vida
        self.vida_actual = vida
        self.fuerza = fuerza
        self.defensa = defensa
        # Equipables
        self.arma_equipada = None
        self.armadura_equipada = None

    # Cálculo de daño total
    @property
    def daño_total(self):
        bono = self.arma_equipada.bonificador_fuerza if self.arma_equipada else 0
        return (
            random.randint(self.fuerza + 1, self.fuerza + bono) if bono else self.fuerza
        )

    # Cálculo de defensa total
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

    # Función para restar vida según la defensa y el daño enemigo
    def recibir_daño(self, cantidad):
        # Lógica de mitigación: el daño real es daño - defensa
        # ejegimos el mayor entre la cantidad y 0 para no obtener números negativos
        daño_final = max(0, cantidad - self.defensa_total)
        self.vida_actual = max(0, self.vida_actual - daño_final)
        # Indicamos el daño recibido y la vida restante
        print(
            f"{self.nombre} recibió {daño_final} de daño. Vida restante: {self.vida_actual}/{self.vida_max}"
        )
