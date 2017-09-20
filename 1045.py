entry = input().split()
entry = [float(i) for i in entry]
entry.sort(reverse=True)
a, b, c = entry[0], entry[1], entry[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    exit()
if (a**2) == ((b**2) + (c**2)):
    print("TRIANGULO RETANGULO")
elif  (a**2) > ((b**2) + (c**2)):
    print("TRIANGULO OBTUSANGULO")
elif  (a**2) < ((b**2) + (c**2)):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif b == c or a == b or a == c:
    print("TRIANGULO ISOSCELES")
