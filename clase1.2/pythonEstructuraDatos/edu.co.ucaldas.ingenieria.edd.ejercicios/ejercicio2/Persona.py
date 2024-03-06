class Persona:
    contador = 0  # Variable de clase para realizar seguimiento del número total de personas creadas

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        Persona.contador += 1  # Incrementar el contador al crear una nueva instancia de Persona

    def comer(self):
        print(self.nombre + " está comiendo.")

    def dormir(self):
        print(self.nombre + " está durmiendo.")

    def trabajar(self):
        print(self.nombre + " está trabajando.")

    def respirar(self):
        print(self.nombre + " está respirando.")

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getGenero(self):
        return self.genero

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setGenero(self, genero):
        self.genero = genero

    def mostrar_informacion(self):
        print("El nombre de la persona es:", self.nombre)
        print("La edad de la persona es:", self.edad)
        print("El genero de la persona es:", self.genero)

    def saludar(self):
        print("¡Hola! Mi nombre es", self.nombre)

if __name__ == "__main__":
    personas = []

    while True:
        opcion = input("\n¿Desea registrar una nueva persona? (S/N): ").upper()

        if opcion != "S":
            break

        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        genero = input("Ingrese el género de la persona: ")

        persona = Persona(nombre, edad, genero)
        personas.append(persona)

    print("\nTotal de personas registradas:", Persona.contador)
    print("\nInformación de las personas registradas:")
    for persona in personas:
        persona.mostrar_informacion()
