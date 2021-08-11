"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissaõ.
- Permissão de leitura para ler o arquivo
- Permissão de escrita para escrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memoria
"""
# primeiro fazemos o import
from io import StringIO

mensagem = 'apenas uma simples string'

# Podemos criar um arquivo em memoria ja com uma string inserida , ou vazio, para inserismos um text depois
arquivo = StringIO(mensagem)
# arquivo = open('texto.txt, 'w')

# Agora tendo o arquivo podemos utilizar tudo oq ja sabemos
print(arquivo.read())

# Escrevendo outro texto
arquivo.write('mais um texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
