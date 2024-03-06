from Persona import Persona
class Empleado(Persona):
    empleados = []  # Lista para almacenar todas las instancias de Empleado creadas

    def __init__(self, nombre, edad, genero, salario, puesto, area):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.puesto = puesto
        self.area = area
        self.proyectos = []
        Empleado.empleados.append(self)  # Agregar la instancia actual a la lista de empleados

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Salario:", self.salario)
        print("Puesto:", self.puesto)
        print("Departamento:", self.area)

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print(f"El proyecto '{proyecto}' ha sido asignado a {self.nombre}")

    def listar_proyectos(self):
        print(f"Proyectos asignados a {self.nombre}:")
        for proyecto in self.proyectos:
            print("-", proyecto)

    def aumentar_salario(self, cantidad):
        self.salario += cantidad
        print(f"El salario de {self.nombre} ha sido aumentado en {cantidad}")

    def saludar(self):
        print(f"Hola, soy {self.nombre} y trabajo en {self.area}. ¡Un placer conocerte!")

    @staticmethod
    def salario_promedio():
        total_salarios = sum(empleado.salario for empleado in Empleado.empleados)
        return total_salarios / len(Empleado.empleados)


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    genero = input("Ingrese el género del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    puesto = input("Ingrese el puesto del empleado: ")
    area = input("Ingrese el departamento del empleado: ")

    # Crear un empleado con la información ingresada por el usuario
    empleado = Empleado(nombre, edad, genero, salario, puesto, area)
    print("Información del empleado:")
    empleado.mostrar_informacion()

    # Asignar proyectos al empleado
    proyectos = input("Ingrese los proyectos asignados al empleado (separados por coma): ").split(",")
    for proyecto in proyectos:
        empleado.asignar_proyecto(proyecto.strip())

    # Mostrar los proyectos asignados al empleado
    empleado.listar_proyectos()

    # Aumentar el salario del empleado
    aumento = float(input("Ingrese el monto del aumento de salario: "))
    empleado.aumentar_salario(aumento)
    print("Nuevo salario:", empleado.salario)

    # Saludar
    empleado.saludar()

    # Calcular el salario promedio de todos los empleados
    print("Salario promedio de todos los empleados:", Empleado.salario_promedio())
