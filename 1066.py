pares = 0
impares = 0
negativos = 0
positivos = 0
for x in range(5):
  entry = int(input())
  if entry % 2 == 0:
    pares += 1
  else:
    impares += 1
  if entry < 0:
    negativos += 1
  elif entry > 0:
    positivos +=1

print("%d valor(es) par(es)" %(pares))
print("%d valor(es) impar(es)" %(impares))
print("%d valor(es) positivo(s)" %(positivos))
print("%d valor(es) negativo(s)" %(negativos))