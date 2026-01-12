from modelos.entidades.entidades import JugadorGuerrero
from interfaz.consola.mapas.MapaInicial import MapaInicial

import os

# Configuración inicial del jugador
heroe = JugadorGuerrero("Link")


# Bucle de Menú principal
while True:
    # Limpiamos la pantalla
    os.system("clear")
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
            input("\nPulsa una tecla para continuar...")
        else:
            break

    elif opt == "2":
        break
