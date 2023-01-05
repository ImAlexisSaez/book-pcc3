import pygame.font

class Boton:
    """Clase para construir botones en el juego."""

    def __init__(self, ia_juego, sms):
        """Inicializa los atributos del botón."""
        self.pantalla = ia_juego.pantalla
        self.pantalla_rect = self.pantalla.get_rect()

        # Fija dimensiones y propiedades del botón
        self.ancho, self.alto = 200, 50
        self.color_boton = (0, 135, 9)
        self.color_texto = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Construye el rectángulo del botón y lo centra.
        self.rect = pygame.Rect(0, 0, self.ancho, self.alto)
        self.rect.center = self.pantalla_rect.center

        # El mensaje necesita ser preparado solo una vez.
        self._prep_sms(sms)
    
    def _prep_sms(self, sms):
        """Convierte el mensaje en una imagen y la centra en el botón."""
        self.sms_imagen = self.font.render(
            sms, True, self.color_texto, self.color_boton
        )
        self.sms_imagen_rect = self.sms_imagen.get_rect()
        self.sms_imagen_rect.center = self.rect.center
    
    def dibuja_boton(self):
        """Dibuja el botón y después del texto."""
        self.pantalla.fill(self.color_boton, self.rect)
        self.pantalla.blit(self.sms_imagen, self.sms_imagen_rect)