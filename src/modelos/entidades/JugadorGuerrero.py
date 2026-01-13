from .Jugador import Jugador


class JugadorGuerrero(Jugador):

    def __init__(
        self, nombre, vida=100, esencia=30, fuerza=8, defensa=5, clase="Guerrero"
    ):
        super().__init__(nombre, vida, esencia, fuerza, defensa, clase)
        self.iniciar_clase()

    def iniciar_clase(self):
        from modelos.habilidades.habilidades import RayoHielo
        from modelos.items.items import (
            EspadaOxidada,
            ArmaduraCuero,
            PocionCuracionPequenia,
            PocionFuerzaPequenia,
        )

        self.equipar(EspadaOxidada())
        self.equipar(ArmaduraCuero())
        self.obtenerItem(PocionCuracionPequenia())
        self.obtenerItem(PocionFuerzaPequenia())
        self.obtenerHabilidad(RayoHielo())
