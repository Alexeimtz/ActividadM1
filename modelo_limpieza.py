# Descripción: Simulación de limpieza de celdas en una cuadrícula con agentes.
# Autor:    Ian Alexei Martínez Armendáriz, Lorena Abigail Solís de los Santos - A01753288, A01746602
# Fecha de creación: 06/11/2024
# Última modificación: 07/11/2024

from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from grid_con_suciedad import MultiGridConSuciedad
from agente_limpieza import AgenteLimpieza

class ModeloLimpieza(Model):
    """
    Clase que representa el modelo de la simulación de limpieza en una cuadrícula.
    """

    def __init__(self, width, height, num_agentes, porc_suciedad):
        """
        Inicializa la simulación con una cuadrícula, agentes y celdas sucias.
        
        Parámetros:
        - width (int): Ancho de la cuadrícula.
        - height (int): Alto de la cuadrícula.
        - num_agentes (int): Número de agentes en la simulación.
        - porc_suciedad (float): Porcentaje de celdas que estarán sucias al inicio.
        """
        super().__init__()  # Inicializa la clase base Model
        self.num_agents = num_agentes
        self.grid = MultiGridConSuciedad(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.porc_suciedad = porc_suciedad
        self.movimientos_totales = 0

        # Crear y colocar agentes en la cuadrícula.
        for i in range(self.num_agents):
            agente = AgenteLimpieza(i, self)
            self.schedule.add(agente)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agente, (x, y))

        # Inicializar celdas sucias de forma aleatoria.
        for cell in self.grid.coord_iter():
            (x, y) = cell[1]  # Extrae las coordenadas (x, y)
            if self.random.random() < self.porc_suciedad:
                self.grid.set_cell_dirty((x, y))

        # Inicializar DataCollector para recopilar estadísticas de la simulación.
        self.datacollector = DataCollector(
            model_reporters={"Porcentaje Limpio": self.calcular_porcentaje_limpio},
            agent_reporters={"Movimientos": "movimientos"}
        )

    def step(self):
        """
        Ejecuta un paso de la simulación, actualizando el estado de los agentes y recopilando datos.
        """
        self.datacollector.collect(self)
        self.schedule.step()
        self.movimientos_totales += sum(agent.movimientos for agent in self.schedule.agents)

    def calcular_porcentaje_limpio(self):
        """
        Calcula el porcentaje de celdas que están limpias en la cuadrícula.

        Retorno:
        - float: Porcentaje de celdas limpias.
        """
        total_celdas = self.grid.width * self.grid.height
        celdas_limpias = total_celdas - len(self.grid.celdas_sucias)
        porcentaje_celdas_limpias = (celdas_limpias / total_celdas) * 100
        return porcentaje_celdas_limpias
