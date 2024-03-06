from Persona import Persona

class Estudiante(Persona):
    # Constructor
    def __init__(self, nombre, edad, genero, semestre, universidad):
        super().__init__(nombre, edad, genero)
        self.semestre = semestre
        self.universidad = universidad

    # Método para mostrar información del estudiante
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("El grado del estudiante es:", self.semestre)
        print("La escuela del estudiante es:", self.universidad)

    def saludar(self):
        print(f"Hola, soy {self.nombre} y estudio en {self.universidad}. ¡Encantado de conocerte!")


if __name__ == "__main__":
    # Solicitar al usuario que ingrese los datos
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    genero = input("Ingrese el género del estudiante: ")
    semestre = input("Ingrese el semestre del estudiante: ")
    universidad = input("Ingrese la Universidad del estudiante: ")

    # Crear una instancia de Estudiante con los datos ingresados
    estudiante1 = Estudiante(nombre, edad, genero, semestre, universidad)

    # Mostrar la información del estudiante
    estudiante1.mostrar_informacion()

    estudiante1.saludar()