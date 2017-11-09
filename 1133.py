num = [0, 0]
num[0] = int(input())
num[1] = int(input())
num = sorted(num, reverse=True)

for x in range(num[1]+1, num[0]):
    if x % 5 == 2 or x % 5 == 3:
        print(x)