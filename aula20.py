primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'primeiro_valor={primeiro_valor} é maior '
        f' do que o segundo_valor={segundo_valor}'
        )
elif segundo_valor > primeiro_valor:
    print(
        f'segundo_valor={segundo_valor} é maior '
        f' do que o primeiro_valor={primeiro_valor}'
        )
else:
    print(
        f'primeiro_valor={primeiro_valor} é igual '
        f' o segundo_valor={segundo_valor}'
        )
