# Descripción: Simulación de limpieza de celdas en una cuadrícula con agentes.
# Autor:    Ian Alexei Martínez Armendáriz, Lorena Abigail Solís de los Santos - A01753288, A01746602
# Fecha de creación: 06/11/2024
# Última modificación: 07/11/2024

import time
import os
from modelo_limpieza import ModeloLimpieza

# Parámetros de la simulación
width = 10           # Ancho de la cuadrícula
height = 10          # Alto de la cuadrícula
num_agentes = 2      # Número de agentes
porc_suciedad = 0.2  # Porcentaje de celdas inicialmente sucias
tiempo_maximo = 15   # Tiempo máximo de ejecución en segundos
tiempo_paso = 0.3    # Tiempo de espera entre cada paso (en segundos)

# Crear y ejecutar el modelo
modelo = ModeloLimpieza(width, height, num_agentes, porc_suciedad)

def imprimir_cuadricula(modelo):
    """
    Imprime la cuadrícula en la consola mostrando celdas sucias, limpias y posiciones de los agentes.

    Parámetros:
    - modelo (ModeloLimpieza): El modelo de la simulación que contiene la cuadrícula y los agentes.
    """
    # Crear una representación de la cuadrícula
    cuadricula = [['S' if (x, y) in modelo.grid.celdas_sucias else '-' for y in range(modelo.grid.height)] for x in range(modelo.grid.width)]
    
    # Colocar los agentes en la representación de la cuadrícula
    for agente in modelo.schedule.agents:
        x, y = agente.pos
        cuadricula[x][y] = 'A'

    # Limpiar la consola y mostrar la cuadrícula
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in cuadricula:
        print(' '.join(fila))
    print()

# Ejecutar la simulación con un tiempo máximo
inicio_simulacion = time.time()
tiempo_transcurrido = 0
celdas_limpias_al_final = False

while tiempo_transcurrido < tiempo_maximo:
    imprimir_cuadricula(modelo)  # Mostrar el estado de la cuadrícula
    modelo.step()                # Realizar un paso en la simulación
    tiempo_transcurrido = time.time() - inicio_simulacion

    # Verificar si todas las celdas están limpias
    if not modelo.grid.celdas_sucias:
        celdas_limpias_al_final = True
        break

    # Pausar la simulación para ralentizarla
    time.sleep(tiempo_paso)

# Calcular los resultados finales
porcentaje_celdas_limpias = modelo.calcular_porcentaje_limpio()
movimientos_realizados = sum(agent.movimientos for agent in modelo.schedule.agents)

# Mostrar los resultados finales
print("Simulación completada.")
print(f"Tiempo necesario hasta que todas las celdas estén limpias (o se haya llegado al tiempo máximo): {tiempo_transcurrido:.2f} segundos")
print(f"Porcentaje de celdas limpias después del término de la simulación: {porcentaje_celdas_limpias:.2f}%")
print(f"Número de movimientos realizados por todos los agentes: {movimientos_realizados}")