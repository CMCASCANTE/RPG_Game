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
                # Limpiamos la pantalla
                os.system("clear")
                # Menú de selección
                print(
                    f"\n--- Turno de {self.jugador.nombre} (HP: {self.jugador.vida_actual}/{self.jugador.vida_max}) ---"
                )
                print("1. Atacar")
                print("2. Usar habilidad")
                print("3. Abrir Inventario")
                print("4. Ver atributos del personaje")
                print("5. Ver enemigos")

                opcion = input("Elige una acción: ")

                # Opción 1 - Ataque
                # menu para seleccionar el objetivo a atacar
                if opcion == "1":
                    # Enumeramos por pantalla los enemigos
                    # Comenzamos a contar desde el 1 para que mejor visualmente
                    for i, e in enumerate(vivos, start=1):
                        print(f"{i}: {e.nombre} ({e.vida_actual} HP)")
                    # Controlamos los errores, para que en caso de que
                    # se indique cualquier valor que no esté contemplado
                    # se vuelva a lanzar el menú inicial
                    try:
                        target = int(
                            input("¿A quién atacas?(ninguno para volver atrás): ")
                        )
                        # Devolvemos la opción correspondiente y el enemigo que se ha seleccionado
                        # Restamos 1 ya que desde el enumerate hemos empezado por 1 en vez de 0
                        # para que sea mas eficiente visualmente
                        # Limpiamos la consola tras elegir la habilidad (por claridad de la interfaz)
                        os.system("clear")
                        print(
                            f"\n⚔️ {self.jugador.nombre} ataca a {vivos[target - 1].nombre} con {self.jugador.arma_equipada.nombre if self.jugador.arma_equipada else "sus puños"}!"
                        )
                        print(
                            f"{vivos[target - 1].nombre} recibió {vivos[target - 1].recibir_daño(self.jugador.daño_total)} de daño. Vida restante: {vivos[target - 1].vida_actual}/{vivos[target - 1].vida_max}"
                        )
                    except:
                        continue

                # Opción 2 - Habilidades
                # menu para seleccionar la habilidad
                elif opcion == "2":
                    # Enumeramos las habilidades
                    for i, item in enumerate(self.jugador.habilidades, start=1):
                        print(
                            f"{i}: {item.nombre} | Coste: {item.coste} | Daño: {item.daño}"
                        )
                    # Controlamos errores para que no se haga nada si la opción
                    # introducida no es válida, y se vuelva a cargar el menú
                    try:
                        skill_idx = int(
                            input("Elige una habilidad (o ninguna para volver atrás): ")
                        )
                        skill = self.jugador.habilidades[skill_idx - 1]
                        # Lanzamos la habilidad y guardamos el resultado
                        # que es un dict con diferentes valores
                        datos_habilidad = self.jugador.usar_habilidad(skill, vivos)
                        # Si nos ha devuelto algo es que se ha podido usar
                        if datos_habilidad:
                            # Limpiamos la consola tras elegir la habilidad (por claridad de la interfaz)
                            os.system("clear")
                            # Mostramos la descripción de la habilidad
                            print(skill.descripcion_uso)
                            # Guardamos el valor de "efectos", que es un dict
                            # con las entidades a las que ha afectado y los daños recibidos
                            danios = datos_habilidad["efectos"].values()
                            # Describimos los daños recibidos por cada entidad
                            for elm in danios:
                                data = list(elm.items())[0]
                                print(
                                    f"\n{data[0].nombre} recibió {data[1]} de daño. Vida restante: {data[0].vida_actual}/{data[0].vida_max}"
                                )
                        # Si no ha devuelto nada (None) es por que no habia esencia para lanzarla
                        else:
                            print(
                                f"No tienes esencia suficiente para usar {skill.nombre}"
                            )
                            input("\nPulsa una tecla para volver al menú...")
                            continue
                    except:
                        continue

                # Opcion 3 - Inventario
                # Menu para la selección de items
                elif opcion == "3":
                    # Si no hay items en el inventario, lanzamos ataque por defecto
                    if not self.jugador.inventario:
                        print("¡El inventario está vacío!")
                        input("\nPulsa una tecla para volver al menú...")
                        continue

                    # Enumeramos los items
                    for i, item in enumerate(self.jugador.inventario, start=1):
                        print(f"{i}: {item.nombre} - {item.descripcion}")
                    # Controlamos errores para que no se haga nada si la opción
                    # introducida no es válida, y se vuelva a cargar el menú
                    try:
                        item_idx = int(input("Elige un objeto (o nada para volver): "))
                        # Limpiamos la consola tras elegir la habilidad (por claridad de la interfaz)
                        os.system("clear")
                        item = self.jugador.inventario.pop(item_idx - 1)
                        # Usamos el item y guardamos los resultados
                        datos_item = item.usar(self.jugador)
                        print(
                            f"✨ {self.jugador.nombre} ha usado un item de {datos_item["tipo"]} obteniendo {datos_item["cantidad"]} de {datos_item["atributo"]}"
                        )
                        input("\nPulsa una tecla para volver al menú...")
                        break
                    except:
                        break

                # Opción para mostrar las estadisticas del personaje
                elif opcion == "4":
                    # Limpiamos la consola tras elegir la habilidad (por claridad de la interfaz)
                    os.system("clear")
                    # Mostramos las estadisticas
                    print("- " * 20)
                    print("Estadisticas del personaje")
                    print("- " * 20)
                    print(f"Nombre: {self.jugador.nombre}")
                    print(f"Clase: {self.jugador.clase}")
                    print(
                        f"Vida actual: {self.jugador.vida_actual}/{self.jugador.vida_max}"
                    )
                    print(
                        f"Esencia actual: {self.jugador.esencia_actual}/{self.jugador.esencia_max}"
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
                    print("Habilidades:")
                    for obj in self.jugador.habilidades:
                        print(
                            f" - {obj.nombre} | Coste: {obj.coste} | Daño: {obj.daño}"
                        )
                        print(f"   - {obj.descripcion}")
                    print("Objetos utilizables:")
                    for obj in self.jugador.inventario:
                        print(f" - {obj.nombre}")
                    input("\nPulsa una tecla para volver al menú...")
                    continue

                # Opción para mostrar los enemigos
                elif opcion == "5":
                    # Limpiamos la consola tras elegir la habilidad (por claridad de la interfaz)
                    os.system("clear")
                    # Mostramos los enemigos
                    print("- " * 20)
                    print("Lista de Enemigos:")
                    for enemy in vivos:
                        print(
                            f"  - {enemy.nombre} | HP: {enemy.vida_actual}/{enemy.vida_max}"
                        )
                    input("\nPulsa una tecla para volver al menú...")
                    continue

                else:
                    continue

                # Turno de los enemigos (estos solo atacan)
                # Revisamos si quedan enemigos vivos
                if any(e.esta_vivo for e in vivos):
                    print("\n--- Es el turno enemigo ---")
                    for e in vivos:
                        if e.esta_vivo and self.jugador.esta_vivo:
                            print(
                                f"\n⚔️ {e.nombre} ataca con {e.arma_equipada.nombre if e.arma_equipada else "sus puños"}!!"
                            )
                            print(
                                f"{self.jugador.nombre} recibió {self.jugador.recibir_daño(e.daño_total)} de daño. Vida restante: {self.jugador.vida_actual}/{self.jugador.vida_max}"
                            )
                    input("\nPulsa una tecla para volver al menú...")
                # Si se ha llegado hasta aquí es por que
                # ya se ha realizado todo correctamente
                # Por lo que lo cortamos para que revise
                # quien sigue vivo y quien no (que es el bucle principal)
                break

        # Si terminamos el bucle y el jugador sigue vivo hemos ganado
        if self.jugador.esta_vivo:
            print("\n🏆 ¡HAS GANADO LA BATALLA!")
            return True
        # Si no sigue vivo hemos perdido
        else:
            print("\n💀 Has sido derrotado...")
            return False
