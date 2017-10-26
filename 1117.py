count = 0
notas = 0
while count < 2:
    entry = float(input())
    if entry >= 0 and entry <= 10:
        notas += entry
        count += 1
    else:
        print("nota invalida")
average = notas/2
print("media = %.2f" %average)