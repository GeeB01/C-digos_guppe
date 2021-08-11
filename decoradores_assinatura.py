"""
Decorators com diferentes assinaturas

Assinatura de uma função é representada pelo seu retorno nome e parametros de entrada

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def ordenar(principal, acompanhamento):
    return f'ola gostaria de pedir {principal} e tambem {acompanhamento} de acompanhamento'


print(ordenar(principal=input('digita'), acompanhamento=input('digita mais')))
"""

def validando(valor):
    def outro(funcao):
        def interna(*args, **kwargs):
            if args and args[0] != valor:
                return f'valor incorreto, valor diferente de {valor}'
            return funcao(*args, **kwargs)
        return interna
    return outro

@validando(15)
def soma(a, b):
    return a + b

print(soma(15, 3))
