import operacion
class multipli(operacion.operacion):

    def operar(self):
        self.num1 = float(input("Ingresa el primer factor: "))
        self.num2 = float(input("Ingresa el segundo factor: "))
        self.resultado = self.num1 * self.num2
        print("Resultado: "+ str(self.resultado))