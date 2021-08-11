'''
# Exercicio 1
lista = []
lista.extend([1, 0, 5, -2, -5, 7])
print(lista)
soma = lista[0]+lista[1]+lista[5]
print(soma)
lista.insert(4, 100)
print(lista)
indice = 0
while indice < len(lista):
    print(lista[indice])
    indice = indice + 1

# Exercicio 2
lista = []
contador = 0
while contador < 6:
    lista.append(input("insira num"'\n'))
    contador = contador + 1
print(lista)

# Exercicio 3
conjunto1 = [10, 5, 3, 45, 64, 7, 9, 87, 100, 15]
contador = 0
conjunto2 = []
while contador < len(conjunto1):
    conjunto2.append(conjunto1[contador]**2)
    contador = contador + 1
print(conjunto2)

# Exercicio 4
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 80, 9]
valor1 = int(input("insira posição x"))
valor2 = int(input("insira posição y"))
soma = vetor[valor1] + vetor[valor2]
print(soma)

# Exercicio 5
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 80, 9]
for key, value in enumerate(vetor):
    print(key, value)


'''


