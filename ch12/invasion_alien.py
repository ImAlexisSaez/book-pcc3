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
            (0, 0), pygame.FULLSCREEN)
        self.ajustes.pantalla_ancho = self.pantalla.get_rect().width
        self.ajustes.pantalla_largo = self.pantalla.get_rect().height
        pygame.display.set_caption("¡Invasión de alienígenas!")

        self.cohete = Cohete(self)

    def ejecuta_juego(self):
        """Inicia el bucle principal para el juego."""
        while True:
            self._controla_eventos()  
            self.cohete.actualiza_posicion()          
            self._actualiza_pantalla()
            self.reloj.tick(60)
    
    def _controla_eventos(self):
        """Responde a eventos de teclado y ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._controla_eventos_KEYDOWN(event)
            elif event.type == pygame.KEYUP:
                self._controla_eventos_KEYUP(event)                
        
    def _controla_eventos_KEYDOWN(self, event):
        """Responde a pulsar una tecla."""
        if event.key == pygame.K_RIGHT:
            self.cohete.moviendo_derecha = True
        elif event.key == pygame.K_LEFT:
            self.cohete.moviendo_izquierda = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _controla_eventos_KEYUP(self, event):
        """Responde a dejar de pulsar una tecla."""
        if event.key == pygame.K_RIGHT:
            self.cohete.moviendo_derecha = False
        elif event.key == pygame.K_LEFT:
            self.cohete.moviendo_izquierda = False
    
    def _actualiza_pantalla(self):
        """Actualiza las imágenes en la pantalla y las dibuja (flip)."""
        self.pantalla.fill(self.ajustes.color_fondo)
        self.cohete.dibuja_nave()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ia = InvasionAlien()
    ia.ejecuta_juego()