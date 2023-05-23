segundos = int(input())

#1h - 60*60 = 3600s
horas = int(segundos/3600)
segundos_restante = segundos%3600

minutos = int(segundos_restante/60)
segundos = segundos_restante%60

print("%d:%d:%d" %(horas, minutos, segundos))