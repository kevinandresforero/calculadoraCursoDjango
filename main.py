from suma import * 
#    2=resta\n 3=división\n 4=multiplicación\n 5=potenciación\n
op = int(input("Ingrese que operación desea realizar; \n1=suma\n"))
print(op)
if op == 1:
    s = suma()
    s.operar()
'''
if op == 2:
    cr = circulo()
    cr.calcularArea()
if op == 3:
    cu = cuadrado()
    cu.calcularArea()'''