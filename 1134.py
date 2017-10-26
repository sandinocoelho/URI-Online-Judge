entry = 0
alcool = 0
gasolina = 0
diesel = 0
while True:
    entry = int(input())
    if entry == 1:
        alcool += 1
    elif entry == 2:
        gasolina += 1
    elif entry == 3:
        diesel += 1
    elif entry == 4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: %d" %alcool)
print("Gasolina: %d" %gasolina)
print("Diesel: %d" %diesel)