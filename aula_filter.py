"""
Filter serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados usando a função mean()
media = statistics.mean(dados)

# OBS - Assim com a função map(), filter recebe dois parametros, sendo uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

"""
paises = ['', 'Brasil', 'Argentina', '', 'Japão', '', '', 'França']

print(paises)
res = filter(None, paises)
print(list(res))

# Diferença entre map() e filter() é :
# map()->recebe dois parâmetros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iteravel.
# filter()->recebe dois parâmetros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a função

