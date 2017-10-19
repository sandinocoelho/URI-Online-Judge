entry = int(input())
for x in range(entry):
  num = int(input())
  if num == 0:
    print("NULL")
  elif num % 2 == 0:
    if num < 0:
      print("EVEN NEGATIVE")
    elif num > 0:
      print("EVEN POSITIVE")
  elif num % 2 != 0:
    if num < 0:
      print("ODD NEGATIVE")
    elif num > 0:
      print("ODD POSITIVE")