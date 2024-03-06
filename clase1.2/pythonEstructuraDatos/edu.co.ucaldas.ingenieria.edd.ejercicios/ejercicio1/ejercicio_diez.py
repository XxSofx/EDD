#Buscar subcadena

def buscar_subcadena(cadena, subcadena):
    posicion = cadena.find(subcadena)
    print("La cadena '{}' se encuentra en la posición {}." .format(subcadena,posicion))

cadena = input("Ingresa una cadena:")
subcadena = input("Ingresa una subcadena:")
buscar_subcadena(cadena, subcadena)