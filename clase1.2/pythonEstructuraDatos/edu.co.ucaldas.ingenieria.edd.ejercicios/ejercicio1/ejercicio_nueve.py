#Ordenamiento rápido (Quicksort)

lista = [1,7, 9, 11, 13, 27, 22]

def ordenamiento_rapido(lista):
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range (1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores, pivote, mayores

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menores, pivote, mayores = ordenamiento_rapido(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)
print(quicksort(lista))