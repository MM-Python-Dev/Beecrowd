tempo = int(input())
velocidade = int(input())
km_p_l = 12.0

km_gasto = tempo*velocidade

litros = km_gasto / km_p_l
print("%.3f" %litros)
