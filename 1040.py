entrada = input().split()
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])

p1, p2, p3, p4 = 2, 3, 4, 1

mediaponderada = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4))/(p1+p2+p3+p4)
if mediaponderada < 5:
    print("Media: %.1f" %mediaponderada)
    print("Aluno reprovado.")
elif mediaponderada >= 5 and mediaponderada < 7:
    print("Media: %.1f" % mediaponderada)
    print("Aluno em exame.")
    recu = float(input())
    print("Nota do exame: %.1f" % recu)
    mediafinal = (mediaponderada + recu) / 2
    if mediafinal >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" %mediafinal)
else:
    print("Media: %.1f" % mediaponderada)
    print("Aluno aprovado.")
