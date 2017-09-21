product1 = input()
product2 = input()

product1 = product1.split(" ")
product2 = product2.split(" ")
qty1 = int(product1[1])
qty2 = int(product2[1])
value1 = float(product1[2])
value2 = float(product2[2])

total = qty1 *value1 +qty2*value2


print("VALOR A PAGAR: R$ %.2f" %total)