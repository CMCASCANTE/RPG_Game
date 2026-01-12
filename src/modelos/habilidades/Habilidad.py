from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..entidades.entidades import Entidad


class Habilidad:

    def __init__(self, nombre, descripcion, descripcion_uso, tipo, coste):
        self.nombre = nombre
        self.descripcion = descripcion
        self.descripcion_uso = descripcion_uso
        self.tipo = tipo
        self.coste = coste

    def usar(self, entity: Entidad):
        raise NotImplementedError
