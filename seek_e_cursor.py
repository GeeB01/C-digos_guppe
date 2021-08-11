"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo

arquivo = open('texto.txt')

print(arquivo.read())

arquivo.seek(14)

print(arquivo.read())

# Readline() -> função que le o arquivo de linha em linha
print(arquivo.readline())

# Readlines() -> função que le o arquivo de linha em linha
print(arquivo.readlines())

# OBS -> Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos
fechar essa conexão. Para isso utilizamos a função close()
"""
# Abrir o arquivo
arquivo = open('texto.txt')

# trabalhar o arquivo
print(arquivo.read())

# fechando o arquivo
arquivo.close()
