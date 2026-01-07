from modelos.entidades.entidades import JugadorGuerrero
from modelos.items.items import (
    EspadaOxidada,
    ArmaduraCuero,
    PocionCuracionPequenia,
    PocionFuerzaPequenia,
)
from interfaz.consola.mapas.MapaInicial import MapaInicial


# Creación de ítems iniciales
espada_inicial = EspadaOxidada()
armadura_inicial = ArmaduraCuero()
pocion_vida = PocionCuracionPequenia()
pocion_fuerza = PocionFuerzaPequenia()

# Configuración inicial del jugador
heroe = JugadorGuerrero("Link")
heroe.equipar(espada_inicial)
heroe.equipar(armadura_inicial)
heroe.inventario.extend([pocion_vida, pocion_fuerza])

# Creación del mapa
mapa = MapaInicial(heroe)
# Cargamos el mapa inicial
mapa.iniciar_mapa()
