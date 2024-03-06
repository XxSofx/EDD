from Motor import Motor
class Coche:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)  # La instancia del motor se crea dentro del constructor de Coche

    def arrancar(self):
        print(f"Arrancando el coche {self.marca} {self.modelo}.")
        self.motor.arrancar()

# Ejemplo de uso
motor_coche = Motor("Gasolina")
coche = Coche("Toyota", "Corolla", motor_coche.tipo)
coche.arrancar()