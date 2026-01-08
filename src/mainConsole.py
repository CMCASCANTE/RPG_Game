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

# Bucle de Menú principal
while True:
    print("############################")
    print("## Bienvenido al RPG GAME ##")
    print("############################")

    print("###################################################")
    print("## Por ahora, el heroe se genera automaticamente ##")
    print("###### 1. Iniciar Juego ###########################")
    print("###### 2. Salir ###################################")
    print("###################################################")
    opt = input("Seleccionar opcion: ")

    if opt == "1":

        # Creación del mapa
        mapa = MapaInicial(heroe)
        # Cargamos el mapa inicial
        if mapa.iniciar_mapa():
            print("Enhora buena!! Has finalizado el mapa inicial")
        else:
            break

    elif opt == "2":
        break
