while True:
    entry = input().split()
    entry = [int(i) for i in entry]
    if entry[0] == 0 or entry[1] == 0:
        exit()
    else:
        if entry[0] > 0 and entry[1] > 0:
            print("primeiro")
        elif entry[0] < 0 and entry[1] > 0:
            print("segundo")
        elif entry[0] < 0 and entry[1] < 0:
            print("terceiro")
        elif entry[0] > 0 and entry[1] < 0:
            print("quarto")
