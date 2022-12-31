import sys

import pygame

from ajustes import Ajustes
from cohete import Cohete

class InvasionAlien:
    """Clase que gestiona los activos del juego y su comportamiento."""

    def __init__(self):
        """Inicializa el juego y crea sus recursos."""
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.ajustes = Ajustes()

        self.pantalla = pygame.display.set_mode(
            (self.ajustes.pantalla_ancho, self.ajustes.pantalla_largo))
        pygame.display.set_caption("¡Invasión de alienígenas!")

        self.cohete = Cohete(self)

    def ejecuta_juego(self):
        """Inicia el bucle principal para el juego."""
        while True:
            self._controla_eventos()            
            self._actualiza_pantalla()
            self.reloj.tick(60)
    
    def _controla_eventos(self):
        """Responde a eventos de teclado y ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Mueve la nave hacia la derecha.
                    self.cohete.rect.x += 1

    
    def _actualiza_pantalla(self):
        """Actualiza las imágenes en la pantalla y las dibuja (flip)."""
        self.pantalla.fill(self.ajustes.color_fondo)
        self.cohete.dibuja_nave()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ia = InvasionAlien()
    ia.ejecuta_juego()
