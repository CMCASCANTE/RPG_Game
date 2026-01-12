from abc import ABC
from modelos.items.items import Arma, Armadura
from modelos.items.items import Pocion
from modelos.habilidades import Habilidad
from typing import Self

import random


# Clase base para todos los personajes, tanto jugadores como npcs
class Entidad(ABC):
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

    # Función para restar vida según la defensa y el daño enemigo
    # Devuelve el daño final que se ha recibido
    def recibir_daño(self, cantidad: int, tipo: str = None) -> int:
        # Lógica de mitigación física: el daño real es daño - defensa
        # El daño mágico se salta la mitigación de la armadura (solo cuenta la defensa base del personaje)
        # Elegimos el mayor entre la cantidad y 0 para no obtener números negativos
        if tipo == "magico":
            daño_final = max(0, cantidad - self.defensa)
        else:
            daño_final = max(0, cantidad - self.defensa_total)
        # restamos el valor del daño de la vida actual
        self.vida_actual = max(0, self.vida_actual - daño_final)
        # devolvemos la cantidad de daño que se ha hecho
        # ya que puede variar segun las armas
        return daño_final

    # Método para usar habilidades
    # Devolvemos el valor que devuelve la habilidad
    # En caso de no tener esencia suficiente, devolvemos -1
    def usar_habilidad(self, habilidad: Habilidad, objetivos: list[Self]) -> int:
        if self.esencia_actual >= habilidad.coste:
            self.esencia_actual -= habilidad.coste
            return habilidad.usar(objetivos)
        else:
            return -1

    # Método para equipar armas y armaduras
    # Devolvemos el propio método por si se quiere encadenar
    def equipar(self, item) -> Self:
        if isinstance(item, Arma):
            self.arma_equipada = item
        if isinstance(item, Armadura):
            self.armadura_equipada = item
        return self

    # Método para añadir items
    # Devolvemos el propio método por si se quiere encadenar
    def obtenerItem(self, item: Pocion) -> Self:
        self.inventario.append(item)
        return self

    # Método para añadir habilidades
    # Devolvemos el propio método por si se quiere encadenar
    def obtenerHabilidad(self, habilidad: Habilidad) -> Self:
        self.habilidades.append(habilidad)
        return self
