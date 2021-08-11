"""
Modos de Abertura de Arquivos
'R' abre para leitura - padrão
'W' abre para escrita - sobrescreve caso o arquivo já exista
'X' abre para escrita somente se o arquivo não existir
'A' abre para escrita adicionando o conteúdo ao final do arquivo
'+' abre para o modo de atualização leitura e escrita

#Obs -> Abrindo no modo 'a' -> 'append, se o arquivo não existir sera criado, caso exista o novo conteudo
sera adicionado ao final

#Exemplo 'X'
try:
    with open('mais_um.txt', 'x') as arquivo:
        arquivo.write('teste de conteudo.\n')
except FileExistsError:
    print('arquivo ja existe')

# Exemplo 'a'
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('escreva uma fruta ou digite sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""
