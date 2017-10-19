pares = 0
for x in range(5):
  entry = int(input())
  if entry % 2 == 0:
    pares += 1

print("%d valores pares" %(pares))