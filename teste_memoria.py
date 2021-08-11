"""
Teste de memoria com generators

"""

# Função usando listas
def fibo(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a, b = b, a + b
    return num

def fibo_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

for i in fibo_gen(100):
    print(i)

