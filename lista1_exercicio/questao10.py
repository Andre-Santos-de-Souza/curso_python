# Problema "duracao"

duracao_segundos = input('Digite a duracao em segundos: ')

hora = int(duracao_segundos)/3600
minutos = (int(duracao_segundos)%3600)//60
segundos = int(duracao_segundos)%60

print(f'{hora:.0f}:{minutos:.0f}:{segundos:.0f}')