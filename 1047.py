hora_i, min_i, hora_f, min_f = (int(x) for x in input().split())

ini_min = hora_i*60 + min_i
fim_min = hora_f*60 + min_f

duracao = fim_min - ini_min
if duracao <= 0:
    duracao = 24*60 + duracao
minutos = duracao % 60
horas = duracao // 60
print("O JOGO DUROU "+str(horas)+" HORA(S) E "+str(minutos)+" MINUTO(S)")