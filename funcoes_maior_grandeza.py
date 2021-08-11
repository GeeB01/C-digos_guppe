"""
Funções de maior grandeza - Higher Order Functions - HOF

Quando uma linguagem de programação suporte HOF, indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo
criar variaveis do tipo de funções nos nosso programas

Em Python as funções são cidadãos de primeira classe - First Class Citizen
-----------------------------------------------------------------------------------
# Exemplo Definindo funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(a, b, funcao):
    return funcao(a, b)


print(calcular(10, 5, somar))
print(calcular(10, 5, diminuir))
print(calcular(10, 5, multiplicar))
print(calcular(10, 5, dividir))
-----------------------------------------------------------------------------------------
# Nested Functions
# Em Python podemos ter funções dentro de funções, que são conhecidas por Listed Functions ou Inner Functions

# Exemplo
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('oi ', 'tchau ', 'koljhgkjhfgk ', 'saaaaaaa '))
    return humor() + pessoa

print(cumprimento('sasasa'))
------------------------------------------------------------------------------------------
# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('ahahahahahah ','kkkkkkk ', 'ayayayayaya'))
    return rir


rindo = faz_me_rir()

print(rindo())
-------------------------------------------------------------------------------------------

"""

# Inner Functions (Funções Internas) podem acessar o escopo de funções externas ou funções mais externas

from random import choice


def rindo_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkkkkkk ', 'AYAYAYAY ', 'HAHAHAHAHAA '))
        return f'{risada} {pessoa}'
    return dando_risada


rir = rindo_novamente('Gabriel')

print(rir())
print(rir())
print(rir())
