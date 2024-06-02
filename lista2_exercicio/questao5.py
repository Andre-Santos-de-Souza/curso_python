# Problema "troco_verificado" 

preco_unitario = input('Preço unitário do produto: ')
quantidade_comprada = input('Quantidade comprada: ')
dinheiro_recebido = input('Dinheiro recebido: ')

mult_preco_quantidade = float(preco_unitario) * int(quantidade_comprada)

if float(dinheiro_recebido) >= mult_preco_quantidade:
    troco = float(dinheiro_recebido) - mult_preco_quantidade
    print(f'TROCO = {troco:.2f}')
elif float(dinheiro_recebido) <= mult_preco_quantidade:
    troco = (float(dinheiro_recebido) - mult_preco_quantidade)*(-1)
    print(f'DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} REAIS')