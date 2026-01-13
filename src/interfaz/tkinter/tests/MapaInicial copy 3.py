import customtkinter as ctk
from PIL import Image
import os


class MapaInicial(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color="#1a1a1a")
        self.controlador = controlador

        # --- CARGAR IMAGEN DE FONDO ---
        ruta_script = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_script, "..", "..", "..", "assets", "fondo.png")

        try:
            self.img_fondo_ctk = ctk.CTkImage(
                light_image=Image.open(ruta_imagen),
                dark_image=Image.open(ruta_imagen),
                size=(800, 600),
            )
        except Exception:
            self.img_fondo_ctk = None

        self.label_fondo = ctk.CTkLabel(self, image=self.img_fondo_ctk, text="")
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.crear_interfaz()

        # Iniciamos la escena
        self.cargar_escena("inicio_cueva")

    def crear_interfaz(self):
        # --- SECCIÓN SUPERIOR: IMAGEN ---
        self.frame_escena = ctk.CTkFrame(
            self, fg_color="#000000", corner_radius=10, height=250
        )
        self.frame_escena.pack(pady=(20, 10), padx=20, fill="x")
        self.frame_escena.pack_propagate(False)

        self.imagen_escena_label = ctk.CTkLabel(
            self.frame_escena,
            text="IMAGEN DE LA ESCENA",
            text_color="white",
            font=("Fixedsys", 20),
        )
        self.imagen_escena_label.pack(fill="both", expand=True)

        # --- SECCIÓN CENTRAL: LOG DE TEXTO ---
        self.frame_log = ctk.CTkFrame(self, fg_color="#242424", corner_radius=10)
        self.frame_log.pack(pady=10, padx=20, fill="both", expand=True)

        self.log_texto = ctk.CTkTextbox(
            self.frame_log,
            font=("Fixedsys", 18),
            text_color="white",
            fg_color="transparent",
            wrap="word",
            cursor="arrow",
        )
        self.log_texto.pack(pady=10, padx=10, fill="both", expand=True)

        # Configuración de estilos para las opciones clicables
        self.log_texto.tag_config("opcion", foreground="#3b8ed0", underline=True)
        self.log_texto.bind(
            "<Motion>", self._cambiar_cursor
        )  # Cambia cursor al pasar por encima

        # --- SECCIÓN INFERIOR: ACCIONES FIJAS (FILA ÚNICA) ---
        self.frame_acciones_fijas = ctk.CTkFrame(
            self, fg_color="#1a1a1a", corner_radius=10
        )
        self.frame_acciones_fijas.pack(pady=(0, 20), padx=20, fill="x")

        # Layout en una sola fila usando pack(side="left")
        self.btn_inv = ctk.CTkButton(
            self.frame_acciones_fijas,
            text="INVENTARIO",
            width=120,
            command=self.mostrar_inventario,
        )
        self.btn_inv.pack(side="left", padx=10, pady=10, expand=True)

        self.btn_mapa = ctk.CTkButton(
            self.frame_acciones_fijas, text="MAPA", width=120, command=self.mostrar_mapa
        )
        self.btn_mapa.pack(side="left", padx=10, pady=10, expand=True)

        self.btn_save = ctk.CTkButton(
            self.frame_acciones_fijas,
            text="GUARDAR",
            width=120,
            command=self.guardar_juego,
        )
        self.btn_save.pack(side="left", padx=10, pady=10, expand=True)

        self.btn_menu = ctk.CTkButton(
            self.frame_acciones_fijas,
            text="SALIR AL MENÚ",
            width=120,
            fg_color="#c0392b",
            hover_color="#a93226",
            command=self.controlador.mostrar_menu_principal,
        )
        self.btn_menu.pack(side="left", padx=10, pady=10, expand=True)

    def escribir_en_log(self, texto, opciones=None):
        """Añade texto y genera opciones clicables dinámicamente"""
        self.log_texto.configure(state="normal")
        self.log_texto.insert("end", f"\n{texto}\n\n")

        if opciones:
            for nombre_visible, id_decision in opciones.items():
                tag_name = f"click_{id_decision}"
                self.log_texto.insert(
                    "end", f" > {nombre_visible}\n", ("opcion", tag_name)
                )
                # Vincular el clic al tag
                self.log_texto.tag_bind(
                    tag_name,
                    "<Button-1>",
                    lambda e, d=id_decision: self.tomar_decision(d),
                )
            self.log_texto.insert("end", "\n")

        self.log_texto.configure(state="disabled")
        self.log_texto.see("end")

    def tomar_decision(self, id_decision):
        # Al tomar una decisión, podemos limpiar el log o simplemente seguir escribiendo
        self.log_texto.configure(state="normal")
        self.log_texto.insert("end", "-------------------------------------------\n")
        self.cargar_escena(id_decision)

    def cargar_escena(self, id_escena):
        if id_escena == "inicio_cueva":
            opciones = {
                "Entrar en la cueva": "dentro_cueva",
                "Buscar alrededor de la entrada": "buscar_antorcha",
            }
            self.escribir_en_log(
                "Estás ante una cueva que emana un aire gélido. El silencio es absoluto.",
                opciones,
            )

        elif id_escena == "dentro_cueva":
            opciones = {
                "Gritar para ver si hay alguien": "gritar",
                "Avanzar a tientas por la pared": "avanzar_pared",
                "Volver atrás": "inicio_cueva",
            }
            self.escribir_en_log(
                "La oscuridad te envuelve. El suelo está resbaladizo.", opciones
            )

        elif id_escena == "buscar_antorcha":
            opciones = {
                "Recoger la antorcha y entrar": "dentro_cueva",
                "Dejarla y marcharte": "inicio_cueva",
            }
            self.escribir_en_log(
                "Entre unos matorrales encuentras una antorcha vieja pero funcional.",
                opciones,
            )

    def _cambiar_cursor(self, event):
        """Cambia el cursor a una 'mano' si está sobre una opción"""
        tags = self.log_texto.tag_names(f"@{event.x},{event.y}")
        if "opcion" in tags:
            self.log_texto.configure(cursor="hand2")
        else:
            self.log_texto.configure(cursor="arrow")

    # --- MÉTODOS DE SOPORTE ---
    def mostrar_inventario(self):
        print("Abriendo Inventario...")

    def mostrar_mapa(self):
        print("Abriendo Mapa...")

    def guardar_juego(self):
        print("Partida Guardada.")
