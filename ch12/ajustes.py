class Ajustes:
    """Recoge los ajustes del juego ¡Invasión alienígena!"""

    def __init__(self):
        """Inicializa los ajustes del juego."""
        self.pantalla_ancho = 1200
        self.pantalla_largo = 800
        self.color_fondo = (230, 230, 230)

        # Ajustes de la nave
        self.velocidad_nave = 1.5