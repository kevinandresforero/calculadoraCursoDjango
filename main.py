from suma import *
from resta import *
from division import * 

#      4=multiplicación\n 5=potenciación\n
op = int(input("\nIngrese que operación desea realizar;\n 1=suma\n 2=resta\n 3=división\n"))

if op == 1:
    s = suma()
    print(s.operar())

if op == 2:
    r = resta()
    print(r.operar())

if op == 3:
    d = division()
    d.operar()