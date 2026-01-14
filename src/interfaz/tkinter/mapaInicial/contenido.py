from modelos.entidades.entidades import Orco, JefeOrco
import os


def obtener_historia(ruta_assets):
    """
    Retorna el diccionario de escenas.
    Recibe ruta_assets para construir las rutas de imagen correctamente.
    """
    return {
        "inicio_combate": {
            "texto": "Estás ante una cueva oscura. Un grupo de Goblins custodia la entrada.",
            "imagen": os.path.join(ruta_assets, "entrada_cueva.png"),
            "opciones": {
                "Atacar a los Goblins": "TRIGGER_COMBATE",  # ID especial
                "Huir": "inicio_cueva",
            },
            # Definimos aquí quiénes aparecen si se inicia un combate en esta escena
            "enemigos": [Orco(), Orco(), Orco()],
            "siguiente_escena": "dentro_cueva",
            "escena_retorno": "inicio_cueva",
        },
        "inicio_cueva": {
            "texto": "Estás ante una cueva que emana un aire gélido. El silencio es absoluto y la entrada parece una boca hambrienta.",
            "imagen": os.path.join(ruta_assets, "entrada_cueva.png"),
            "opciones": {
                "Entrar en la cueva": "dentro_cueva",
                "Buscar alrededor de la entrada": "buscar_antorcha",
                "Empezar combate": "inicio_combate",
            },
        },
        "dentro_cueva": {
            "texto": "La oscuridad te envuelve. El suelo está resbaladizo y escuchas gotas de agua cayendo en la lejanía.",
            "imagen": os.path.join(ruta_assets, "interior_cueva.png"),
            "opciones": {
                "Gritar para ver si hay alguien": "gritar",
                "Avanzar a tientas por la pared": "avanzar_pared",
                "Volver atrás": "inicio_cueva",
            },
        },
        "buscar_antorcha": {
            "texto": "Entre unos matorrales secos, brilla algo de madera. Es una vieja antorcha que parece tener algo de resina aún.",
            "imagen": os.path.join(ruta_assets, "antorcha.png"),
            "opciones": {
                "Recoger la antorcha y entrar": "dentro_cueva",
                "Dejarla y marcharte": "inicio_cueva",
            },
        },
    }
