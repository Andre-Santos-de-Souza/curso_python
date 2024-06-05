# Problema "aumento"

salario_pessoa = float(input('Digite o salario da pessoa: '))

if salario_pessoa <= 1000:
    porcentagem = 20
    aumento = (salario_pessoa * porcentagem) /100
    novo_salario = salario_pessoa+aumento
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print(f'Porcentagem = {porcentagem} %')
elif salario_pessoa > 1000 and salario_pessoa <= 3000:
    porcentagem = 15
    aumento = (salario_pessoa * porcentagem) /100
    novo_salario = salario_pessoa+aumento
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print(f'Porcentagem = {porcentagem} %')
elif salario_pessoa > 3000 and salario_pessoa <= 8000:
    porcentagem = 10
    aumento = (salario_pessoa * porcentagem) /100
    novo_salario = salario_pessoa+aumento
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print(f'Porcentagem = {porcentagem} %')
else:
    porcentagem = 5
    aumento = (salario_pessoa * porcentagem) /100
    novo_salario = salario_pessoa+aumento
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print(f'Porcentagem = {porcentagem} %')
    