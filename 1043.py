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
entrada.sort()
print(entrada)
a, b, c = entrada[0], entrada[1], entrada[2]
if b-c < a < b+c or a-c < b < a+c or a-b < c < a+b:
    print("é triangulo")