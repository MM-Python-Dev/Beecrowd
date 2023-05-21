N = int(input())
impares = []
pares = []

for i in range(0,N):
    val = int(input())
    if val%2 == 0:
        # par
        pares.append(val)
    else:
        # impar
        impares.append(val)
pares.sort()
impares.sort()
impares.reverse()
for i in pares:
    print(i)
for i in impares:
    print(i)