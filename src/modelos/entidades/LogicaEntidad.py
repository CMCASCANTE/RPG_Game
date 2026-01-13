from modelos.items.items import Arma, Armadura
from modelos.items.items import Pocion
from modelos.habilidades import Habilidad
from typing import Self


class LogicaEntidad:

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
    def usar_habilidad(
        self, habilidad: Habilidad, objetivos: list[Self]
    ) -> dict | None:
        # Comprobamos si se tiene esencia y envianos None si no lo tiene
        if self.esencia_actual < habilidad.coste:
            return None
        # Restamos la esencia y usamos la skill
        # Nos devolverá un dict con
        # los valores de la skill y los efectos que ha tenido
        self.esencia_actual -= habilidad.coste
        return habilidad.usar(objetivos)

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
