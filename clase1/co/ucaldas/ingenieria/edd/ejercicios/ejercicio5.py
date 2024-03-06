# Multiplicar matrices
import numpy as np
from queue import Queue

matriz1 = [[]]
matriz2 = [[]]
cola = Queue()
llenado = True


def llenarMatriz(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"¿Que número quieres poner para la posición {i} - {j}:"))

for i in range(2):
    filas = int(input("Cuantas filas quieres tener para tu primera matriz: "))
    columnas = int(input("Cuantas columnas quieres tener para tu primera matriz:"))
    if(llenado):
        matriz1 = np.zeros((filas, columnas))
        llenarMatriz(matriz1, filas, columnas)
        cola.put(columnas)
        llenado = False

    else:
        matriz2 = np.zeros((filas, columnas))
        llenarMatriz(matriz2, filas, columnas)
        cola.put(filas)

# Llenado de matrices

if (cola.get() != cola.get()):
    print("null")
else:
    print(f"Matriz resultante: {np.dot(matriz1, matriz2)}")