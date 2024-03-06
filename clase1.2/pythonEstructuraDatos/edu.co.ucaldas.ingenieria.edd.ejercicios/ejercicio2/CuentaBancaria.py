class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f'Se han depositado {cantidad} unidades.')

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f'Se han retirado {cantidad} unidades.')
        else:
            print('Fondos insuficientes.')

    def consultar_saldo(self):
        print(f'Saldo actual: {self.__saldo}')


# Ejemplo de uso
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
cuenta = CuentaBancaria(saldo_inicial)

opcion = 0
while opcion != 4:
    print("\n1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == 3:
        cuenta.consultar_saldo()
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
