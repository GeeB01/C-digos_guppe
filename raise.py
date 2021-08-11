"""
Levantando os proprios erros com raise

raise: lança exceções
Obs: o raise não é uma função, é uma palavra reservada
Para simplificar pense no raise como util para criar nossas proprias exceções e mensagens de erro.
A forma geral de utilização é:
raise TipoDoErro('Mensagem de Erro')

#Exemplo
def colore(texto, cor):
    cores = ('azul', 'vermelho', 'cinza', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma dessas {cores}')
    print(f'o texto {texto} sera impresso na cor {cor} ')


colore('gabriel', 'vermelho')

"""


