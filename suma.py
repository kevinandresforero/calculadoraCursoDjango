import operacion
class suma(operacion.operacion):
    def __init__(self):
        self.resultado = 0

    def operar(self):
        self.sumando1 = float(input("Ingresa el primer sumando: "))
        self.sumando2 = float(input("Ingresa el segundo sumando: "))
        self.resultado = self.sumando1 + self.sumando2
        print("Resultado: "+ str(self.resultado))