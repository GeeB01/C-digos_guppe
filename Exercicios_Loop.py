# Exercicio 1
'''
for i in range(3, 18, 3):
    print(i)
'''

# Exercicio 2
'''
for i in range(1, 101):
    print(i)

num = 1
while num <= 100:
    print(num)
    num = num + 1
'''
# Exercicio 3
'''
contador = 10
while contador >= 0:
    print(contador)
    contador = contador -1
print("Fim da contagem")
'''

# Exercicio 4
'''
for i in range(0, 101000, 1000):
    print(i)
'''

# Exercicio 5
'''
conta = 1
soma = 0
while conta <= 10:
    num = float(input("insira um numero"))
    soma = soma + num
    conta = conta + 1
print(soma)
'''

# Exercicio 6
'''
conta = 1
media = 0
soma = 0
while conta <= 10:
    num = float(input("insira um numero"))
    soma = soma + num
    media = soma/conta
    conta = conta + 1
print(media)
'''

# Exercicio 7 igual o 6

# Exercicio 8
'''
maior = None
menor = None
n = int(input("insira num"))
for i in range(n):
    x = float(input("Digita num"))
    maior = maior if maior != None and maior > x else x
    menor = menor if menor != None and menor < x else x
print(f'maior numeor {maior}\nmenor numero{menor}')
'''
# Exercicio 9
'''
n = int(input("coloca num:"))
for i in range(1, n, 2):
    print(i)
'''

# Exercicio 10
'''
num = int(input("digita num"))
for i in range(0, num + 1, 2):
    print(i)
'''


