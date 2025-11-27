N = int(input())

f = 1
while N > 1:
    f *= N
    N -= 1

print(f)
