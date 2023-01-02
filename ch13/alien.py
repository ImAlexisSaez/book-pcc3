import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Gestiona un alienígna de la flota enemiga."""

    def __init__(self, ia_juego):
        """Inicializa el alien y fija su posición de partida."""
        super().__init__()
        self.pantalla = ia_juego.pantalla
        self.ajustes = ia_juego.ajustes

        # Carga la imagen del alien y fija su atributo del rectángulo
        self.image = pygame.image.load('ch13/imagenes/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nuevo alien en la esquina superior izquierda
        # de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda la posición exacta horizontal del alienígena
        self.x = float(self.rect.x)
    
    def controla_bordes(self):
        """Devuelve True si el alien está en el borde de la pantalla."""
        pantalla_rect = self.pantalla.get_rect()
        return (self.rect.right >= pantalla_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Mueve el alien a la derecha"""
        self.x += self.ajustes.velocidad_alien * self.ajustes.sentido_flota
        self.rect.x = self.x