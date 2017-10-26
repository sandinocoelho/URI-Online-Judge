password = 2002
while True:
    entry = int(input())
    if entry == password:
        print("Acesso Permitido")
        exit()
    else:
        print("Senha Invalida")