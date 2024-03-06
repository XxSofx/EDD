class Carro:
    def __init__(self, velocidad_inicial=0):
        self.__velocidad = velocidad_inicial

    def acelerar(self, incremento):
        self.__velocidad += incremento
        print(f"El coche ha acelerado a {self.__velocidad} km/h.")

    def frenar(self, decremento):
        if self.__velocidad - decremento >= 0:
            self.__velocidad -= decremento
            print(f"El coche ha frenado a {self.__velocidad} km/h.")
        else:
            print("El coche ya está detenido.")

    def obtener_velocidad(self):
        return self.__velocidad


# Ejemplo de uso
velocidad_inicial = float(input("Ingrese la velocidad inicial del coche (km/h): "))
carro = Carro(velocidad_inicial)

opcion = 0
while opcion != 3:
    print("\n1. Acelerar")
    print("2. Frenar")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        incremento = float(input("Ingrese el incremento de velocidad (km/h): "))
        carro.acelerar(incremento)
    elif opcion == 2:
        decremento = float(input("Ingrese el decremento de velocidad (km/h): "))
        carro.frenar(decremento)
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
