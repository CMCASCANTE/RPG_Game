import os


class Mapa:

    def __init__(self, jugador):
        self.jugador = jugador

    def iniciar_mapa():
        raise NotImplementedError

    def limpiar_pantalla(self):
        # Si el sistema es Windows ('nt'), usa 'cls'
        # Si es Linux/Mac ('posix'), usa 'clear'
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
