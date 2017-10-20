tests = int(input())
countC = 0
countR = 0
countS = 0
countTotal = 0
percentC = 0.0
percentR = 0.0
percentS = 0.0

for x in range(tests):
    entry = input().split(" ")
    if entry[1] == "C":
        countC += int(entry[0])
        countTotal += int(entry[0])
    elif entry[1] == "R":
        countR += int(entry[0])
        countTotal += int(entry[0])
    elif entry[1] == "S":
        countS += int(entry[0])
        countTotal += int(entry[0])

percentC = (countC*100)/float(countTotal)
percentR = (countR*100)/countTotal
percentS = (countS*100)/countTotal


print("Total: %d cobaias" %(countTotal))
print("Total de coelhos: %d" %(countC))
print("Total de ratos: %d" %(countR))
print("Total de sapos: %d" %(countS))
print("Percentual de coelhos: %.2f %%" %(percentC))
print("Percentual de ratos: %.2f %%" %(percentR))
print("Percentual de sapos: %.2f %%" %(percentS))