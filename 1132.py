num1 = int(input())
num2 = int(input())
list = [num1, num2]
list = sorted(list)
sum = 0
for x in range(list[0], list[1]+1):
    if x % 13 != 0:
       sum += x
print(sum)
