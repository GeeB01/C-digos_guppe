"""
Teste de velocidade com expressões geradoras

# Generators (geradores)

def nuns():
    for num in range(1, 10):
        yield num


gel = nuns()
print(gel)

# Generator expression
gel2 = (num for num in range(1, 10))
print(gel2)

"""
# Realizando o teste de velocidade
import time
# Generator
gen_inicio = time.time()
print(sum(num for num in range(100000)))
gen_tempo = time.time() - gen_inicio

# List comprehension
list_inicio = time.time()
print(sum([num for num in range(100000)]))
list_tempo = time.time() - list_inicio

print(gen_tempo)
print(list_tempo)