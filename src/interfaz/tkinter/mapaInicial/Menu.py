import customtkinter as ctk
from .MenuBase import MenuBase
from .MenuInicial import MenuJuego
from .MapaInicial import MapaInicial
from modelos.entidades.entidades import JugadorGuerrero


class Controlador(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RPG GAME")
        self.geometry("800x600")
        self.resizable(False, False)

        # Este será el contenedor donde "montaremos" los menús
        self.contenedor = ctk.CTkFrame(self, fg_color="transparent")
        self.contenedor.pack(fill="both", expand=True)

        # Configuración inicial del jugador
        self.jugador = JugadorGuerrero("Link")

        # Iniciamos con el menú principal
        self.mostrar_menu_principal()

    def cambiar_pantalla(self, clase_pantalla):
        """Borra el contenido actual y carga una nueva pantalla"""
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # Instanciamos la nueva pantalla dentro del contenedor
        nueva_pantalla = clase_pantalla(master=self.contenedor, controlador=self)
        nueva_pantalla.pack(fill="both", expand=True)

    def mostrar_menu_principal(self):
        self.cambiar_pantalla(MenuBase)

    def mostrar_interfaz_juego(self):
        self.cambiar_pantalla(MenuJuego)

    def primer_mapa(self):
        self.cambiar_pantalla(MapaInicial)
