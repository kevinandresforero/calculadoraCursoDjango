from suma import *
from resta import *
from division import * 
from multipli import *
from potencia import * 

op = int(input("\nIngrese que operación desea realizar;\n 1=suma\n 2=resta\n 3=división\n 4=multiplicación\n  5=potenciación\n"))

if op == 1:
    s = suma()
    print(s.operar())

if op == 2:
    r = resta()
    print(r.operar())

if op == 3:
    d = division()
    d.operar()

if op == 4:
    d = multipli()
    d.operar()

if op == 5:
    p = potencia()
    p.operar()