"""
Try/Except/Else/Finally

Dica de onde e quando tratar código:
TODA ENTRADA DEVE SER TRATADA
----------------------------------------
Else é executado somente se não houver erro

try:
    num = int(input('digite um númeoro'))
except ValueError:
    print('Valor invalido')
else:
    print(f'você digitou o número: {num}')
---------------------------------------------
Finally
try:
    num = int(input('digite um númeoro'))
except ValueError:
    print('Valor invalido')
else:
    print(f'você digitou o número: {num}')
finally:
    print('executando finally...')

# Obs. O bloco finally sempre é EXECUTADO, independente se houve execução ou não
# O finally geralmente é utilizado para fechar ou desalocar recursos
-----------------------------------------------------------------------

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('informe um numero:'))
try:
    num2 = int(input('informe mais um numero:'))
except ValueError:
    print('deve ser digitado um numero')

try:
    print(dividir(num1, num2))
except NameError:
    print('valor invalido')
-------------------------------------------
# Exemplo mais complexo CORRETO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor invalido'
    except ZeroDivisionError:
        return 'Não divida por zero'


num1 = input('informe um numero:')
num2 = input('informe mais um numero:')

print(dividir(num1, num2))
---------------------------------------------------
# Exemplo mais complexo SEMI-GENERICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'ocorreu um erro: {err}'


num1 = input('informe um numero:')
num2 = input('informe mais um numero:')

print(dividir(num1, num2))

"""

# Exemplo mais complexo SEMI-GENERICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'ocorreu um erro: {err}'


num1 = input('informe um numero:')
num2 = input('informe mais um numero:')

print(dividir(num1, num2))

