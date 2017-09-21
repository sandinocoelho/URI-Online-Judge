# -*- coding: utf-8 -*-

value = int(input())
money = value

note100 = 0
note50 = 0
note20 = 0
note10 = 0
note5 = 0
note2 = 0
note1 = 0

note100 = value / 100
value = value % 100
note50 = value / 50
value = value % 50
note20 = value / 20
value = value % 20
note10 = value / 10
value = value % 10
note5 = value / 5
value = value % 5
note2 = value / 2
value = value % 2
note1 = value / 1

print(money)
print("%d nota(s) de R$ 100,00" %note100)
print("%d nota(s) de R$ 50,00" %note50)
print("%d nota(s) de R$ 20,00" %note20)
print("%d nota(s) de R$ 10,00" %note10)
print("%d nota(s) de R$ 5,00" %note5)
print("%d nota(s) de R$ 2,00" %note2)
print("%d nota(s) de R$ 1,00" %note1)