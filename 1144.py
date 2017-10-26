entry = int(input())
print1 = [1, 1, 1]
print2 = [1, 2, 2]

for x in range(entry):
    print(print1[0], print1[1], print1[2])
    print(print2[0], print2[1], print2[2])
    print1[0] += 1
    print2[0] += 1
    print1[1] = print1[0]**2
    print1[2] = print1[0]*print1[1]
    print2[1] = print1[1]+1
    print2[2] = print1[2]+1