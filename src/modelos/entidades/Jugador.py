from .Entidad import Entidad
from modelos.items.items import Arma, Armadura


class Jugador(Entidad):
    # Constructor del jugador
    def __init__(self, nombre, vida, fuerza, defensa, clase):
        super().__init__(nombre, vida, fuerza, defensa)
        # Clase del jugador
        self.clase = clase
        # Aquí guardaremos los objetos como Pocion
        self.inventario = []

    # Método para definir y ejecutar las acciones del personaje en combate
    def seleccionar_accion(self, enemigos):
        # Bucle que se repite constantemente
        # hasta que entra en la opción 1 o 2 que tiene return
        while True:
            # Menú de selección
            print(
                f"\n--- Turno de {self.nombre} (HP: {self.vida_actual}/{self.vida_max}) ---"
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
                    for i, e in enumerate(enemigos):
                        print(f"{i}: {e.nombre} ({e.vida_actual} HP)")
                    # Controlamos los errores, para que en caso de que
                    # se indique cualquier valor que no esté contemplado
                    # no se haga nada y se repita el bucle
                    try:
                        target = int(input("¿A quién atacas?: "))
                        # Devolvemos la opción correspondiente y el enemigo que se ha seleccionado
                        return ("atacar", enemigos[target])
                    except:
                        pass

            # Opcion 2 - Inventario
            # Menu para la selección de items
            elif opcion == "2":
                # Si no hay items en el inventario, lanzamos ataque por defecto
                if not self.inventario:
                    print("¡El inventario está vacío! Atacas por defecto.")
                    return ("atacar", enemigos[0])

                # Si hay items, lanzamos menú para seleccionar 1
                # Como en los anteriores menus, lanzamos bucle infinito
                # del que se sale solo si se llega a un return
                while True:
                    # Enumeramos los items
                    for i, item in enumerate(self.inventario):
                        print(f"{i}: {item.nombre} - {item.descripcion}")
                    # Controlamos errores para que no se haga nada si la opción
                    # introducida no es válida, y se vuelva a cargar el menú
                    try:
                        item_idx = int(input("Elige un objeto (o -1 para volver): "))
                        # Si la opción es -1 volvemos a lanzar el menú principal sin hacer nada
                        if item_idx == -1:
                            return self.seleccionar_accion(enemigos)
                        # Si no da error (como por ejemplo que el número exceda el indice)
                        # devolvemos la opción "objeto" y el item del inventario,
                        # que sacamos del mismo con pop
                        return ("objeto", self.inventario.pop(item_idx))
                    except:
                        pass

            # Opción para mostrar las estadisticas del personaje
            elif opcion == "3":
                # Mostramos las estadisticas
                print("- " * 20)
                print("Estadisticas del personaje")
                print("- " * 20)
                print(f"Nombre: {self.nombre}")
                print(f"Clase: {self.clase}")
                print(f"Vida actual: {self.vida_actual}/{self.vida_max}")
                print(f"Fuerza: {self.fuerza}")
                print(f"Defensa: {self.defensa}")
                print("Equipo:")
                print(
                    f" - Arma: {self.arma_equipada.nombre} | Daño: 1d{self.arma_equipada.bonificador_fuerza}"
                )
                print(
                    f" - Armadura: {self.armadura_equipada.nombre} | Defensa: {self.armadura_equipada.bonificador_defensa}"
                )
                print("Objetos utilizables:")
                for obj in self.inventario:
                    print(f" - {obj.nombre}")
                input("Pulsa una tecla para volver al menú...")
                # Volvemos al menú de selección
                return self.seleccionar_accion(enemigos)

    # Método para equipar armas y armaduras
    def equipar(self, item):
        if isinstance(item, Arma):
            self.arma_equipada = item
        if isinstance(item, Armadura):
            self.armadura_equipada = item
