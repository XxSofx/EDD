# Eliminar duplicados

def eliminar_elementos(arreglo):
    elementos = set()
    resultado = []

    for elemento in arreglo:
        if elemento not in elementos:
            elementos.add(elemento)
            resultado.append(elemento)

    return resultado

arreglo = [1,2,3,4,5,6,7,8,5,7, 89, 58, 76, 89]
resultado = eliminar_elementos(arreglo)
print("Arreglo original:" , arreglo)
print("Arreglo sin duplicados" , resultado)