num_anterior = 0
num_ant_anterior = 1
i = 0
while i <= 8:
    num_final = num_ant_anterior + num_anterior
    num_anterior = num_ant_anterior
    num_ant_anterior = num_final
    print(num_final)
    num_final = 0
    i += 1