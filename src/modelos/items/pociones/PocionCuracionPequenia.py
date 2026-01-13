from .Pocion import Pocion


class PocionCuracionPequenia(Pocion):

    def __init__(
        self,
        nombre="Poción de curación pequeña",
        descripcion="Cura 20 puntos de vida",
        tipo="curacion",
        atributo="vida",
        cantidad=20,
    ):
        super().__init__(nombre, descripcion, tipo, atributo, cantidad)

    def usar(self, entidad):
        # Elegimos el mínimo entre la vida maxima y la vida actual mas la curación
        # para que no sobrepase la vida maxima
        entidad.vida_actual = min(entidad.vida_max, entidad.vida_actual + self.cantidad)
        return {"tipo": self.tipo, "atributo": self.atributo, "cantidad": self.cantidad}
