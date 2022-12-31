import pygame

class Cohete:
    """Gestiona la nave del jugador."""

    def __init__(self, juego_ia):
        """Inicializa la nave y establece su posición inicial."""
        self.pantalla = juego_ia.pantalla
        self.pantalla_rect = juego_ia.pantalla.get_rect()

        # Carga la imagen de la nave y coge su rectángulo
        self.imagen = pygame.image.load('ch12/imagenes/ship.bmp')
        self.rect = self.imagen.get_rect()

        # Comienza cada nueva imagen en el centro de la parte 
        # inferior de la pantalla
        self.rect.midbottom = self.pantalla_rect.midbottom

        # Flag de movimiento; la nave comienza sin moverse.
        self.moviendo_derecha = False
        self.moviendo_izquierda = False
    
    def actualiza_posicion(self):
        """Actualiza la posición de la nave en función de las
           flags de movimiento"""
        if self.moviendo_derecha:
            self.rect.x += 1
        if self.moviendo_izquierda:
            self.rect.x -= 1
    
    def dibuja_nave(self):
        """Dibuja la nave en su posición actual."""
        self.pantalla.blit(self.imagen, self.rect)