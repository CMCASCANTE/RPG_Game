class AccionesCombate:

    # Método de clase para definir y ejecutar las acciones del personaje en combate
    def seleccionar_accion(jugador, enemigos):
        # Bucle que se repite constantemente
        # hasta que entra en la opción 1 o 2 que tiene return
        while True:
            # Menú de selección
            print(
                f"\n--- Turno de {jugador.nombre} (HP: {jugador.vida_actual}/{jugador.vida_max}) ---"
            )
            print("1. Atacar")
            print("2. Abrir Inventario")
            print("3. Ver atributos del personaje")

            opcion = input("Elige una acción: ")

            # Opción 1 - Ataque
            # menu para seleccionar el objetivo a atacar
            if opcion == "1":
                # Lanzamos un bucle infinito igual que en el menú anterior
                # del que se saldrá al devolver un return
                while True:
                    # Enumeramos por pantalla los enemigos
                    # Comenzamos a contar desde el 1 para que mejor visualmente
                    for i, e in enumerate(enemigos, start=1):
                        print(f"{i}: {e.nombre} ({e.vida_actual} HP)")
                    # Controlamos los errores, para que en caso de que
                    # se indique cualquier valor que no esté contemplado
                    # no se haga nada y se repita el bucle
                    try:
                        target = int(input("¿A quién atacas?: "))
                        # Devolvemos la opción correspondiente y el enemigo que se ha seleccionado
                        # Restamos 1 ya que desde el enumerate hemos empezado por 1 en vez de 0
                        # para que sea mas eficiente visualmente
                        return ("atacar", enemigos[target - 1])
                    except:
                        pass

            # Opcion 2 - Inventario
            # Menu para la selección de items
            elif opcion == "2":
                # Si no hay items en el inventario, lanzamos ataque por defecto
                if not jugador.inventario:
                    print("¡El inventario está vacío! Atacas por defecto.")
                    return ("atacar", enemigos[0])

                # Si hay items, lanzamos menú para seleccionar 1
                # Como en los anteriores menus, lanzamos bucle infinito
                # del que se sale solo si se llega a un return
                while True:
                    # Enumeramos los items
                    for i, item in enumerate(jugador.inventario):
                        print(f"{i}: {item.nombre} - {item.descripcion}")
                    # Controlamos errores para que no se haga nada si la opción
                    # introducida no es válida, y se vuelva a cargar el menú
                    try:
                        item_idx = int(input("Elige un objeto (o -1 para volver): "))
                        # Si la opción es -1 volvemos a lanzar el menú principal sin hacer nada
                        if item_idx == -1:
                            return AccionesCombate.seleccionar_accion(jugador, enemigos)
                        # Si no da error (como por ejemplo que el número exceda el indice)
                        # devolvemos la opción "objeto" y el item del inventario,
                        # que sacamos del mismo con pop
                        return ("objeto", jugador.inventario.pop(item_idx))
                    except:
                        pass

            # Opción para mostrar las estadisticas del personaje
            elif opcion == "3":
                # Mostramos las estadisticas
                print("- " * 20)
                print("Estadisticas del personaje")
                print("- " * 20)
                print(f"Nombre: {jugador.nombre}")
                print(f"Clase: {jugador.clase}")
                print(f"Vida actual: {jugador.vida_actual}/{jugador.vida_max}")
                print(f"Fuerza: {jugador.fuerza}")
                print(f"Defensa: {jugador.defensa}")
                print("Equipo:")
                print(
                    f" - Arma: {jugador.arma_equipada.nombre} | Daño: 1d{jugador.arma_equipada.bonificador_fuerza}"
                )
                print(
                    f" - Armadura: {jugador.armadura_equipada.nombre} | Defensa: {jugador.armadura_equipada.bonificador_defensa}"
                )
                print("Objetos utilizables:")
                for obj in jugador.inventario:
                    print(f" - {obj.nombre}")
                input("Pulsa una tecla para volver al menú...")
                # Volvemos al menú de selección
                return AccionesCombate.seleccionar_accion(jugador, enemigos)
