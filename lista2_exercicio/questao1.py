# Problema "notas" 

primeira_nota = input("Digite a primeira nota: ")
segunda_nota = input('Digite a segunda nota: ')

soma_notas = float(primeira_nota) + float(segunda_nota)

if soma_notas >= 60:
    print(f'NOTA FINAL = {soma_notas:.1f}')
else:
    print(f'NOTA FINAL = {soma_notas:.1f}')
    print('REPROVADO')