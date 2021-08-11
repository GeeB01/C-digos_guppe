"""
Decoradores - Decorators
Oque são decorators ?
- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de higher order functions
- Decorators tem uma sintaxe própria, usando '@'(Syntactic Sugar/ Açucar sintatico)
------------------------------------------------------------------------------------------------

# Decorators como funções (não recomendada / sem açucar sintatico)

def seja_educado(funcao):
    def sendo():
        print('ola bem vindo')
        funcao()
        print('tchau klkk')
    return sendo


def saudacao():
    print('gabriel')

# Teste 1


teste = seja_educado(saudacao)

teste()

# Teste 2


def raiva():
    print('EU TE ODEIO!!!!!')


teste = seja_educado(raiva)

teste()
---------------------------------------------------------------------------------------
# Decorator com syntax sugar "@"
def educado(funcao):
    def sendo_mesmo():
        print('ola')
        funcao()
        print('tchau')
    return sendo_mesmo


@educado
def algo():
    print('nome de alguem_placeholder')


algo()

"""

