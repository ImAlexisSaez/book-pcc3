class Caja:
    """Modelo de una caja donde almacenar pertenencias."""

    def __init__(self, dimensiones, color, material, objetos=[]):
        """Inicializa atributos de la caja."""
        self.dimensiones = dimensiones
        self.color = color
        self.material = material
        self.objetos = objetos
    
    def insertar_pertenencia(self, pertenencia):
        """Inserta pertenencias en la caja."""
        print(f"Se introduce en la caja: {pertenencia}.")
        self.objetos.append(pertenencia)
    
    def extraer_pertenencia(self, pertenencia):
        """Extrae pertenencias de la caja."""
        if not self.objetos:
            print("La caja está vacía. No se puede extraer nada.")
        elif pertenencia not in self.objetos:
            print(f"En la caja no hay: {pertenencia}.")
        else:
            print(f"Se extrae de la caja: {pertenencia}.")
            self.objetos.remove(pertenencia)
    
    def listar_pertenencias(self):
        """Lista las pertenencias de la caja."""
        if not self.objetos:
            print("La caja está vacía.")
        else:
            print("Contenidos de la caja:")
            for objeto in self.objetos:
                print(f"\t-{objeto}")
    
    def describir_caja(self):
        """Describe físicamente la caja."""
        print(
            f"La caja tiene unas dimensiones de",
            f"{self.dimensiones[0]} x {self.dimensiones[1]} x {self.dimensiones[2]},",
            f"es de color {self.color} y está hecha de {self.material}.")

caja_libros = Caja((100,200,50), 'rojo', 'plástico')
caja_libros.describir_caja()
caja_libros.extraer_pertenencia('Libro de matemáticas')
caja_libros.insertar_pertenencia('Libro de matemáticas')
caja_libros.insertar_pertenencia('Libro de inglés')
caja_libros.extraer_pertenencia('Libro de francés')
caja_libros.extraer_pertenencia('Libro de inglés')
caja_libros.listar_pertenencias()

caja_pegatinas = Caja(
    (200,200,100), 'blanco', 'madera',
    objetos=['Pegatinas de gatos', 'Pegatinas de perros'])
caja_pegatinas.listar_pertenencias()

