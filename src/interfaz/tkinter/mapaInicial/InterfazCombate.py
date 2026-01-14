class InterfazCombate:

    def __init__(self, interfaz, jugador, enemigos, escena_retorno, siguiente_escena):
        self.interfaz = interfaz
        self.jugador = jugador
        self.enemigos = enemigos
        self.escena_retorno = escena_retorno
        self.siguiente_escena = siguiente_escena
        # Añadimos un estado para saber qué menú estamos pintando
        self.estado_menu = "PRINCIPAL"

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
        if (
            not vivos and self.estado_menu != "PRINCIPAL"
        ):  # Evitar errores si todos mueren
            # self.finalizar_victoria()
            self.interfaz.escribir_en_log(f"{prefacio}\n\n")
            self.interfaz.after(1500, self.finalizar_victoria)
            return

        barra_jug = self.generar_barra(
            self.jugador.vida_actual, self.jugador.vida_max, ancho=15
        )
        hud_jugador = f"TU ESTADO: {barra_jug} {self.jugador.vida_actual}/{self.jugador.vida_max} HP\n"
        texto_final = f"{prefacio}\n\n"

        opciones = {}
        if mostrar_opciones:
            texto_final = f"{prefacio}\n\n{hud_jugador}"
            if self.estado_menu == "PRINCIPAL":
                opciones["⚔️ Atacar"] = "MC_MENU_ATACAR"
                opciones["✨ Habilidades"] = "MC_MENU_HABILIDADES"
                opciones["🏃 Huir"] = "MC_ESCAPE"

            elif self.estado_menu == "ATACAR":
                for i, en in enumerate(vivos):
                    barra_en = self.generar_barra(en.vida_actual, en.vida_max, ancho=8)
                    label = f"{i+1} - {en.nombre} {barra_en} {en.vida_actual} HP"
                    opciones[label] = f"MC_EJECUTAR_ATAQUE_{id(en)}"
                opciones["⬅️ Volver"] = "MC_MENU_PRINCIPAL"

            elif self.estado_menu == "HABILIDADES":
                # Aquí listamos las habilidades (puedes traerlas del objeto jugador)
                for hab in self.jugador.habilidades:
                    opciones[f"🩹 {hab.nombre}"] = f"MC_HAB_USAR_{hab.nombre}"
                opciones["⬅️ Volver"] = "MC_MENU_PRINCIPAL"

        self.interfaz.escribir_en_log(texto_final, opciones)

    def manejar_clic(self, id_destino):
        """Gestiona el flujo de los menús"""
        # Navegación de menús
        if id_destino == "MC_MENU_HABILIDADES":
            self.estado_menu = "HABILIDADES"
            self.mostrar_estado_actual(prefacio="Selecciona una habilidad:")
            return True

        # Acciones de Habilidad
        if "MC_HAB_USAR_" in id_destino:
            nombre_habilidad = id_destino.replace("MC_HAB_USAR_", "")
            self.ejecutar_turno_habilidad(nombre_habilidad)
            return True

        # Resto de acciones
        if id_destino == "MC_MENU_ATACAR":
            self.estado_menu = "ATACAR"
            self.mostrar_estado_actual(prefacio="¿A quién quieres atacar?")
            return True

        if id_destino == "MC_MENU_PRINCIPAL":
            self.estado_menu = "PRINCIPAL"
            self.mostrar_estado_actual(prefacio="¿Qué harás ahora?")
            return True

        # Ejecución de acciones
        if id_destino.startswith("MC_EJECUTAR_ATAQUE_"):
            obj_id_str = id_destino.replace("MC_EJECUTAR_ATAQUE_", "")
            self.ejecutar_turno_ataque(obj_id_str)
            return True

        if id_destino == "MC_ESCAPE":
            self.interfaz.escribir_en_log("¡Has escapado del combate!")
            self.interfaz.combate_activo = None  # Muy importante para liberar el motor
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
        self.interfaz.after(
            1500, lambda: self.interfaz.cargar_escena(self.siguiente_escena)
        )

    def ejecutar_turno_ataque(self, obj_id_str):
        objetivo = next((e for e in self.enemigos if str(id(e)) == obj_id_str), None)
        if not objetivo:
            return

        # 1. Jugador ataca
        dano_j = objetivo.recibir_daño(self.jugador.daño_total)
        log_j = f"--- TU TURNO ---\n\nGolpeas a {objetivo.nombre} causando {dano_j} de daño."

        # Mostramos el daño del jugador y QUITAMOS las opciones para que no pueda clicar
        self.mostrar_estado_actual(prefacio=log_j, mostrar_opciones=False)

        if [e for e in self.enemigos if e.esta_vivo]:
            # Programamos el contraataque
            self.interfaz.after(1500, self.procesar_contraataque)

    def ejecutar_turno_habilidad(self, nombre_habilidad):
        vivos = [e for e in self.enemigos if e.esta_vivo]
        log_danios = ""
        for hab in self.jugador.habilidades:
            if hab.nombre == nombre_habilidad:
                resultado = self.jugador.usar_habilidad(hab, vivos)
                log_danios += f"{hab.descripcion_uso}\n\n"

        # Obtenemos los daños desde los resultados de usar la habilidad
        danios = resultado["efectos"].values()

        # Describimos los daños recibidos por cada entidad
        for elm in danios:
            data = list(elm.items())[0]
            log_danios += f"\n{data[0].nombre} recibió {data[1]} de daño. Vida restante: {data[0].vida_actual}/{data[0].vida_max}"

        # # Mostramos el daño del jugador y QUITAMOS las opciones para que no pueda clicar
        self.mostrar_estado_actual(prefacio=log_danios, mostrar_opciones=False)

        if [e for e in self.enemigos if e.esta_vivo]:
            # Programamos el contraataque
            self.interfaz.after(2500, self.procesar_contraataque)

    def procesar_contraataque(self):
        log_e = "--- TURNO ENEMIGO ---\n\n"
        for en in self.enemigos:
            if en.esta_vivo:
                dano_e = self.jugador.recibir_daño(en.daño_total)
                log_e += f"» {en.nombre} te inflige {dano_e} de daño.\n"

        # Mostramos el daño del enemigo (seguimos sin opciones)
        self.mostrar_estado_actual(prefacio=log_e, mostrar_opciones=False)

        # AHORA SÍ, tras ver el daño enemigo, esperamos para volver al menú
        self.interfaz.after(1500, self.resetear_turno)

    def resetear_turno(self):
        """Vuelve al menú principal tras terminar todas las animaciones de daño"""
        self.estado_menu = "PRINCIPAL"
        self.mostrar_estado_actual(prefacio="Elige tu siguiente movimiento:")
