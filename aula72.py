# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

def multiplicar(*args):
    total=1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é ímpar'
    
print(par_impar(numero))