"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número.
"""

try:
    numero = input('Digite um número inteiro: ')
    numero = int(numero)

    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
except:
    print("Digite apenas números inteiros.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('////////////////////////////////////////////////////////')

try:
    hora = input('Digite a hora atual(0-23): ')
    hora = int(hora)

    if hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora <= 17:
        print('Boa tarde')
    elif hora > 17 and hora <= 23:
        print('Boa noite')
    else:
        print('Digite a hora de 0 ate 23.')
except:
    print("Digite apenas números inteiros.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('////////////////////////////////////////////////////////')

primeiro_nome = input("Digite o seu primeiro nome: ")

tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome > 4 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print("Digite mais de uma letra.")