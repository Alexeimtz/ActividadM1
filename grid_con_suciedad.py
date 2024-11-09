# Descripción: Simulación de limpieza de celdas en una cuadrícula con agentes.
# Autor:    Ian Alexei Martínez Armendáriz, Lorena Abigail Solís de los Santos - A01753288, A01746602
# Fecha de creación: 06/11/2024
# Última modificación: 07/11/2024

from mesa.space import MultiGrid

class MultiGridConSuciedad(MultiGrid):
    """
    Clase que extiende MultiGrid para incluir la capacidad de manejar celdas sucias en la cuadrícula.
    """

    def __init__(self, width, height, torus):
        """
        Inicializa una cuadrícula con capacidad para rastrear celdas sucias.

        Parámetros:
        - width (int): Ancho de la cuadrícula.
        - height (int): Alto de la cuadrícula.
        - torus (bool): Indica si la cuadrícula es un toroide (conexión de bordes).
        """
        super().__init__(width, height, torus)
        self.celdas_sucias = []  # Lista para rastrear las posiciones de las celdas sucias.

    def set_cell_dirty(self, pos):
        """
        Marca una celda en la posición dada como sucia.

        Parámetros:
        - pos (tuple): Coordenadas (x, y) de la celda a marcar como sucia.
        """
        pos = tuple(pos)
        if pos not in self.celdas_sucias:
            self.celdas_sucias.append(pos)

    def is_cell_dirty(self, pos):
        """
        Verifica si una celda en la posición dada está sucia.

        Parámetros:
        - pos (tuple): Coordenadas (x, y) de la celda a verificar.

        Retorno:
        - bool: True si la celda está sucia, False en caso contrario.
        """
        pos = tuple(pos)
        return pos in self.celdas_sucias

    def clean_cell(self, pos):
        """
        Limpia una celda en la posición dada si está marcada como sucia.

        Parámetros:
        - pos (tuple): Coordenadas (x, y) de la celda a limpiar.
        """
        pos = tuple(pos)
        if pos in self.celdas_sucias:
            self.celdas_sucias.remove(pos)