#Invertir Arreglo

def invertir_arreglo(arreglo):
    size = len(arreglo)
    index = 0
    for i in reversed(arreglo):
        arreglo.append(i)
        index += 1
    del arreglo[0:size]

arreglo = [1,2,3,4,5,6,7,8,9,11]
invertir_arreglo(arreglo)
print(arreglo)
