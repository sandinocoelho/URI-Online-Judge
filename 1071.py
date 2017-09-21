# -*- coding: utf-8 -*-

x = int(input())
y = int(input())
list = []
if x == y:
    print(0)
elif x > y:
    for i in range(y+1,x):
        if i%2 != 0:
            list.append(i)
elif y > x:
    for i in range(x+1,y):
        if i%2 != 0:
            list.append(i)
print(sum(list))
