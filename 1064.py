positives = 0
average = 0

for x in range(6):
    entry = float(input())
    if entry > 0:
        positives += 1
        average += entry
average = average/positives
print("%d valores positivos" %(positives))
print("%.1f" %(average))