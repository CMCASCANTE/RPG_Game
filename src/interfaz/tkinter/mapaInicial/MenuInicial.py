import customtkinter as ctk


class MenuJuego(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color="black")
        self.controlador = controlador

        self.label = ctk.CTkLabel(self, text="ESTÁS EN EL JUEGO", font=("Arial", 30))
        self.label.pack(pady=50)

        self.btn_volver = ctk.CTkButton(
            self,
            text="VOLVER AL MENÚ",
            command=lambda: self.controlador.mostrar_menu_principal(),
        )
        self.btn_volver.pack()
