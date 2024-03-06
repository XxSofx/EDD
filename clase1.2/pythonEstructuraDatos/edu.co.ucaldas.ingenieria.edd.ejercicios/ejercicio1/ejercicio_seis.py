# Buscar elemento en un arreglo

def buscar_elemento(arreglo, elemento):
    for num in arreglo:
        if num == elemento:
            return True
    return False

arreglo = [1, 100, 50, 7, 4, 27]
elemento_seleccionado = 4

if buscar_elemento(arreglo, elemento_seleccionado):
    print(f"El elemento {elemento_seleccionado} esta presente en el arreglo")

else:
    print(f"El elemento {elemento_seleccionado} no esta presente en el arreglo")