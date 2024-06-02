# Problema "pagamento" 

nome = input('Nome: ')
valor_hora = input('Valor por hora: ')
horas_trabalhadas = input('Horas trabalhadas: ')

pagamento = float(valor_hora) * int(horas_trabalhadas)

print(f'O pagamento para {nome} deve ser {pagamento:.2f}')