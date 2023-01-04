import pygame

class Cohete:
    """Gestiona la nave del jugador."""

    def __init__(self, juego_ia):
        """Inicializa la nave y establece su posición inicial."""
        self.pantalla = juego_ia.pantalla
        self.ajustes = juego_ia.ajustes
        self.pantalla_rect = juego_ia.pantalla.get_rect()

        # Carga la imagen de la nave y coge su rectángulo
        self.imagen = pygame.image.load('ch12/imagenes/ship.bmp')
        self.rect = self.imagen.get_rect()

        # Comienza cada nueva imagen en el centro de la parte 
        # inferior de la pantalla
        self.rect.midbottom = self.pantalla_rect.midbottom

        # Almacena un float para la posición exacta de la nave
        self.x = float(self.rect.x)

        # Flag de movimiento; la nave comienza sin moverse.
        self.moviendo_derecha = False
        self.moviendo_izquierda = False
    
    def actualiza_posicion(self):
        """Actualiza la posición de la nave en función de las
           flags de movimiento"""
        # Actualiza el valor de x de la nave, no del rectángulo
        if self.moviendo_derecha and self.rect.right < self.pantalla_rect.right:
            self.x += self.ajustes.velocidad_nave
        if self.moviendo_izquierda and self.rect.left > 0:
            self.x -= self.ajustes.velocidad_nave
        
        # Actualiza el objeto rect con el valor de self.x
        self.rect.x = self.x
    
    def centra_cohete(self):
        """Centra el cohete en la pantalla."""
        self.rect.midbottom = self.pantalla_rect.midbottom
        self.x = float(self.rect.x)
    
    def dibuja_nave(self):
        """Dibuja la nave en su posición actual."""
        self.pantalla.blit(self.imagen, self.rect)