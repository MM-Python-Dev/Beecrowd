total = 0
for i in range(2):
    item = input().split(" ")
    #item = [13] [2] [15.30]
    cod = int(item[0])
    qt = int(item[1])
    valor = float(item[2])
    total = total + qt*valor
print("VALOR A PAGAR: R$ %.2f" %total)