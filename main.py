from suma import *
from resta import * 
#     3=división\n 4=multiplicación\n 5=potenciación\n
op = int(input("Ingrese que operación desea realizar; \n1=suma\n 2=resta\n"))

if op == 1:
    s = suma()
    print(s.operar())

if op == 2:
    r = resta()
    print(r.operar())

'''if op == 3:
    cu = cuadrado()
    cu.calcularArea()'''