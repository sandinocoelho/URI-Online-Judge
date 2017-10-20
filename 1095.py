i=1
j=60

while True:
    if j == 0:
        print("I=%d J=%d" % (i, j))
        break
    print("I=%d J=%d" % (i, j))
    i += 3
    j -= 5
