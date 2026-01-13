import customtkinter as ctk
from PIL import Image
import os

# Importamos el diccionario de la historia
from mapaInicial.contenido import obtener_historia


class MapaInicial(ctk.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master, fg_color="#1a1a1a")
        self.controlador = controlador

        # --- RUTAS ---
        self.ruta_script = os.path.dirname(__file__)
        # Subimos niveles para llegar a la raíz del proyecto y luego a assets
        self.ruta_assets = os.path.abspath(
            os.path.join(self.ruta_script, "..", "..", "..", "assets")
        )

        # Cargar base de datos de la historia
        self.datos_historia = obtener_historia(self.ruta_assets)

        # --- FONDO PRINCIPAL ---
        self.cargar_fondo_principal()

        # --- INTERFAZ ---
        self.crear_interfaz()

        # Iniciamos la primera escena
        self.cargar_escena("inicio_cueva")

    def cargar_fondo_principal(self):
        ruta_fondo = os.path.join(self.ruta_assets, "fondo.png")
        try:
            img = ctk.CTkImage(Image.open(ruta_fondo), size=(800, 600))
            self.label_fondo = ctk.CTkLabel(self, image=img, text="")
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.label_fondo = ctk.CTkLabel(
                self, text="Fondo no encontrado", fg_color="#1a1a1a"
            )
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    def crear_interfaz(self):
        # 1. IMAGEN DE ESCENA (Superior)
        self.frame_escena = ctk.CTkFrame(self, fg_color="#000000", height=250)
        self.frame_escena.pack(pady=(20, 5), padx=20, fill="x")
        self.frame_escena.pack_propagate(False)

        self.imagen_escena_label = ctk.CTkLabel(
            self.frame_escena, text="", text_color="white"
        )
        self.imagen_escena_label.pack(fill="both", expand=True)

        # 2. LOG DE TEXTO (Central)
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

        self.log_texto.tag_config("opcion", foreground="#3b8ed0", underline=True)
        self.log_texto.bind("<Motion>", self._cambiar_cursor)

        # 3. ACCIONES FIJAS (Inferior)
        self.frame_acciones = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=10)
        self.frame_acciones.pack(pady=(0, 20), padx=20, fill="x")

        botones = [
            ("INVENTARIO", self.mostrar_inventario),
            ("MAPA", self.mostrar_mapa),
            ("GUARDAR", self.guardar_juego),
            ("SALIR", self.controlador.mostrar_menu_principal),
        ]

        for texto, comando in botones:
            color = "#c0392b" if texto == "SALIR" else "#3b8ed0"
            ctk.CTkButton(
                self.frame_acciones, text=texto, command=comando, fg_color=color
            ).pack(side="left", padx=10, pady=10, expand=True)

    def cargar_escena(self, id_escena):
        """Carga los datos de la escena desde el archivo externo"""
        escena = self.datos_historia.get(id_escena)

        if escena:
            # 1. Actualizar Imagen
            self.actualizar_imagen_escena(escena["imagen"])

            # 2. Actualizar Texto y Opciones
            self.escribir_en_log(escena["texto"], escena["opciones"])
        else:
            self.escribir_en_log(f"Error: La escena '{id_escena}' no existe.")

    def actualizar_imagen_escena(self, ruta_img):
        try:
            # Forzamos la actualización de la imagen superior
            img_pil = Image.open(ruta_img)
            # El tamaño debe coincidir con el frame_escena
            img_ctk = ctk.CTkImage(img_pil, size=(760, 250))
            self.imagen_escena_label.configure(image=img_ctk, text="")
        except Exception as e:
            self.imagen_escena_label.configure(
                image=None, text=f"Error al cargar: {os.path.basename(ruta_img)}"
            )

    def escribir_en_log(self, texto, opciones=None):
        self.log_texto.configure(state="normal")
        self.log_texto.insert("end", f"\n{texto}\n\n")

        if opciones:
            for nombre_visible, id_destino in opciones.items():
                tag_name = f"click_{id_destino}"
                self.log_texto.insert(
                    "end", f" > {nombre_visible}\n", ("opcion", tag_name)
                )
                self.log_texto.tag_bind(
                    tag_name,
                    "<Button-1>",
                    lambda e, d=id_destino: self.seleccionar_opcion(d),
                )
            self.log_texto.insert("end", "\n" + "-" * 40 + "\n")

        self.log_texto.configure(state="disabled")
        self.log_texto.see("end")

    def seleccionar_opcion(self, id_destino):
        # Aquí puedes añadir sonidos o efectos antes de cargar
        self.cargar_escena(id_destino)

    def _cambiar_cursor(self, event):
        tags = self.log_texto.tag_names(f"@{event.x},{event.y}")
        self.log_texto.configure(cursor="hand2" if "opcion" in tags else "arrow")

    # Métodos placeholder
    def mostrar_inventario(self):
        print("Inventario")

    def mostrar_mapa(self):
        print("Mapa")

    def guardar_juego(self):
        print("Guardado")
