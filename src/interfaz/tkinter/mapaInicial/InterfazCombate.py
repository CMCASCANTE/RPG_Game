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
        """
        Renderiza toda la información en el log de texto.
        :param prefacio: Texto descriptivo de lo que acaba de ocurrir.
        :param mostrar_opciones: Si es False, oculta los botones para evitar clics durante animaciones.
        """
        # Filtramos quién sigue en pie
        vivos = [e for e in self.enemigos if e.esta_vivo]

        # Si no hay enemigos vivos, el motor termina
        if not vivos:
            self.finalizar_victoria()
            return

        # --- CONSTRUCCIÓN DEL HUD (BARRAS DE VIDA) ---
        hud = "\n" + "=" * 40 + "\n"
        # 1. Listamos enemigos
        for en in self.enemigos:
            barra = self.generar_barra(en.vida_actual, en.vida_max)
            status = "VIVO" if en.esta_vivo else "CAÍDO"
            # :<15 alinea el nombre a la izquierda con 15 caracteres de espacio
            if en.esta_vivo:
                hud += f" ENEMIGO: {en.nombre:<15} {barra} {en.vida_actual}/{en.vida_max} HP\n"

        hud += "-" * 40 + "\n"

        # 2. Añadimos la barra del Jugador (HUD PROPIO)
        barra_jug = self.generar_barra(
            self.jugador.vida_actual, self.jugador.vida_max, ancho=20
        )
        hud += f" TÚ:   {'JUGADOR':<15} {barra_jug} {self.jugador.vida_actual}/{self.jugador.vida_max} HP\n"
        hud += "=" * 40 + "\n"

        texto_final = f"{prefacio}\n{hud}"

        # --- GENERACIÓN DE OPCIONES CLICABLES ---
        opciones = {}
        if mostrar_opciones:
            texto_final += "\n¿A quién quieres atacar?"
            for i, en in enumerate(vivos):
                # Usamos id(en) para vincular el clic a la instancia exacta del objeto
                opciones[f"{i+ 1} - Atacar a {en.nombre}"] = f"MC_ATAQUE_{id(en)}"
            opciones["Intentar escapar"] = "MC_ESCAPE"

        # IMPORTANTE: El prefacio DEBE ir primero en la cadena de texto
        texto_final = f"{prefacio}\n{hud}"

        # Enviamos todo al log de la interfaz principal
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

    def ejecutar_turno_ataque(self, obj_id_str):
        """Fase 1 del turno: El jugador golpea."""
        objetivo = next((e for e in self.enemigos if str(id(e)) == obj_id_str), None)
        if not objetivo:
            return

        # Capturamos el daño exacto devuelto por la lógica del objeto
        dano_j = objetivo.recibir_daño(self.jugador.daño_total)

        # Construimos un mensaje detallado
        log_jugador = (
            f"--- [ TURNO DEL JUGADOR ] ---\n"
            f"» Atacas a {objetivo.nombre}.\n"
            f"» ¡Le has infligido {dano_j} puntos de daño!"
        )

        if not objetivo.esta_vivo:
            log_jugador += f"\n» ¡{objetivo.nombre} ha sido derrotado!"

        # Actualizamos la pantalla con el mensaje (prefacio)
        self.mostrar_estado_actual(prefacio=log_jugador, mostrar_opciones=False)

        # Retraso para el contraataque
        self.interfaz.after(1200, self.procesar_contraataque)

    def procesar_contraataque(self):
        """Fase 2 del turno: Los enemigos responden."""
        log_enemigos = "--- [ TURNO ENEMIGO ] ---\n"
        hay_enemigos_vivos = False

        for en in self.enemigos:
            if en.esta_vivo:
                hay_enemigos_vivos = True
                # El jugador recibe el daño y guardamos la cifra
                dano_recibido = self.jugador.recibir_daño(en.daño_total)
                log_enemigos += f"» {en.nombre} te golpea: -{dano_recibido} HP.\n"

        if not hay_enemigos_vivos:
            log_enemigos = "No quedan enemigos en pie para contraatacar."

        # Comprobación de salud del jugador (opcional)
        if self.jugador.vida_actual <= 0:
            log_enemigos += "\n¡HAS CAÍDO EN COMBATE!"

        # Mostramos el resultado final del turno y devolvemos los botones
        self.mostrar_estado_actual(prefacio=log_enemigos, mostrar_opciones=True)
