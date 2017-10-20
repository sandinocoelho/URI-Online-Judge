numList = []
for x in range(100):
    entry = int(input())
    numList.append(entry)
bigger = max(numList)
index = numList.index(bigger)
print(bigger)
print(index+1)