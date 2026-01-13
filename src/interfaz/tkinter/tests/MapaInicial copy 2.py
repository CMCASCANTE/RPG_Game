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

        # --- FONDO ---
        # Usamos 'self' como master, no los frames dentro de él.
        # 'place' permite que el fondo flote detrás de todo sin afectar al 'pack'.
        self.label_fondo = ctk.CTkLabel(self, image=self.img_fondo_ctk, text="")
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # --- INTERFAZ ---
        # Ahora todos los contenedores tienen como master a 'self'
        self.crear_interfaz()
        self.cargar_escena("inicio_cueva")

    def crear_interfaz(self):
        # --- SECCIÓN SUPERIOR: IMAGEN DE ESCENA ---
        self.frame_escena = ctk.CTkFrame(
            self,
            fg_color="#000000",  # Negro puro para que resalte la imagen
            corner_radius=10,
            height=250,
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

        # --- SECCIÓN CENTRAL: LOG DE TEXTO Y OPCIONES ---
        self.frame_log_opciones = ctk.CTkFrame(
            self,
            fg_color="#242424",  # Gris muy oscuro (sustituye al rgba 0.7)
            corner_radius=10,
        )
        self.frame_log_opciones.pack(pady=10, padx=20, fill="both", expand=True)

        self.log_texto = ctk.CTkTextbox(
            self.frame_log_opciones,
            font=("Fixedsys", 16),
            text_color="white",
            fg_color="transparent",  # Aquí sí funciona transparent porque hereda del frame
            wrap="word",
            state="disabled",
        )
        self.log_texto.pack(pady=10, padx=10, fill="both", expand=True)

        self.frame_opciones = ctk.CTkFrame(
            self.frame_log_opciones, fg_color="transparent"
        )
        self.frame_opciones.pack(pady=(0, 10), padx=10, fill="x")

        # --- SECCIÓN INFERIOR: BOTONES DE ACCIONES FIJAS ---
        self.frame_acciones_fijas = ctk.CTkFrame(
            self,
            fg_color="#1a1a1a",  # Un tono ligeramente distinto para diferenciar
            corner_radius=10,
        )
        self.frame_acciones_fijas.pack(pady=(0, 20), padx=20, fill="x")

        self.inner_frame_acciones = ctk.CTkFrame(
            self.frame_acciones_fijas, fg_color="transparent"
        )
        self.inner_frame_acciones.pack(pady=10)

    def tomar_decision(self, decision):
        self.escribir_en_log(f"\n> HAS ELEGIDO: {decision.upper()}")

        if decision == "cueva":
            self.escribir_en_log("Has entrado en la cueva. Está muy oscuro...")
            self.cargar_escena("dentro_cueva")
        elif decision == "buscar":
            self.escribir_en_log(
                "Has encontrado una vieja antorcha en el suelo. ¡Útil!"
            )
            self.cargar_escena("antorcha_encontrada")

    def escribir_en_log(self, texto):
        """Función auxiliar para añadir texto al log fácilmente"""
        self.log_texto.configure(state="normal")
        self.log_texto.insert("end", f"{texto}\n")
        self.log_texto.configure(state="disabled")
        self.log_texto.see("end")  # Scroll automático

    def cargar_escena(self, id_escena):
        # Limpiar botones de opciones anteriores
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()

        if id_escena == "inicio_cueva":
            self.escribir_en_log(
                "Estás en la entrada de una cueva oscura. ¿Qué quieres hacer?"
            )
            ctk.CTkButton(
                self.frame_opciones,
                text="Entrar en la cueva",
                command=lambda: self.tomar_decision("cueva"),
            ).pack(pady=5, fill="x")
            ctk.CTkButton(
                self.frame_opciones,
                text="Buscar alrededor",
                command=lambda: self.tomar_decision("buscar"),
            ).pack(pady=5, fill="x")

        elif id_escena == "dentro_cueva":
            self.escribir_en_log(
                "Estás dentro de la cueva. Apenas ves nada. Un ruido te asusta."
            )
            ctk.CTkButton(
                self.frame_opciones,
                text="Encender una antorcha",
                command=lambda: self.tomar_decision("antorcha"),
            ).pack(pady=5, fill="x")
            ctk.CTkButton(
                self.frame_opciones,
                text="Intentar huir",
                command=lambda: self.tomar_decision("huir"),
            ).pack(pady=5, fill="x")

    # --- MÉTODOS DE SOPORTE ---
    def actualizar_imagen_escena(self, ruta_nueva_imagen):
        try:
            img = Image.open(ruta_nueva_imagen)
            nueva_img = ctk.CTkImage(
                img, img, size=(self.frame_escena.winfo_width(), 250)
            )
            self.imagen_escena_label.configure(image=nueva_img, text="")
        except Exception as e:
            print(f"Error al cargar imagen: {e}")

    def mostrar_inventario(self):
        print("Inventario abierto")

    def mostrar_mapa(self):
        print("Mapa abierto")

    def guardar_juego(self):
        print("Partida guardada")
