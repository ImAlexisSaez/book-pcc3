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
        # self.velocidad_bala = 2.5
        self.velocidad_bala = 10.0
        # self.anchura_bala = 3
        self.anchura_bala = 3000
        self.altura_bala = 15
        self.color_bala = (60, 60, 60)
        # self.balas_permitidas = 3
        self.balas_permitidas = 10

        # Ajustes de los alienígenas
        # self.velocidad_alien = 1.5
        self.velocidad_alien = 50
        self.velocidad_caida_flota = 10
        # Sentido flota: 1, derecha; -1, izquierda.
        self.sentido_flota = 1
