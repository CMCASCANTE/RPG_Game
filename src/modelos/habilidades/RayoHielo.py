from .Habilidad import Habilidad
from ..entidades.entidades import Entidad


class RayoHielo(Habilidad):
    def __init__(
        self,
        nombre="Rayo de Hielo",
        descripcion="Un rayo de hielo que golpea a todos los objetivos y atraviesa la armadura",
        descripcion_uso="Lanzas un rayo helado que al golpear en el objetivo se expande en una gran explosión de hielo que cubre todo el área",
        tipo="magico",
        coste=10,
        daño=10,
    ):
        super().__init__(nombre, descripcion, descripcion_uso, tipo, coste)
        self.daño = daño

    def usar(self, entities: list[Entidad]):
        daño_total = 0
        for entity in entities:
            daño_total += entity.recibir_daño(self.daño, self.tipo)
        return daño_total
