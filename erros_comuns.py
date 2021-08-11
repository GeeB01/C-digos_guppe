"""
Erros mais comuns no python

É importante prestar atenção e aprender a ler as saidas de error geradas pela execução do código

Os erros mais comuns :
SyntaxError : ocorre quando o python encontra um erro de syntax , ou seja , você escreveu algo que o python nao reconhece
como parte da linguagem
exemplos:
a)
def funcao:
    print('laelel')

b)
None = 1

c)
return
-----------------------------
NameError: ocorre quando uma varialvel ou função não foi definida
a)print(alguma coisa)
b)uma_funcao()
----------------------------------------
TypeError: ocorre quando uma função/operação/ação é aplicada a um tipo errado
a)print(len(4))
b)print('string' + [])
-----------------------------------------
IndexError: Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice inválido
a)lista = ['alguma coisa']
  print(lista[1])
b)lista = ['alguma coisa']
  print(lista[1][78])
-----------------------------------
ValueError: Ocorre quando uma função/operação built-in (integrada) recebe um argumento com o tipo correto
mas valor inapropriado
a)print(int('String'))
-------------------------------------
KeyError: Ocorre quando tentamos acessar um dicionario com uma chave que não existe
a)dic = {'oi': 'adeus'}
print(dic['outra_chave'])
---------------------------
AttributeError: Ocorre quando uma variavel não tem um atributo ou função
a)tupla = (12, 543, 5, 1)
print(tupla.sort())
----------------------------
IndentationError: Ocorre quando não respeitamos a indentação do python (4 espaços)
a)def funcao():
print('Algo')

b)for i in range(10):
i + 1
--------------------
Obs: Exceptions e Erros são sinonimos na programação
importante ler e prestar atenção na saída de erro.
"""
