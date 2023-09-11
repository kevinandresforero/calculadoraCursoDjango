import operacion
class division(operacion.operacion):

    def operar(self):
        self.num1 = float(input("Ingresa el divisor: "))
        self.num2 = float(input("Ingresa el dividendo: "))
        self.resultado = self.num1 / self.num2
        print("Resultado: "+ str(self.resultado))