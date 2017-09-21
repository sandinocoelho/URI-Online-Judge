entry = input()
oldSalary = float(entry)
newSalary = 0.0
percent = 0
def printSalary(oldSalary, newSalary, percent):
    print("Novo salario: %.2f" %(newSalary))
    print("Reajuste ganho: %.2f" %(newSalary-oldSalary))
    print("Em percentual: {} %" .format(percent))


def increaseSalary(oldSalary):
    if oldSalary <= 400:
        percent = 15
        difference = (oldSalary/100) * percent
        newSalary = oldSalary + difference
        printSalary(oldSalary, newSalary, percent)
    elif oldSalary > 400 and oldSalary <= 800:
        percent = 12
        difference = (oldSalary/100) * percent
        newSalary = oldSalary + difference
        printSalary(oldSalary, newSalary, percent)
    elif oldSalary > 800 and oldSalary <= 1200:
        percent = 10
        difference = (oldSalary / 100) * percent
        newSalary = oldSalary + difference
        printSalary(oldSalary, newSalary, percent)
    elif oldSalary > 1200 and oldSalary <= 2000:
        percent = 7
        difference = (oldSalary / 100) * percent
        newSalary = oldSalary + difference
        printSalary(oldSalary, newSalary, percent)
    elif oldSalary > 2000:
        percent = 4
        difference = (oldSalary / 100) * percent
        newSalary = oldSalary + difference
        printSalary(oldSalary, newSalary, percent)

increaseSalary(oldSalary)