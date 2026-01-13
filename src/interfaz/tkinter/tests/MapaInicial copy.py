import customtkinter as ctk
from PIL import Image
import os


class MapaInicial(ctk.CTkFrame):

    def __init__(self, master, controlador):
        super().__init__(master, fg_color="black")
        self.controlador = controlador

        # --- CARGAR FONDO ---
        ruta_script = os.path.dirname(__file__)
        ruta_img = os.path.join(ruta_script, "..", "..", "..", "assets", "fondo.png")
        self.img_fondo = ctk.CTkImage(Image.open(ruta_img), size=(800, 600))

        self.label_fondo = ctk.CTkLabel(self, image=self.img_fondo, text="")
        self.label_fondo.place(relwidth=1, relheight=1)

        self.label = ctk.CTkLabel(self, text="ESTÁS EN EL JUEGO", font=("Arial", 30))
        self.label.pack(pady=50)

        self.btn_volver = ctk.CTkButton(
            self,
            text="VOLVER AL MENÚ",
            command=lambda: self.controlador.mostrar_menu_principal(),
        )
        self.btn_volver.pack()
        self.mostrar_interfaz_juego()

    def mostrar_interfaz_juego(self):

        # --- SECCIÓN SUPERIOR: IMAGEN DE ESCENA ---
        # Este Frame contendrá la imagen de la escena actual
        self.frame_escena = ctk.CTkFrame(
            self.label_fondo_juego, fg_color="black", corner_radius=10
        )
        self.frame_escena.pack(pady=10, padx=20, fill="x", expand=False)
        self.frame_escena.configure(
            height=250
        )  # Altura fija para la imagen de la escena

        # Placeholder para la imagen de la escena
        self.imagen_escena_label = ctk.CTkLabel(
            self.frame_escena,
            text="IMAGEN DE LA ESCENA",
            text_color="white",
            font=("Fixedsys", 20),
        )
        self.imagen_escena_label.pack(fill="both", expand=True)
        # Ejemplo: cargar una imagen de escena (tendrías que tener más en una carpeta)
        # ruta_escena = os.path.join(ruta_script, "../../../assets", "escena_bosque.png")
        # escena_img = ctk.CTkImage(Image.open(ruta_escena), size=(self.frame_escena.winfo_width(), 250))
        # self.imagen_escena_label.configure(image=escena_img)

        # --- SECCIÓN CENTRAL: LOG DE TEXTO Y OPCIONES ---
        # Este Frame contendrá el texto de la historia y los botones de opciones
        self.frame_log_opciones = ctk.CTkFrame(
            self.label_fondo_juego, fg_color="rgba(0,0,0,0.7)", corner_radius=10
        )  # Fondo semitransparente
        self.frame_log_opciones.pack(pady=10, padx=20, fill="both", expand=True)

        # Log de texto (donde se narra la historia)
        self.log_texto = ctk.CTkTextbox(
            self.frame_log_opciones,
            font=("Fixedsys", 16),
            text_color="white",
            fg_color="transparent",
            wrap="word",  # Envuelve el texto al llegar al final de la línea
            state="disabled",  # Por defecto, el usuario no puede editarlo
        )
        self.log_texto.pack(pady=10, padx=10, fill="both", expand=True)
        self.log_texto.configure(state="normal")
        self.log_texto.insert(
            "end", "Estás en la entrada de una cueva oscura. ¿Qué quieres hacer?\n"
        )
        self.log_texto.configure(state="disabled")

        # Frame para las opciones (botones interactivos)
        self.frame_opciones = ctk.CTkFrame(
            self.frame_log_opciones, fg_color="transparent"
        )
        self.frame_opciones.pack(pady=(0, 10), padx=10, fill="x")

        # Ejemplo de botones de opción (estos se generarían dinámicamente)
        self.btn_opcion1 = ctk.CTkButton(
            self.frame_opciones,
            text="Entrar en la cueva",
            command=lambda: self.tomar_decision("cueva"),
        )
        self.btn_opcion1.pack(pady=5, fill="x")
        self.btn_opcion2 = ctk.CTkButton(
            self.frame_opciones,
            text="Buscar alrededor",
            command=lambda: self.tomar_decision("buscar"),
        )
        self.btn_opcion2.pack(pady=5, fill="x")

        # --- SECCIÓN INFERIOR: BOTONES DE ACCIONES FIJAS ---
        self.frame_acciones_fijas = ctk.CTkFrame(
            self.label_fondo_juego, fg_color="rgba(0,0,0,0.8)", corner_radius=10
        )
        self.frame_acciones_fijas.pack(pady=(0, 10), padx=20, fill="x")

        # Frame para centrar los botones
        self.inner_frame_acciones = ctk.CTkFrame(
            self.frame_acciones_fijas, fg_color="transparent"
        )
        self.inner_frame_acciones.pack(pady=5)

        # Botones de acciones fijas
        self.btn_inventario = ctk.CTkButton(
            self.inner_frame_acciones,
            text="Inventario",
            command=self.mostrar_inventario,
        )
        self.btn_inventario.pack(side="left", padx=5)

        self.btn_mapa = ctk.CTkButton(
            self.inner_frame_acciones, text="Mapa", command=self.mostrar_mapa
        )
        self.btn_mapa.pack(side="left", padx=5)

        self.btn_guardar = ctk.CTkButton(
            self.inner_frame_acciones, text="Guardar", command=self.guardar_juego
        )
        self.btn_guardar.pack(side="left", padx=5)

        self.btn_volver_menu = ctk.CTkButton(
            self.inner_frame_acciones, text="Menú", command=self.mostrar_menu_principal
        )
        self.btn_volver_menu.pack(side="left", padx=5)

        # Al iniciar, cargamos la primera escena
        self.cargar_escena("inicio_cueva")

    def tomar_decision(self, decision):
        # Lógica para manejar las decisiones del jugador
        if decision == "cueva":
            self.log_texto.configure(state="normal")
            self.log_texto.insert(
                "end", "\nHas entrado en la cueva. Está muy oscuro...\n"
            )
            self.log_texto.configure(state="disabled")
            self.cargar_escena("dentro_cueva")
        elif decision == "buscar":
            self.log_texto.configure(state="normal")
            self.log_texto.insert(
                "end", "\nHas encontrado una vieja antorcha en el suelo. ¡Útil!\n"
            )
            self.log_texto.configure(state="disabled")
            self.cargar_escena("antorcha_encontrada")

    def cargar_escena(self, id_escena):
        # Aquí es donde cambiarías la imagen superior y el texto de las opciones
        # dependiendo de la 'id_escena'.

        # Primero, limpiar opciones anteriores
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()

        if id_escena == "inicio_cueva":
            self.log_texto.configure(state="normal")
            self.log_texto.delete(1.0, "end")  # Borrar contenido anterior
            self.log_texto.insert(
                "end", "Estás en la entrada de una cueva oscura. ¿Qué quieres hacer?\n"
            )
            self.log_texto.configure(state="disabled")
            # Cargar imagen de la entrada de la cueva
            # self.actualizar_imagen_escena("ruta/a/imagen_entrada_cueva.png")
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
            self.log_texto.configure(state="normal")
            self.log_texto.delete(1.0, "end")
            self.log_texto.insert(
                "end",
                "Estás dentro de la cueva. Apenas ves nada. Un ruido te asusta. ¿Qué haces?\n",
            )
            self.log_texto.configure(state="disabled")
            # Cargar imagen del interior de la cueva
            # self.actualizar_imagen_escena("ruta/a/imagen_interior_cueva.png")
            ctk.CTkButton(
                self.frame_opciones,
                text="Encender una antorcha (si tienes)",
                command=lambda: self.tomar_decision("antorcha"),
            ).pack(pady=5, fill="x")
            ctk.CTkButton(
                self.frame_opciones,
                text="Intentar huir",
                command=lambda: self.tomar_decision("huir"),
            ).pack(pady=5, fill="x")

        elif id_escena == "antorcha_encontrada":
            self.log_texto.configure(state="normal")
            self.log_texto.delete(1.0, "end")
            self.log_texto.insert(
                "end",
                "¡Encontraste una antorcha! Ahora puedes ver un poco mejor. ¿Qué haces ahora?\n",
            )
            self.log_texto.configure(state="disabled")
            # Cargar imagen de la antorcha encontrada
            # self.actualizar_imagen_escena("ruta/a/imagen_antorcha_encontrada.png")
            ctk.CTkButton(
                self.frame_opciones,
                text="Entrar en la cueva (con antorcha)",
                command=lambda: self.tomar_decision("cueva_con_antorcha"),
            ).pack(pady=5, fill="x")
            ctk.CTkButton(
                self.frame_opciones,
                text="Volver al inicio",
                command=lambda: self.cargar_escena("inicio_cueva"),
            ).pack(pady=5, fill="x")

        # Puedes añadir más elif para cada escena de tu juego

    def actualizar_imagen_escena(self, ruta_nueva_imagen):
        # Esta función cargaría una nueva imagen en el frame superior
        try:
            nueva_img = ctk.CTkImage(
                light_image=Image.open(ruta_nueva_imagen),
                dark_image=Image.open(ruta_nueva_imagen),
                size=(
                    self.frame_escena.winfo_width(),
                    self.frame_escena.winfo_height(),
                ),
            )
            self.imagen_escena_label.configure(image=nueva_img, text="")
        except FileNotFoundError:
            self.imagen_escena_label.configure(
                text=f"Imagen no encontrada: {os.path.basename(ruta_nueva_imagen)}"
            )
            print(f"Error: No se encontró la imagen de escena en {ruta_nueva_imagen}")

    def mostrar_inventario(self):
        print("Abriendo inventario...")
        # Aquí podrías abrir una nueva ventana o un frame emergente

    def mostrar_mapa(self):
        print("Mostrando mapa...")

    def guardar_juego(self):
        print("Guardando partida...")
