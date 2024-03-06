#Ordenamiento de numeros enteros de menor a mayor

def ordenar_menor_mayor (arreglo):
    for i in range(len(arreglo) - 1):
        menor = i

        for j in range(i + 1, len(arreglo)):
            if arreglo [j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

ordenar_menor  = [100, 21, 24, 28, 34, 250, 1]
ordenar_menor_mayor(ordenar_menor)

print(ordenar_menor)