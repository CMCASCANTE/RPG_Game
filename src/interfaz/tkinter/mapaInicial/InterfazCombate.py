class InterfazCombate:
    def __init__(self, interfaz, jugador, enemigos, escena_retorno):
        """
        Constructor del motor de combate.
        :param interfaz: Referencia a la clase MapaInicial (la vista).
        :param jugador: Objeto del jugador con sus stats (vida, fuerza).
        :param enemigos: Lista de objetos enemigo instanciados.
        :param escena_retorno: ID de la escena a la que volver tras ganar.
        """
        self.interfaz = interfaz
        self.jugador = jugador
        self.enemigos = enemigos
        self.escena_retorno = escena_retorno

    def generar_barra(self, actual, total, ancho=12):
        """
        Crea una representación visual de la salud.
        Ejemplo: [#######-----] 7/10
        """
        # Aseguramos que el porcentaje esté entre 0 y 1 para evitar errores de dibujo
        porcentaje = max(0, min(actual / total, 1))
        lleno = int(ancho * porcentaje)
        vacio = ancho - lleno
        return f"[{'#' * lleno}{'.' * vacio}]"

    def iniciar(self):
        """Punto de entrada: cambia la imagen y lanza el primer turno."""
        # Cambiamos la imagen del frame superior a una de batalla
        self.interfaz.actualizar_imagen_escena("assets/fondo_combate.png")
        self.mostrar_estado_actual("¡EL COMBATE COMIENZA!")

    def mostrar_estado_actual(self, prefacio="", mostrar_opciones=True):
        vivos = [e for e in self.enemigos if e.esta_vivo]

        if not vivos:
            self.finalizar_victoria()
            return

        # El cuerpo del mensaje solo mostrará el "prefacio" (el daño que acaba de ocurrir)
        # y la barra del jugador para tenerla siempre a la vista
        barra_jug = self.generar_barra(
            self.jugador.vida_actual, self.jugador.vida_max, ancho=15
        )
        hud_jugador = f"TU ESTADO: {barra_jug} {self.jugador.vida_actual}/{self.jugador.vida_max} HP\n"

        texto_final = f"{prefacio}"

        opciones = {}
        if mostrar_opciones:
            for i, en in enumerate(vivos):
                # CREAMOS LA BARRA PARA LA OPCIÓN
                barra_en = self.generar_barra(en.vida_actual, en.vida_max, ancho=8)
                # El texto del "botón" ahora incluye la vida del enemigo
                # Opcional - mantener el nombre en 12 caracteres para que todo se muestre homogeneo
                # label = f"{i} - Atacar a {en.nombre:<12} {barra_en} {en.vida_actual} HP"
                label = f"{i} - Atacar a {en.nombre} {barra_en} {en.vida_actual} HP"
                opciones[label] = f"MC_ATAQUE_{id(en)}"

            opciones["Intentar escapar"] = "MC_ESCAPE"
            texto_final = f"{prefacio}\n\n{hud_jugador}"

        self.interfaz.escribir_en_log(texto_final, opciones)

    def manejar_clic(self, id_destino):
        """Gestiona las pulsaciones capturadas por la interfaz."""
        if id_destino.startswith("MC_ATAQUE_"):
            # Extraemos la dirección de memoria enviada en el ID
            obj_id_str = id_destino.replace("MC_ATAQUE_", "")
            self.ejecutar_turno_ataque(obj_id_str)
            return True  # Confirmamos que el motor procesó la acción

        if id_destino == "MC_ESCAPE":
            self.interfaz.escribir_en_log("¡Has escapado del combate!")
            self.interfaz.combate_activo = None  # Liberamos el motor de la interfaz
            self.interfaz.cargar_escena(self.escena_retorno)
            return True
        return False

    def finalizar_victoria(self):
        """Cierre del combate y limpieza."""
        # Evitamos que se ejecute dos veces si por error se llama desde varios sitios
        if self.interfaz.combate_activo is None:
            return

        self.interfaz.escribir_en_log("¡VICTORIA! El combate ha terminado.")
        self.interfaz.combate_activo = (
            None  # Muy importante ponerlo a None antes de cargar escena
        )

        # Volvemos a la narrativa
        self.interfaz.cargar_escena(self.escena_retorno)

    def ejecutar_turno_ataque(self, obj_id_str):
        objetivo = next((e for e in self.enemigos if str(id(e)) == obj_id_str), None)
        if not objetivo:
            return

        # 1. Jugador ataca
        dano_j = objetivo.recibir_daño(self.jugador.daño_total)
        log_j = f"--- TU TURNO ---\n\nGolpeas a {objetivo.nombre} causando {dano_j} de daño."

        # Mostramos el daño del jugador y QUITAMOS las opciones para que no pueda clicar
        self.mostrar_estado_actual(prefacio=log_j, mostrar_opciones=False)

        # 2. Programamos el contraataque
        self.interfaz.after(1500, self.procesar_contraataque)

    def procesar_contraataque(self):
        log_e = "--- TURNO ENEMIGO ---\n\n"
        for en in self.enemigos:
            if en.esta_vivo:
                dano_e = self.jugador.recibir_daño(en.daño_total)
                log_e += f"» {en.nombre} te inflige {dano_e} de daño.\n"

        # Mostramos el daño de los enemigos (todavía sin opciones)
        self.mostrar_estado_actual(prefacio=log_e, mostrar_opciones=False)

        # 3. Tras otros 1.5 segundos, devolvemos el menú de ataque
        # Esto permite que el jugador lea el daño recibido antes de que salgan los botones
        self.interfaz.after(
            1500, lambda: self.mostrar_estado_actual(prefacio="¿Qué harás ahora?")
        )
