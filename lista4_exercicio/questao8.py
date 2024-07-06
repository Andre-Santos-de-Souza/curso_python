try:
    def calcular_valor_final(valor_produto, forma_pagamento):
        if forma_pagamento == 1:
            valor_final = valor_produto - ((valor_produto * 15) /100)
        elif forma_pagamento == 2:
            valor_final = valor_produto - ((valor_produto * 10)/100)
        elif forma_pagamento == 3:
            valor_final = valor_produto
        elif forma_pagamento == 4:
            mais_juros_dez_porcento = (valor_produto * 10)/100
            valor_final = valor_produto + mais_juros_dez_porcento
        return valor_final


    valor_produto = float(input("Digite o valor do produto: "))
    print("1. Á vista em Dinheiro ou Pix, recebe 15% de desconto.")
    print("2. Á vista no cartão de crédito, recebe 10%")
    print("3. Parcelado no cartão em duas vezes, preço normal do produto sem juros.")
    print("4. Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%.")
    opcao_pagamento = int(input("Digite o número da sua escolha: "))

    valor_final = calcular_valor_final(valor_produto, opcao_pagamento)
    print(valor_final)
except UnboundLocalError:
    print("Opção inválida")