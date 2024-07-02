# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertou = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta['Pergunta'])
    
    for i,opcao in enumerate(pergunta['Opções']):
        print(i,')',opcao)
    try:
        res = int(input("Escolha uma opção: ")) 
        resposta_correta_id = pergunta['Opções'].index(pergunta['Resposta'])
        if res == resposta_correta_id:
            acertou +=1
            print("Acertou 👍")
            print()
        else:
            print("Errou 👎")
            print()
    except:
        print("Digite apenas números inteiros de 0 a 3.")
        print()
        
print(f'Você acertou {acertou}')
print(f'de {len(perguntas)} perguntas.')