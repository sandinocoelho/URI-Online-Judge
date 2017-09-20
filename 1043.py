from math import fabs

#Cuidado com os negativos
#primero acha a duplicidade, depois verifica se é igual ao restante.

'''
6.0 4.0 2.0

b-c < a < b+c
a-c < b < a+c
a-b < c < a+b
'''
entrada = input().split()
#converte em float e ordena
entrada = [float(i) for i in entrada]
a, b, c = entrada[0], entrada[1], entrada[2]
if fabs(b-c) < a < b+c or fabs(a-c) < b < a+c or fabs(a-b) < c < a+b:
    perimetro = a+b+c
    print("Perimetro = %.1f" %perimetro)
else:
    area = ((a+b)*c)/2
    print("Area = %.1f" %area)