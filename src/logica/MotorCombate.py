class MotorCombate:

    # Creamos el objeto con los jugadores y los enemigos que van a
    # entrar en combate
    def __init__(self, jugador, enemigos):
        self.jugador = jugador
        self.enemigos = enemigos

    # Lógica de combate
    # Mientras el jugador y alguno de los enemigos estan vivos se repite
    # la mecánica
    def iniciar_batalla(self):
        while self.jugador.esta_vivo and any(e.esta_vivo for e in self.enemigos):

            # Como primer paso filtramos enemigos vivos
            vivos = [e for e in self.enemigos if e.esta_vivo]

            # Lanzamos la acción del Jugador que nos devolvera 1 de 2 opciones
            tipo, valor = self.jugador.seleccionar_accion(vivos)

            # Si la opción elegida es atacar, restamos vida del enemigo que nos
            # devuelve el método .seleccionar_accion
            if tipo == "atacar":
                print(
                    f"\n⚔️ {self.jugador.nombre} ataca a {valor.nombre} con {self.jugador.arma_equipada.nombre if self.jugador.arma_equipada else "sus puños"}!"
                )
                valor.recibir_daño(self.jugador.daño_total)

            # Si la opción elegida es usar un item, este se restará de la lista de items
            # dentro del método .seleccionar_accion, por lo que solo nos queda usarlo sobre el jugador
            elif tipo == "objeto":
                valor.usar(self.jugador)

            # Si la opción elegida es consultar las estadisticas
            # se muestran desde la función del propio personaje
            # y se vuelve a cargar el menu de selección
            # por lo que no existe como acción en el motor de combate

            # Turno de los enemigos (estos solo atacan)
            for e in vivos:
                if e.esta_vivo and self.jugador.esta_vivo:
                    print(
                        f"\n⚔️ {e.nombre} ataca con {e.arma_equipada.nombre if e.arma_equipada else "sus puños"}!!"
                    )
                    self.jugador.recibir_daño(e.daño_total)

        # Si terminamos el bucle y el jugador sigue vivo hemos ganado
        if self.jugador.esta_vivo:
            print("\n🏆 ¡HAS GANADO LA BATALLA!")
            return True
        # Si no sigue vivo hemos perdido
        else:
            print("\n💀 Has sido derrotado...")
            return False
