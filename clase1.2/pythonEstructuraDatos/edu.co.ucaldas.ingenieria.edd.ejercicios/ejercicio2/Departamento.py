from Empleado import Empleado
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self,nombre, edad, genero, salario, puesto, area):
        empleado = Empleado(nombre, edad, genero, salario, puesto, area)
        self.empleados.append(empleado)
        print(f"{nombre} ha sido contratado en el departamento {self.nombre}")

    def mostrar_empleados(self):
        print(f"Empleados del departamento {self.nombre}:")
        for empleado in self.empleados:
            print(empleado.nombre)

# Ejemplo de uso
departamento_ventas = Departamento("Ventas")
departamento_ventas.contratar_empleado("Juan", 30, "Masculino",  "120000", "Vendedor", "Ventas" )
departamento_ventas.contratar_empleado("María", 35, "Femenino", "200000", "Vendedora", "Ventas" )
departamento_ventas.mostrar_empleados()