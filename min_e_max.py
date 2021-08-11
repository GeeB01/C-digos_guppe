"""
- Min() e Max()

Max() retorna o maior valor em um iteravel ou o maior de dois ou mais elementos

lista = [1, 8, 645, 99, 129, 4467]
print(max(lista))

tupla = {1, 8, 645, 99, 129, 4467}
print(max(tupla))

conjunto = {1, 8, 645, 99, 129, 4467}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 645, 'd': 99, 'e': 129, 'f': 4467}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 645, 'd': 99, 'e': 129, 'f': 4467}
print(max(dicionario.values()))

nomes = ['Arya', 'Ollivander', 'Tim', 'Dora', 'Samson']

print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

"""
musicas = [{'titulo': 'Thunderstruck', 'tocou': 3},
           {'titulo': 'Dead Skin Mask', 'tocou': 2},
           {'titulo': 'Back in Black', 'tocou': 4},
           {'titulo': 'Too old to rock n roll', 'tocou': 32}
           ]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

max = 0
min = 999999999
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
