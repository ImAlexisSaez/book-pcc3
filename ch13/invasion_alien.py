import sys

import pygame

from ajustes import Ajustes
from cohete import Cohete
from bala import Bala
from alien import Alien

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
        self.balas = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._crea_flota()

    def ejecuta_juego(self):
        """Inicia el bucle principal para el juego."""
        while True:
            self._controla_eventos()  
            self.cohete.actualiza_posicion() 
            self._actualiza_balas()
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
        elif event.key == pygame.K_SPACE:
            self._dispara_bala()
        elif event.key == pygame.K_q:
            sys.exit()

    def _controla_eventos_KEYUP(self, event):
        """Responde a dejar de pulsar una tecla."""
        if event.key == pygame.K_RIGHT:
            self.cohete.moviendo_derecha = False
        elif event.key == pygame.K_LEFT:
            self.cohete.moviendo_izquierda = False
    
    def _dispara_bala(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.balas) < self.ajustes.balas_permitidas:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)
    
    def _actualiza_balas(self):
        """Actualiza posición de balas y elimina las que se salen."""
        # Actualiza la posición de las balas.
        self.balas.update()

        # Elimina las balas que desaparecen de la pantalla.
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)
    
    def _crea_flota(self):
        """Crea la flota de alienígenas."""
        # Crea un alien y continua añadiendo hasta que no quede hueco.
        # Espacio entre aliens: la anchura y la altura de uno de ellos.
        alien = Alien(self)
        alien_anchura, alien_altura = alien.rect.size
        
        x_actual, y_actual = alien_anchura, alien_altura
        while y_actual < (self.ajustes.pantalla_largo - 9 * alien_altura):
            while x_actual < (self.ajustes.pantalla_ancho - 2 * alien_anchura):
                self._crea_alien(x_actual, y_actual)
                x_actual += 2 * alien_anchura
            
            # Finalizada una fila, resetea x e incrementa y
            x_actual = alien_anchura
            y_actual += 2 * alien_altura
    
    def _crea_alien(self, posicion_x, posicion_y):
        """Crea un alien y lo coloca en la flota."""
        nuevo_alien = Alien(self)
        nuevo_alien.x = posicion_x
        nuevo_alien.rect.x = posicion_x
        nuevo_alien.rect.y = posicion_y
        self.aliens.add(nuevo_alien)
            
    def _actualiza_pantalla(self):
        """Actualiza las imágenes en la pantalla y las dibuja (flip)."""
        self.pantalla.fill(self.ajustes.color_fondo)
        for bala in self.balas.sprites():
            bala.dibuja_bala()
        self.cohete.dibuja_nave()
        self.aliens.draw(self.pantalla)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    ia = InvasionAlien()
    ia.ejecuta_juego()