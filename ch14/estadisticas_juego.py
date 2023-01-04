class EstadisticasJuego:
    """Realiza seguimiento de estadísticas para Invasión Alienígena."""

    def __init__(self, ia_juego):
        """Inicializa estadísticas."""
        self.ajustes = ia_juego.ajustes
        self.resetea_estadisticas()
    
    def resetea_estadisticas(self):
        """Inicializa estadísticas que cambian durante una partida."""
        self.naves_disponibles = self.ajustes.limite_naves