import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Gestiona un alienígna de la flota enemiga."""

    def __init__(self, ia_juego):
        """Inicializa el alien y fija su posición de partida."""
        super().__init__()
        self.pantalla = ia_juego.pantalla

        # Carga la imagen del alien y fija su atributo del rectángulo
        self.imagen = pygame.image.load('ch13/imagenes/alien.bmp')
        self.rect = self.imagen.get_rect()

        # Inicia cada nuevo alien en la esquina superior izquierda
        # de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda la posición exacta horizontal del alienígena
        self.x = float(self.rect.x)