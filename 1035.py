# -*- coding: utf-8 -*-

list = input().split()
a = list[0]
b = list[1]
c = list[2]
d = list[3]

if b > c and d > a and c + d > a + b:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")