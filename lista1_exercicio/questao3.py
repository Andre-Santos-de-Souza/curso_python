# Problema "idades"
print('Dados da primeira pessoa:')
nome_pessoa1 = input('Nome: ')
idade_pessoa1 = input('Idade: ')

print('Dados da segunda pessoa:')
nome_pessoa2 = input('Nome:')
idade_pessoa2 = input('Idade:')

media_idades = (float(idade_pessoa1)+float(idade_pessoa2))/2

print(f'A idade média de {nome_pessoa1} e {nome_pessoa2} é de {media_idades} anos')