import sys

import pygame

class InvasionAlien:
    """Clase que gestiona los activos del juego y su comportamiento."""

    def __init__(self):
        """Inicializa el juego y crea sus recursos."""
        pygame.init()
        self.reloj = pygame.time.Clock()

        self.pantalla = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("¡Invasión de alienígenas!")

    def ejecuta_juego(self):
        """Inicia el bucle principal para el juego."""
        while True:
            # Vigila eventos del teclado y del ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Hace visible la última pantalla dibujada
            pygame.display.flip()
            self.reloj.tick(60)

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ia = InvasionAlien()
    ia.ejecuta_juego()
