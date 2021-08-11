"""
Leitura de arquivos

para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa abrir

open() -> Na forma mais simples de utilização nos passamos apenas um parametro de entrada, que neste caso é
o caminho para o arquivo à ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então

# Por padrao a função open(), abre o arquivo para leitura. Este arquivo deve existir, ou entao
teremos o erro FileNotFoundError
"""

arquivo = open('pacotes.py')

print(arquivo.read())
