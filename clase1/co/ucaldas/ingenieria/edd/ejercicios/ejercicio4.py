lista1 = ["Banano", "Banano", "Piña"]
lista2 = ["Melón", "Uva", "Manzana"]
def elemento_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

print(elemento_comun(lista1, lista2))