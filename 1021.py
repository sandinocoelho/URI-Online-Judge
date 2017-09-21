# -*- coding: utf-8 -*-

valor = float(input())

valorc =  (valor - int(valor))*100

nota100r = int(valor /100)
valor = valor - nota100r*100
nota50r = int(valor /50)
valor = valor - nota50r*50
nota20r = int(valor /20)
valor = valor - nota20r*20
nota10r = int(valor /10)
valor = valor - nota10r*10
nota5r = int(valor /5)
valor = valor - nota5r*5
nota2r = int(valor /2)
valor = valor - nota2r*2

moeda1r = int(valor / 1)
valor = valor - moeda1r
moeda50c = int(valorc / 50)
valorc = valorc - moeda50c*50
moeda25c = int(valorc / 25)
valorc = valorc - moeda25c*25
moeda10c = int(valorc / 10)
valorc = valorc - moeda10c*10
moeda5c = int(valorc / 5)
valorc = valorc - moeda5c*5
moeda1c = round(valorc)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %nota100r)
print("%d nota(s) de R$ 50.00" %nota50r)
print("%d nota(s) de R$ 20.00" %nota20r)
print("%d nota(s) de R$ 10.00" %nota10r)
print("%d nota(s) de R$ 5.00" %nota5r)
print("%d nota(s) de R$ 2.00" %nota2r)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %moeda1r)
print("%d moeda(s) de R$ 0.50" %moeda50c)
print("%d moeda(s) de R$ 0.25" %moeda25c)
print("%d moeda(s) de R$ 0.10" %moeda10c)
print("%d moeda(s) de R$ 0.05" %moeda5c)
print("%d moeda(s) de R$ 0.01" %moeda1c)
