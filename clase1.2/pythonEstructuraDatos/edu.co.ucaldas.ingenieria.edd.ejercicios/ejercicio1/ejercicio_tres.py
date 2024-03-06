#Buscar elemento maximo

def buscar_elemento_maximo(arreglo):
    maximo = arreglo[0]
    for num in arreglo:
        if num > maximo:
            maximo = num
    return maximo

arreglo = [89,45,34,68,90,29,17,120]
print("El maximo elemento del arreglo es:", buscar_elemento_maximo(arreglo))
