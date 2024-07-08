palavra_1 = 'abc'
palavra_2 = 'pqrst'

palavra_alternada = ''

min_len = min(len(palavra_1), len(palavra_2))

for i in range(min_len):
    palavra_alternada += palavra_1[i] + palavra_2[i]

palavra_alternada += palavra_1[min_len:] + palavra_2[min_len:]

print(palavra_alternada)