import operacion
class resta(operacion.operacion):

    def operar(self):
        self.resto1 = float(input("Ingresa el primer resto: "))
        self.resto2 = float(input("Ingresa el segundo resto: "))
        self.resultado = self.resto1 - self.resto2
        print("Resultado: "+ str(self.resultado))