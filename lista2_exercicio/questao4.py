# Problema "operadora"

telefonia_cobra = 50.00
plano_minuto = 100
exceder_franquia = 2.00

minutos = input('Digite a quantidade de minutos:')

quantidade_minutos = int(minutos)

if quantidade_minutos <= plano_minuto:
    print(f'Valor a pagar: R$ {telefonia_cobra:.2f}')
elif quantidade_minutos > plano_minuto:
    subt = quantidade_minutos-plano_minuto
    valor_apagar = (subt*exceder_franquia)+telefonia_cobra
    print(f"Valor a pagar: R$ {valor_apagar:.2f}")