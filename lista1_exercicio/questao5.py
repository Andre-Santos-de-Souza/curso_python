# Problema "troco"

preco_unitario = input('Preço unitário do produto: ')
quantidade_comprada = input('Quantidade comprada: ')
dinheiro_recebido = input('Dinheiro recebido: ')

mult_preco_quantidade = float(preco_unitario) * int(quantidade_comprada)

troco = float(dinheiro_recebido)-mult_preco_quantidade

print(f'TROCO = {troco:.2f}')