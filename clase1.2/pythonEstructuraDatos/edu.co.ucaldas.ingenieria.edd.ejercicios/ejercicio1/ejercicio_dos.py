#Ordenamiento de Burbuja

def ordenar_burbuja(vector):
    for elemento in vector:
        print(elemento, end = "")
    print()

vector = [89,45,34,68,90,29,17]
tamanio = len(vector)
print("Vector original: ")
ordenar_burbuja(vector)

print ("\n Ordenamiento burbuja: \n")
for i in range (tamanio - 1 ):
    for j in range(tamanio - 1 - i ):
        if vector [j + 1 ] < vector [j]:
            aux = vector[j]
            vector[j] = vector [j + 1]
            vector[j + 1] = aux
ordenar_burbuja(vector)
