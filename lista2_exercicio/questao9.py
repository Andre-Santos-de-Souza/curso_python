# Problema "lanchonete"

try: 
    codigo_produto = int(input("Codigo do produto comprado: "))

    if codigo_produto == 1:
        quantidade = int(input('Quantidade comprada: '))
        preco_produto = 5.00
        valor_apagar = quantidade * preco_produto
        print(f'Valor a pagar: R$ {valor_apagar:.2f}')
    elif codigo_produto == 2:
        quantidade = int(input('Quantidade comprada: '))
        preco_produto = 3.50
        valor_apagar = quantidade * preco_produto
        print(f'Valor a pagar: R$ {valor_apagar:.2f}')
    elif codigo_produto == 3:
        quantidade = int(input('Quantidade comprada: '))
        preco_produto = 4.80
        valor_apagar = quantidade * preco_produto
        print(f'Valor a pagar: R$ {valor_apagar:.2f}')
    elif codigo_produto == 4:
        quantidade = int(input('Quantidade comprada: '))
        preco_produto = 8.90
        valor_apagar = quantidade * preco_produto
        print(f'Valor a pagar: R$ {valor_apagar:.2f}')
    elif codigo_produto == 5:
        quantidade = int(input('Quantidade comprada: '))
        preco_produto = 7.32
        valor_apagar = quantidade * preco_produto
        print(f'Valor a pagar: R$ {valor_apagar:.2f}')
    else:
        print('Valor inválido, digite numeros inteiros de 1 a 5.')
except:
    print('Valor inválido, o código dos produtos são de 1 a 5.')