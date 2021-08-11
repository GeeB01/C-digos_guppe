"""
Preservando MetaDatas com Wraps

MetaData - são dados intrínsecos em arquivo.
Wraps - são funções que envolvem elementos com diversas finalidades
------------------------------------------------------------------------------------

# Problema
def log_val(funcao):
    def logar(*args, **kwargs):
        documentacao
        print(f'essa é a documentacao {funcao.__doc__}')
        print(f'Essa é a chamada {funcao.__name__}')
        return funcao(*args, **kwargs)
    return logar

@log_val
def soma(a, b):
    #soma dois numeros
    return a + b

print(soma(12, 1))
print(soma.__name__)
print(soma.__doc__)
-----------------------------------------------------------------------------------
# Resolvendo / Utilizamos o import wraps

"""
from functools import wraps
# Problema resolvido


def log_val(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """documentacao"""
        print(f'essa é a documentacao {funcao.__doc__}')
        print(f'Essa é a chamada {funcao.__name__}')
        return funcao(*args, **kwargs)
    return logar


@log_val
def soma(a, b):
    """soma dois numeros"""
    return a + b


print(soma(12, 1))
print(soma.__name__)
print(soma.__doc__)
