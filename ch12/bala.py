import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Clase que gestiona las balas disparadas por el cohete."""

    def __init__(self, ia_juego):
        """Crea una bala en la posición actual del cohete."""
        super().__init__()
        self.pantalla = ia_juego.pantalla
        self.ajustes = ia_juego.ajustes
        self.color = self.ajustes.color_bala

        # Crea un rectángulo en (0,0) y luego ajuste la posición
        self.rect = pygame.rect(
            0, 0, self.ajustes.anchura_bala, self.ajustes.altura_bala
        )
        self.rect.midtop = ia_juego.cohete.rect.midtop

        # Almacena la posición como float
        self.y = float(self.rect.y)
