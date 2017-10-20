i = 0
j = 1
for x in range(3):
    for y in range(3):
        if i is float:
            print("I=%.1f J=%.1f" %(i, j))
        else:
            print("I=%d J=%d" %(i, j))
        j += 1.0
    i += 0.2
    j += 0.2
