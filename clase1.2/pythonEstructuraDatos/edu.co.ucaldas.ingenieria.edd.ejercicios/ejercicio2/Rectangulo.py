from FiguraGeometrica import  FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, longitud, ancho):
        self._longitud = longitud
        self._ancho = ancho

    def calcular_area(self):
        return self._longitud * self._ancho

    def calcular_perimetro(self):
        return 2 * (self._longitud + self._ancho)

    # Getters
    def get_longitud(self):
        return self._longitud

    def get_ancho(self):
        return self._ancho

    # Setters

    def set_longitud(self, longitud):
        self._longitud = longitud

    def set_ancho(self, ancho):
        self._ancho = ancho

if __name__ == "__main__":
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))

    rectangulo = Rectangulo(longitud, ancho)

    print("Área del rectángulo:", rectangulo.calcular_area())
    print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())

    nueva_longitud = float(input("Ingrese la nueva longitud del rectángulo: "))
    rectangulo.set_longitud(nueva_longitud)

    nuevo_ancho = float(input("Ingrese el nuevo ancho del rectángulo: "))
    rectangulo.set_ancho(nuevo_ancho)

    print("Nueva área del rectángulo:", rectangulo.calcular_area())
    print("Nuevo perímetro del rectángulo:", rectangulo.calcular_perimetro())
