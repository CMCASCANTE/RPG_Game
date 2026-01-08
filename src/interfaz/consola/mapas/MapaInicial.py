from .Mapa import Mapa
from modelos.entidades.entidades import Orco, JefeOrco
from ..MotorCombate import MotorCombate


import random


class MapaInicial(Mapa):

    def __init__(self, jugador):
        super().__init__(jugador)

    # El mapa tendrá eventos
    # que saltarán de manera aleatoria
    # según si sale algún evento concreto,
    # las opciones disponibles aumentarán.
    # ejemplo:
    # avanzas - de entre todos los eventos salta
    # 1 random (a concretar si se elimina para que
    # no salte mas veces), este evento es una tienda,
    # la siguiente opción es avanzar o entrar a la tienda
    # cuando salgas de la tienda vuelve a tener disponible
    # solo la opción de avanzar

    # POR AHORA
    # tendra un número de enemigos concreto y un boss final
    # y un par de eventos especiales -
    # una tienda, una casa que investigar y un habitante con el que hablar
    # los enemigos se dividiran en diferentes grupos cada 1 un evento
    # algunos serán opcionales, otros no
    # el mapa se acaba cuando hayan saltado todos los eventos
    # en ese cmomento saldrá el boss y si se derrota se podrá continuar al siguiente
    # ¿¿ Una fuente de recuperación de vida como evento ??

    def iniciar_mapa(self) -> bool:
        print(
            "Tras salir de tu aldea en busca de aventuras"
            "\nHas llegado a un pueblo en ruinas que parece deshabitado"
            "\nComienzas a explorarlo... "
        )
        input("Pulsa una tecla para continuar...")
        # lanzamos un random que elija un evento
        eventos = [self.evento1, self.evento2]

        # Vamos lanzando los eventos mientas haya en la lista
        while eventos:
            evento = eventos.pop(random.randrange(len(eventos)))
            if evento():
                print("Sigues recorriendo el pueblo")
                input("Pulsa una tecla para continuar...")
            else:
                print("has muerto, se acabo la partida...")
                return False

        # Cuando ya no tenemos eventos en la lista
        # lanzamos el evento final
        if self.evento_final():
            print("Has vencido al jefe, enhorabuena!!!")
            return True
        else:
            print("has muerto, se acabo la partida...")
            return False

    # Evento 1 - Combate
    def evento1(self):
        self.limpiar_pantalla()
        print("Mientras recorrias el pueblo te han atacado!")
        lista_enemigos = [Orco(), Orco(), Orco()]

        # Ejecución
        partida = MotorCombate(self.jugador, lista_enemigos)
        return partida.iniciar_batalla()

    def evento2(self):
        self.limpiar_pantalla()
        print(
            "Oyes voces desde dentro de una casa, te acercas despacio..."
            "\nNada mas entrar por la puerta te asaltan unos Orcos!!"
        )
        lista_enemigos = [Orco(), Orco()]

        # Ejecución
        partida = MotorCombate(self.jugador, lista_enemigos)
        return partida.iniciar_batalla()

    def evento_final(self):
        self.limpiar_pantalla()
        print(
            "Tras deshacerte de los Orcos que quedaban en el pueblo"
            "\nOyes unos pasos que se acercan"
            "\nParecen pertenecer a algo mas grande que un Orco o un humano..."
            "\nTras un callejon aparece el jefe de los Orcos!!!"
            "\nEsta va a ser una batalla dificil..."
        )
        combateFinal = [JefeOrco()]
        # Ejecución
        partida = MotorCombate(self.jugador, combateFinal)
        return partida.iniciar_batalla()
