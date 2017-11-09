entry = int(input())
a, b, c = 1, 1, 1
for x in range(entry):
    print("%d %d %d" % (a, b, c))
    a += 1
    b = a * a
    c = a * b