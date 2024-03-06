#Suma de elementos

def adicion_elementos(arreglo):
    suma = 0
    for num in arreglo:
        suma += num
    return suma

arreglo = [1,2,3,4,5]
print("La suma de los elementos del arreglo es:", adicion_elementos(arreglo))