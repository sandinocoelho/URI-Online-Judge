entry = input().split()
entry = [int(i) for i in entry]
a, b = entry[0], entry[1]
entry.sort()
if b % a == 0 or a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
