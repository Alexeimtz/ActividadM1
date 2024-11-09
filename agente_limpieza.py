# Descripción: Simulación de limpieza de celdas en una cuadrícula con agentes.
# Autor:    Ian Alexei Martínez Armendáriz, Lorena Abigail Solís de los Santos - A01753288, A01746602
# Fecha de creación: 06/11/2024
# Última modificación: 07/11/2024

from mesa import Agent
import random

class AgenteLimpieza(Agent):
    """
    Clase que representa a un agente de limpieza en la simulación.
    El agente se mueve aleatoriamente por la cuadrícula y limpia las celdas sucias.
    """

    def __init__(self, unique_id, model):
        """
        Inicializa un agente de limpieza.

        Parámetros:
        - unique_id (int): Identificador único del agente.
        - model (Model): Referencia al modelo al que pertenece el agente.
        """
        super().__init__(unique_id, model)
        self.movimientos = 0  # Contador de movimientos realizados por el agente.

    def step(self):
        """
        Realiza un paso en la simulación:
        - Limpia la celda actual si está sucia.
        - Se mueve a una celda adyacente aleatoria.
        """
        # Limpiar la celda actual si está sucia
        if self.model.grid.is_cell_dirty(self.pos):
            self.model.grid.clean_cell(self.pos)
            # Imprimir para depuración cuando se limpia una celda
            print(f"Agente {self.unique_id} limpió la celda en {self.pos}")

        # Obtener las posiciones adyacentes para moverse
        posibles_movimientos = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )

        # Elegir una nueva posición aleatoria y moverse a ella
        nueva_posicion = self.random.choice(posibles_movimientos)
        self.model.grid.move_agent(self, nueva_posicion)
        self.movimientos += 1  # Incrementar el contador de movimientos
