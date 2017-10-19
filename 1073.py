entry = int(input())
if entry % 2 == 0:
  for x in range(2,entry+1,2):
    print("%d^2 = %d" %(x, x*x))
else:
  for x in range(2,entry,2):
    print("%d^2 = %d" %(x, x*x))