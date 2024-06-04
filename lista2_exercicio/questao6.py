# Problema "glicose"

medida_da_glicose = input('Digite a medida da glicose: ')

medida_da_glicose = float(medida_da_glicose)

if medida_da_glicose <= 100:
    print('Classificacao: normal')
elif medida_da_glicose > 100 and medida_da_glicose <= 140:
    print('Classificacao: elevado')
else:
    print('Classificacao: diabetes')