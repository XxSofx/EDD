#Contar ocurrecias

def contar_ocurrencias(arreglo, mapa):
    for i in arreglo:
        if i in mapa:
            mapa[i] = mapa[i] + 1
        else:
            mapa [i] = 1

arreglo = [3,4,5,6,7,4,4,5]
mapa = {}

contar_ocurrencias(arreglo, mapa)
print(mapa)