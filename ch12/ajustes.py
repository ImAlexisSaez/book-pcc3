class Ajustes:
    """Recoge los ajustes del juego ¡Invasión alienígena!"""

    def __init__(self):
        """Inicializa los ajustes del juego."""
        self.pantalla_ancho = 1200
        self.pantalla_largo = 800
        self.color_fondo = (230, 230, 230)

        # Ajustes de la nave
        self.velocidad_nave = 1.5

        # Ajustes de las balas
        self.velocidad_bala = 2.0
        self.anchura_bala = 3
        self.altura_bala = 15
        self.color_bala = (60, 60, 60)
        self.balas_permitidas = 3
