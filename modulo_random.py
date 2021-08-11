"""
Modulo random e o que são módulos

Em python, modulos nada mais são do que outros arquivos python

Modulo random possui varias funções para geração de números pseudo aleatórios

# Existem duas formas de se utilizar um modulo ou função deste

# Forma 1 - importando todo o modulo (não recomendado)

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classe e propriedades que estiverem dentro
# do modulo , ficarão disponiveis . Caso você saiba quais funções você precisa utilizar deste módulo, então esta
# não seria a forma ideal de utilização. Nós veremos uma forma melhor na forma 2

print(random.random())

# Veja que para utilizar a função random do pacote random, nós colocamos o nome do pacote e o nome da função separados
# por ponto "."

# Forma 2 - importando uma função especifica do módulo

from random import random

# No import acima, estamos falando do modulo random, importe a função random

for i in range(10):
    print(random())

# uniform() - Gerar um número pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 nunca é incluido

# randint() -> Gera valores inteiros pseudo aleatorios entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1,61), end=",") # começa em 1 e vai até 60

# choice() -> mostra um valor aleatorio entre um iteravel
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""
# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9']

print(cartas)

shuffle(cartas)

print(cartas)


