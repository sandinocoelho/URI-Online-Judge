mark = 1
soma = 0
while mark == 1:
    entry = input().split()
    entry = [int(i) for i in entry]
    entry = sorted(entry)
    for i in entry:
        if i <= 0:
            mark = 0
            break
    for x in range(entry[0], entry[1]):
        soma += x
        print(x, end=" ")
        print("Sum=%d" %soma)

