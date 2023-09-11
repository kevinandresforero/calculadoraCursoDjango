import operacion
class potencia(operacion.operacion):

    def operar(self):
        self.num1 = float(input("Ingresa la base: "))
        self.num2 = float(input("Ingresa el exponente: "))
        self.resultado = self.num1 **  self.num2
        print("Resultado: "+ str(self.resultado))