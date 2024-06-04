# Problema "temperatura"
temperatura_em_qual_escala = input('Voce vai digitar a temperatura em qual escala (C/F)? ')

if temperatura_em_qual_escala == 'c' or temperatura_em_qual_escala == 'C':
    celsius = float(input('Digite a temperatura em Celsius: '))
    f =  (celsius * 9 / 5) + 32
    print(f'Temperatura equivalente em Fahrenheit: {f:.2f}')
elif temperatura_em_qual_escala == 'f' or temperatura_em_qual_escala == 'F':
    fahrenheit = input('Digite a temperatura em Fahrenheit: ')
    fahrenheit = float(fahrenheit)
    c = (fahrenheit - 32) / 9 * 5
    print(f'Temperatura equivalente em Celsius: {c:.2f}')