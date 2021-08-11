"""
O bloco try except: utilizamos para tratar erros que podem ocorrer no nosso código, prevenindo assim , que o
programa pare de funcionar e o usuario receba mensagens de erro inesperadas

a forma geral mais simples é
try:
    //execução problematica
except:
    //o que deve ser feito em caso de problemas
----------------------------------------------------
# Tratando um erro generico:

try:
    funcao = int('ola')
except:
    print("algo")

# Tratar erro de forma generica não é a melhor forma de tratamento de erros. O ideal é sempre tratar de forma especifica

# tratando erro de forma especifica
try:
    funcao()
except NameError:
    print('função inexistente')

# Podemos utilizar diversos tratamentos de erro de uma vez
try:
    duncao()
except TypeError as err:
    print(f'é isso q ta acontecendo: {err}')
except NameError as errb:
    print(f'é isso q ta acontecendo: {errb}')
------------------------------------------------
def pega_dic(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'erro de chave'


dic = {'nome': 'gabriel'}

print(pega_dic(dic, 'nom'))
"""



