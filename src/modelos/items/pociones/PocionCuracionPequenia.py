from .Pocion import Pocion


class PocionCuracionPequenia(Pocion):

    def __init__(
        self, nombre="Poción de curación pequeña", descripcion="Cura 20 puntos de vida"
    ):
        super().__init__(nombre, descripcion)
        self.curacion = 20

    def usar(self, entidad):
        antes = entidad.vida_actual
        # Elegimos el mínimo entre la vida maxima y la vida actual mas la curación
        # para que no sobrepase la vida maxima
        entidad.vida_actual = min(entidad.vida_max, entidad.vida_actual + self.curacion)
        print(f"✨ {entidad.nombre} recuperó {entidad.vida_actual - antes} HP.")
