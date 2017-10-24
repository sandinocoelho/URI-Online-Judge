tests = int(input())
sum = 0
for test in range(tests):
    entry = input().split()
    entry = [int(i) for i in entry]
    entry = sorted(entry)
    if entry[0] + 1 == entry[1]:
        print(0)
        continue
    for x in range(entry[0] + 1, entry[1]):
        if x % 2 != 0:
            sum += x
    print(sum)
    sum = 0

