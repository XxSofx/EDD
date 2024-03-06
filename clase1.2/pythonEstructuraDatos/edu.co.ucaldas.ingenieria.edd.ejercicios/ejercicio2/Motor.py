class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def arrancar(self):
        print(f"El motor {self.tipo} está arrancando.")