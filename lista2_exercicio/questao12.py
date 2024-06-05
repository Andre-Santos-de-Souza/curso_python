# Problema "tempo_de_jogo"

hora_inicial = int(input("Digite a hora inicial do jogo (0-23): "))
hora_final = int(input("Digite a hora final do jogo (0-23): "))

if hora_final <= hora_inicial:
    duracao = 24 - hora_inicial + hora_final
else:
    duracao = hora_final - hora_inicial

print(f"Duração do jogo: {duracao} horas")