"""
Utilizando Lambdas

Conhecidas por expressoes lambdas ou simplesmente lambdas. São funções sem nome, ou seja , funções anonimas.

# função em python

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# e como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('gabriel', 'silveira'))

# Outro exemplo

autores = ['isaac asimov', 'Ray Bradbury', 'Robert seila oq', 'Arthur C. Clarke', 'Frank sei la oq', 'H.P Lovecraft']
print(autores)

autores.sort(key=lambda  sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

# função quadratica
# f(x)= a + x ** 2 + b * x + c

# definindo a função

def funcao_quadratica(a, b, c):
    return lambda x: a + x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, 5)

print(teste(2))







