"""
Reduce
Obs. A partir de python 3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar essa função a partir do modulo 'functools'

para enteder o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ... an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iteravel.

reduce(função, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n resn = f(resn, an)
"""
from functools import reduce

dados = [1, 2, 12, 43, 554, 24, 76, 8, 5]

res = reduce(lambda x, y: x + y, dados)
print(res)


for n in dados:
    ac = 1
    ac = ac + n

print (res)
