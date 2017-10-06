salario = float(input())
aliquota = 0
def calcula_roubo(salario):
    if salario <= 2000:
        aliquota = "Isento"
        print(aliquota)
    elif salario > 2000 and salario <= 3000:
        aliquota = 8
        result = (salario-2000)/100*aliquota
        print("R$ %.2f" %(result))
    elif salario > 3000 and salario <= 4500:
        aliquota = 18
        aliquotaAnterior = 80
        result = aliquotaAnterior + ((salario - 3000) / 100 * aliquota)
        print("R$ %.2f" % (result))
    elif salario > 4500:
        aliquota = 28
        aliquotaAnterior = 350
        result = aliquotaAnterior + ((salario - 4500) / 100 * aliquota)
        print("R$ %.2f" % (result))


calcula_roubo(salario)