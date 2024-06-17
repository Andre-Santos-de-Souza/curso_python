"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os
lista = []
while True:
    print("Selecione uma opção")
    escolha_opcao = input('[i]nserir [a]pagar [l]istar: ')

    if len(escolha_opcao) > 1:
        print('Digite apenas uma letra.')
        continue

    elif escolha_opcao == 'i':
        os.system('cls')
        inserir = input('Valor: ')
        lista.append(inserir)

    elif escolha_opcao == 'a':
        os.system('cls')
        try:
            apagar = int(input('Escolha o índice para apagar: '))
            del lista[apagar]
        except:
            print("O valor digitado não existe.")

    elif escolha_opcao == 'l':
        os.system('cls')
        for indice,nome in enumerate(lista):
            print(indice,nome)
        continue

    else:
        print("Escolha apenas uma das opções ([i],[a] e [l]):")
