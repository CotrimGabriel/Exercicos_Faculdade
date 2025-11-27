X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

soma = 0
i = X

while i <= Y:
    if i % 13 != 0:
        soma += i
    i += 1

print(soma)
