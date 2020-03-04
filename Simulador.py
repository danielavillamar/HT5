# DANIELA VILLAMAR
# HT5 DATOS 
# 4 DE MARZO DEL 2020

# LAS VARIABLES ESTAN MAS ABAJO PARA QUE LAS PUEDAN EDITAR!!!

import simpy
import random
import statistics

# Simulador del sistema operativo que une al CPU, RAM, Procesos y Simulador

def OperatingSystem(env,simulationTime,processName,simulationMemory,simulationInstructions,instructionsForTimeUnit):

    #Etapa New
    yield env.timeout(simulationTime)
    print("El %s utilizara %s de la memoria RAM"%(processName,simulationMemory))
    entranceTime = env.now
    
    #Etapa ready
    #Obtiene la memoria de la RAM de lo contrario si no hay memoria suficiente va a WAIT

    while(RAMMemory.level<simulationMemory):
        with WAIT.request() as request:
                        yield request
                        yield env.timeout(1) 
      
    yield RAMMemory.get(simulationMemory)
    print("\tSe ha obtenido la memoria %s en tiempo %s" %(simulationMemory,env.now))
    while (simulationInstructions > 0) :
    

        simulationInstructions = simulationInstructions - INSTRUCTIONS
        yield env.timeout(1)
        
        #Etapa Waiting
        decision = random.randint(1,2)
        if decision == 2:
            with WAIT.request() as request:
                        yield request
                        yield env.timeout(1)      
        #Etapa Terminated
        yield RAMMemory.put(simulationMemory)
        print("\tSe ha regresado la memoria %s a la RAM en tiempo %s" %(simulationMemory,env.now))
        #Tiempo del proceso total
        ProcessTime= (env.now-entranceTime)
        #Se guarda el tiempo tardado del proceso para analisis de datos
        global TOTALTIME
        global TIMES
        TOTALTIME = TOTALTIME + ProcessTime
        TIMES.append(ProcessTime)

# Variables a modificar
CAPACITY = 1 #Capacidad de CPU
INSTRUCTIONS = 3  # Instruccciones que puede ejecutar el CPU por unidad de tiempo
MEMORY = 100  # Memoria RAM
PROCESS = 25  # Cantidad de procesos
INTERVAL = 10  # Intervalo de creacion de procesos
TOTALTIME = 0 # Tiempo total de ejecucion
TIMES = [] #Todos los tiempos
SEED = 8 #Semilla para random
random.seed(SEED)

#Creación ambiente,CPU modelado como resource, RAMMemory modelado como Container y  el Wait

env = simpy.Environment()
CPU = simpy.Resource(env, capacity= CAPACITY)
RAMMemory = simpy.Container(env,init=MEMORY,capacity=MEMORY)
WAIT = simpy.Resource(env, capacity= CAPACITY)
    
# Main en la simulación

def main():

    for i in range(PROCESS):
        simulationTime = random.expovariate(1.0/INTERVAL)
        simulationInstructions = random.randint(1,10)
        simulationMemory = random.randint(1,10)
        env.process(OperatingSystem(env,simulationTime,"Proceso %s" %i,simulationMemory,simulationInstructions,INSTRUCTIONS))
    env.run()
    
    MeanTime = float(TOTALTIME/PROCESS)
    StdevTime = statistics.stdev(TIMES)

    print("Procesos Terminados")
    print("El tiempo total para %s procesos fue de %.2f, el tiempo por proceso promedio fue de %.2f con desviacion estandar de %.2f" %(PROCESS, TOTALTIME,MeanTime ,StdevTime))
    
main()
