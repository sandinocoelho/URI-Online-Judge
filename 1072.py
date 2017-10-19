varIn = 0
varOut = 0
numX = int(input())
for x in range(numX):
    entry = int(input())
    if entry in range(10, 20):
        varIn += 1
    else:
        varOut += 1
print("%d in" % (varIn))
print("%d out" % (varOut))
