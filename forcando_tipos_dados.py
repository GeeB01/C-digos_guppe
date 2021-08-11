"""
Forçando Tipos de Dados com Decoradores


"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo = []
            for(valor, tipo) in zip(args, tipos):
                novo.append(tipo(valor))
            return funcao(*novo, **kwargs)
        return converter
    return decorador

@ forca_tipo(str, int)
def mensagem(mens, vezes):
    for i in range(vezes):
        print(mens)


print(mensagem("ola", 10))