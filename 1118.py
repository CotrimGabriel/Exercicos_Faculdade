repeticao = 1
controle = 1
controle_ava1 = 1
controle_ava2 = 1

while controle != 2:
    controle_ava1 = 1
    controle_ava2 = 1

    while controle_ava1 != 0:
        primiera_ava = float(input())
        if primiera_ava < 0 or primiera_ava > 10:
            print("nota invalida")
        else:
            controle_ava1 = 0

    while controle_ava2 != 0:
        segunda_ava = float(input())
        if segunda_ava < 0 or segunda_ava > 10:
            print("nota invalida")
        else:
            controle_ava2 = 0

    media = (primiera_ava + segunda_ava) / 2
    print(f"media = {media:.2f}")

    repeticao = 0
    while repeticao != 1 and repeticao != 2:
        print("novo calculo (1-sim 2-nao)")
        repeticao = int(input())

    if repeticao == 1:
        controle = 1
    else:
        controle = 2
