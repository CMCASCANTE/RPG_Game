import os


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

            # Lanzamos bucle para controlar el menú de acciones para cada turno
            while True:
                # Menú de selección
                print(
                    f"\n--- Turno de {self.jugador.nombre} (HP: {self.jugador.vida_actual}/{self.jugador.vida_max}) ---"
                )
                print("1. Atacar")
                print("2. Abrir Inventario")
                print("3. Ver atributos del personaje")

                opcion = input("Elige una acción: ")

                # Opción 1 - Ataque
                # menu para seleccionar el objetivo a atacar
                if opcion == "1":
                    # Lanzamos un bucle infinito igual que en el menú anterior
                    # del que se saldrá al usar un break
                    while True:
                        # Enumeramos por pantalla los enemigos
                        # Comenzamos a contar desde el 1 para que mejor visualmente
                        for i, e in enumerate(vivos, start=1):
                            print(f"{i}: {e.nombre} ({e.vida_actual} HP)")
                        # Controlamos los errores, para que en caso de que
                        # se indique cualquier valor que no esté contemplado
                        # no se haga nada y se repita el bucle
                        try:
                            target = int(input("¿A quién atacas?: "))
                            # Devolvemos la opción correspondiente y el enemigo que se ha seleccionado
                            # Restamos 1 ya que desde el enumerate hemos empezado por 1 en vez de 0
                            # para que sea mas eficiente visualmente

                            print(
                                f"\n⚔️ {self.jugador.nombre} ataca a {vivos[target - 1].nombre} con {self.jugador.arma_equipada.nombre if self.jugador.arma_equipada else "sus puños"}!"
                            )
                            print(
                                f"{vivos[target - 1].nombre} recibió {vivos[target - 1].recibir_daño(self.jugador.daño_total)} de daño. Vida restante: {vivos[target - 1].vida_actual}/{vivos[target - 1].vida_max}"
                            )
                            break
                        except:
                            pass

                # Opcion 2 - Inventario
                # Menu para la selección de items
                elif opcion == "2":
                    # Si no hay items en el inventario, lanzamos ataque por defecto
                    if not self.jugador.inventario:
                        print("¡El inventario está vacío!")

                    # Si hay items, lanzamos menú para seleccionar 1
                    # Como en los anteriores menus, lanzamos bucle infinito
                    # del que se sale solo si se llega a un return
                    while True:
                        # Enumeramos los items
                        for i, item in enumerate(self.jugador.inventario, start=1):
                            print(f"{i}: {item.nombre} - {item.descripcion}")
                        # Controlamos errores para que no se haga nada si la opción
                        # introducida no es válida, y se vuelva a cargar el menú
                        try:
                            item_idx = int(
                                input("Elige un objeto (o nada para volver): ")
                            )
                            item = self.jugador.inventario.pop(item_idx - 1)
                            if item.tipo == "curacion":
                                # Si no da error (como por ejemplo que el número exceda el indice)
                                # Sacamos el item del inventario con pop y lo usamos
                                print(
                                    f"✨ {self.jugador.nombre} recuperó {item.usar(self.jugador)} HP."
                                )
                            if item.tipo == "fuerza":
                                print(
                                    f"🔥 ¡La fuerza de {self.jugador.nombre} aumentó en {item.usar(self.jugador)}!"
                                )
                            self.iniciar_batalla()
                        except Exception as e:
                            print(e)

                # Opción para mostrar las estadisticas del personaje
                elif opcion == "3":
                    # Mostramos las estadisticas
                    print("- " * 20)
                    print("Estadisticas del personaje")
                    print("- " * 20)
                    print(f"Nombre: {self.jugador.nombre}")
                    print(f"Clase: {self.jugador.clase}")
                    print(
                        f"Vida actual: {self.jugador.vida_actual}/{self.jugador.vida_max}"
                    )
                    print(f"Fuerza: {self.jugador.fuerza}")
                    print(f"Defensa: {self.jugador.defensa}")
                    print("Equipo:")
                    print(
                        f" - Arma: {self.jugador.arma_equipada.nombre} | Daño: 1d{self.jugador.arma_equipada.bonificador_fuerza}"
                    )
                    print(
                        f" - Armadura: {self.jugador.armadura_equipada.nombre} | Defensa: {self.jugador.armadura_equipada.bonificador_defensa}"
                    )
                    print("Objetos utilizables:")
                    for obj in self.jugador.inventario:
                        print(f" - {obj.nombre}")
                    input("Pulsa una tecla para volver al menú...")
                    self.iniciar_batalla()

                else:
                    continue

                # Turno de los enemigos (estos solo atacan)
                for e in vivos:
                    if e.esta_vivo and self.jugador.esta_vivo:
                        print(
                            f"\n⚔️ {e.nombre} ataca con {e.arma_equipada.nombre if e.arma_equipada else "sus puños"}!!"
                        )
                        print(
                            f"{self.jugador.nombre} recibió {self.jugador.recibir_daño(e.daño_total)} de daño. Vida restante: {self.jugador.vida_actual}/{self.jugador.vida_max}"
                        )
                # Si han atacado es por que se ha llegado al fin del bucle
                # Por lo que lo cortamos para que revise
                # quien sigue vivo y quien no (que es el bucle principal)
                input("Pulsa una tecla para volver al menú...")
                opcion = ""
                os.system("clear")
                break

        # Si terminamos el bucle y el jugador sigue vivo hemos ganado
        if self.jugador.esta_vivo:
            print("\n🏆 ¡HAS GANADO LA BATALLA!")
            return True
        # Si no sigue vivo hemos perdido
        else:
            print("\n💀 Has sido derrotado...")
            return False
