import customtkinter as ctk
from PIL import Image
import os


class MenuBase(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color="transparent")
        self.controlador = (
            controlador  # Guardamos referencia para llamar a cambiar_pantalla
        )

        # --- CARGAR FONDO ---
        ruta_script = os.path.dirname(__file__)
        ruta_img = os.path.join(ruta_script, "..", "assets", "fondo.png")
        self.img_fondo = ctk.CTkImage(Image.open(ruta_img), size=(800, 600))

        self.label_fondo = ctk.CTkLabel(self, image=self.img_fondo, text="")
        self.label_fondo.place(relwidth=1, relheight=1)

        # --- BOTÓN PARA IR AL JUEGO ---
        self.btn_jugar = ctk.CTkButton(
            self.label_fondo,  # <--- IMPORTANTE: El master es el fondo
            text="NUEVA PARTIDA",
            command=lambda: self.controlador.mostrar_interfaz_juego(),  # Llamamos al controlador
            fg_color="#2c3e50",
            hover_color="#34495e",
            width=150,
            height=40,
        )
        self.btn_jugar.place(
            relx=0.50,  # Mueve de izquierda (0) a derecha (1).
            rely=0.75,  # Mueve de arriba (0) a abajo (1).
            anchor="center",
        )

        # --- BOTÓN PARA SALIR DEL JUEGO ---
        self.btn_salir = ctk.CTkButton(
            self.label_fondo,
            text="SALIR",
            command=self.quit,
            fg_color="#c0392b",
            hover_color="#e74c3c",
            width=150,
            height=40,
        )
        self.btn_salir.place(
            relx=0.50,  # Mueve de izquierda (0) a derecha (1).
            rely=0.90,  # Mueve de arriba (0) a abajo (1).
            anchor="center",
        )

        # --- BOTÓN PARA IR AL TEST PRIMER MAPA ---
        self.btn_jugar = ctk.CTkButton(
            self.label_fondo,  # <--- IMPORTANTE: El master es el fondo
            text="MAPA 1",
            command=lambda: self.controlador.primer_mapa(),  # Llamamos al controlador
            fg_color="#2c3e50",
            hover_color="#34495e",
            width=150,
            height=40,
        )
        self.btn_jugar.place(
            relx=0.50,  # Mueve de izquierda (0) a derecha (1).
            rely=0.45,  # Mueve de arriba (0) a abajo (1).
            anchor="center",
        )
