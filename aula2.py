# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep='-', end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-')#sep='-': Este é um argumento opcional chamado sep (abreviação de "separator", ou separador em português). Ele especifica o separador que deve ser usado entre os valores que estão sendo impressos. O valor padrão do sep é um espaço (' '), mas aqui foi alterado para um traço ('-').