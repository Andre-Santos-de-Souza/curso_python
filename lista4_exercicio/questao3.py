palavra = input("Digite uma palavra: ")

vogais = 0
consoante = 0

for palav in palavra.lower():
    if palav == 'a' or palav == 'e' or palav == 'i' or palav == 'o' or palav == 'u':
        vogais +=1
    else:
        consoante+=1

print(f'A palavra digitada possui {vogais} vogais')
print(f'A palavra digitada possui {consoante} consoantes')