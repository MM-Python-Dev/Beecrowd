entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])

flag = 0
if b<0:
    b = -b
    flag = 1
quociente = a//b
resto = a%b
if flag:
    quociente = -quociente

print(str(quociente)+" "+str(resto))
