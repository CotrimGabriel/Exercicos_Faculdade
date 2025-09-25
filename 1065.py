valores=[]

for i in range(5):
    valor = int(input('insira o numero a ser lido: '))
    valores.append(valor)

i = 0
contador = 0
for j in range(5):
    if valores[i] %2 ==0:
        contador +=1
        i += 1
        
    else: 
        i+=1
print(f'voce tem {contador} numeros pares')