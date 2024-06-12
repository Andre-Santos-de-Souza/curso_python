# Problema "senha_fixa"

senha = int(input('Digite a senha: '))
if senha == 2002:
    print('Acesso permitido!')

while senha != 2002:
    senha_invalida = int(input('Senha Invalida! Tente novamente: '))

    if senha_invalida == 2002:
        print('Acesso permitido!')
        break