def calcular_valor_por_litros(preco_por_litro, litros):
    return preco_por_litro * litros

def calcular_litros_por_valor(preco_por_litro, valor):
    return valor / preco_por_litro

def main():
    combustiveis = {
        1: ("Gasolina", 6.50),
        2: ("Etanol", 4.30),
        3: ("Diesel", 5.00)
    }

    print("Escolha o tipo de combustível:")
    for chave, (nome, preco) in combustiveis.items():
        print(f"{chave}. {nome} - R$ {preco}/litro")

    tipo_combustivel = int(input("Digite o número correspondente ao combustível desejado: "))
    if tipo_combustivel not in combustiveis:
        print("Opção inválida. Tente novamente.")
        return

    nome_combustivel, preco_por_litro = combustiveis[tipo_combustivel]

    print("Escolha o modo de abastecimento:")
    print("1. Abastecer por quantidade de litros")
    print("2. Abastecer por valor em dinheiro")
    modo_abastecimento = int(input("Digite o número correspondente ao modo de abastecimento desejado: "))

    if modo_abastecimento == 1:
        litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
        valor_total = calcular_valor_por_litros(preco_por_litro, litros)
        print(f"Você abasteceu {litros:.2f} litros de {nome_combustivel}.")
        print(f"Valor total a pagar: R$ {valor_total:.2f}")
    elif modo_abastecimento == 2:
        valor = float(input("Digite o valor em dinheiro que deseja gastar: "))
        litros = calcular_litros_por_valor(preco_por_litro, valor)
        print(f"Você abasteceu {litros:.2f} litros de {nome_combustivel}.")
        print(f"Valor total a pagar: R$ {valor:.2f}")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()