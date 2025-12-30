from .Enemigo import Enemigo
from modelos.items.items import GarroteGigante, ArmaduraPieles


class JefeOrco(Enemigo):

    def __init__(self, nombre="Jefe Orco", vida=50, fuerza=12, defensa=5):
        super().__init__(nombre, vida, fuerza, defensa)
        self.arma_equipada = GarroteGigante()
        self.armadura_equipada = ArmaduraPieles()
