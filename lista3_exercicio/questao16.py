# Problema "experiencias" 

n_casos = int(input("Quantos casos de teste serão digitados? "))
quantidade_total = 0

quantidade_coelho = 0
quantidade_rato = 0
quantidade_sapo = 0

for i in range(0,n_casos):
    quantidade_cobaias = int(input('Quantidade de cobaias: '))
    tipo_cobaia = input('Tipo de cobaia (R, S ou C): ')
    
    if tipo_cobaia == 'c' or tipo_cobaia == 'C':
        quantidade_coelho += quantidade_cobaias
    elif tipo_cobaia == 'r' or tipo_cobaia == 'R':
        quantidade_rato += quantidade_cobaias
    elif tipo_cobaia == 's' or tipo_cobaia == 'S':
        quantidade_sapo += quantidade_cobaias

    quantidade_total += quantidade_cobaias

percentual_coelhos = (quantidade_coelho*100)/quantidade_total
percentual_rato = (quantidade_rato*100)/quantidade_total
percentual_sapo = (quantidade_sapo*100)/quantidade_total

print("RELATORIO FINAL:")
print(f'Total: {quantidade_total} cobaias ')
print("Tipo de coelhos:", quantidade_coelho)
print("Tipo de ratos:", quantidade_rato)
print("Tipo de sapos:", quantidade_sapo)
print(f"Percentual de coelhos: {percentual_coelhos:.2f}")
print(f"Percentual de ratos: {percentual_rato:.2f}")
print(f"Percentual de sapos: {percentual_sapo:.2f}")