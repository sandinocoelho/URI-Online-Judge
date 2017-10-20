weight1 = 2
weight2 = 3
weight3 = 5
weightedAverage = 0
tests = int(input())
for x in range(tests):
    entry = input().split()
    entry = [float(i) for i in entry]
    for j in entry:
        num = (entry[0]*weight1) + (entry[1]*weight2) + (entry[2]*weight3)
        weightedAverage = num / 10
    print("%.1f" %(weightedAverage))