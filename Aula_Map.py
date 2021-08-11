'''
Map

Com Map, fazemos mapeamento de valores para função

import math

def area(r):
    """Calcula area de um circulo com raio r"""
    return math.pi * (r ** 2)

print(area(2))

raios = [12, 2, 5.23, 345, 21]

# forma comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# forma 2 - Map
# Map é uma função que recebe dois parametros : o primeiro a função , o segundo um iteravel

areas = map(area,raios)
print(list(areas))

após utilizar map e ele zera os valores


'''

