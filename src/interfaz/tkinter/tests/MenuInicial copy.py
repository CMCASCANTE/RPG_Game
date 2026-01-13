import customtkinter as ctk
from PIL import Image
import os


class MenuInicial(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RPG GAME")
        self.resizable(False, False)
        self.geometry("600x400")

        self.configure(fg_color="black")

        # --- CARGAR IMAGEN PARA EL FONDO ---
        # Buscamos la ruta de la imagen
        ruta_script = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_script, "../../../assets", "fondo.png")

        # Cargamos la imagen con CTkImage para que se vea bien en pantallas de alta resolución
        self.imagen_fondo = ctk.CTkImage(
            light_image=Image.open(ruta_imagen),
            dark_image=Image.open(ruta_imagen),
            size=(600, 400),  # Tamaño de la ventana
        )

        # --- MOSTRAR IMAGEN ---
        # Usamos un Label para que la imagen actúe como fondo
        self.label_fondo = ctk.CTkLabel(self, image=self.imagen_fondo, text="")
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # --- BOTONES Y TÍTULO DIRECTOS ---
        # En lugar de usar un Frame, usamos 'master=self.label_fondo'
        # para que los elementos "pertenezcan" visualmente a la imagen.

        # self.titulo = ctk.CTkLabel(
        #     self.label_fondo,  # <--- IMPORTANTE: El master es el fondo
        #     text="PROYECTO RPG",
        #     font=("Fixedsys", 50, "bold"),
        #     text_color="white",
        #     fg_color="transparent",  # Aseguramos transparencia
        # )
        # self.titulo.place(relx=0.5, rely=0.3, anchor="center")

        self.btn_jugar = ctk.CTkButton(
            self.label_fondo,  # <--- IMPORTANTE: El master es el fondo
            text="NUEVA PARTIDA",
            command=self.iniciar_juego,
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

    def iniciar_juego(self):
        print("Cargando mundo...")


if __name__ == "__main__":
    app = MenuInicial()
    app.mainloop()
