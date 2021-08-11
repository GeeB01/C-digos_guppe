"""
Entendendo Iterators e Iterables

Iterator -> Ele é um objeto que pode ser iterado
         -> um objeto que retorna um dado , sendo um elemento por vez, quando a função next() é chamada

Iterable -> Um objeto que irá retornar um iterator quando a função iter() for chamada

nome = 'Gabriel'
numero = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numero)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

"""

nome = 'Gabriel'


