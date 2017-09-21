# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

list = [a,b,c,d,e,f]
positivo = 0
for i in list:
    if i <= 0:
        continue
    else:
        positivo+=1

print("%d valores positivos" %positivo)