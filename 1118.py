controle=1

while(controle!=2):
    controle=2
    primiera_ava = int(input('insira a avalicao numero 1: '))
    segunda_ava = int(input('insira a avalicao numero 2: '))

    if primiera_ava>10 or primiera_ava<0:
        controle+=1
    elif segunda_ava>10 or segunda_ava<0:
        controle+=1
        
    if controle>2:
        print('nota invalida')
    else:
        media = (primiera_ava+segunda_ava)/2
        print(f'{media:.2f}')
        repeticao=int(input('novo calculo? (1-sim 2-nao)'))
        if repeticao==1:
            controle+=1

    