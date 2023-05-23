dias = int(input())

anos = int(dias/365)
dias_restante = dias % 365

meses = int(dias_restante/30)
dias = dias_restante%30

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)