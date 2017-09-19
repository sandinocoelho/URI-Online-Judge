table = {"1": 4, "2": 4.5, "3": 5, "4": 2, "5": 1.5}
entrada = input()
entrada = entrada.split()
total = table[entrada[0]] * float(entrada[1])
print("Total: R$ %.2f" % total)
