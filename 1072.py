n = int(input('inisira o valor de n: '))

dentro =0
fora = 0
for j in range(n):
    x = int(input('insira o numero:'))

    if x>=10 and x<=20:
        dentro +=1
    else:
     fora +=1

print(f'numeros dentro: {dentro}')    
print(f'numeros fora: {fora}') 
      