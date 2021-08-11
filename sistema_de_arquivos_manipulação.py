"""
Sistema de Arquivo - manipulação

# Descobrindo se um arquivo ou diretorio existe
#paths relativos
print(os.path.exists('texto.txt'))
print(os.path.exists('gb'))
print(os.path.exists('gb/gabriel1.py'))

#paths absolutos
print(os.path.exists('C:\\Users\\Gabriel'))

# criando arquivo
# forma 1
open('aruivo_teste.txt', 'w').close()

# forma 2
open('arquivo2.txt', 'a').close()

# forma 3
with open('arquivo3.txt', 'w') as arquivo:
    pass

# criando arquivo

os.mknod('aruivo_teste2.txt')
os.mknod('C:\\Users\\Gabriel\\PycharmProjects\\guppe\\arquivo_teste3.txt')

# criando diretorio

os.mkdir('novo')
# a função cira um diretorio se este nao existir. Caso exista, teremos FileExistsError

# criando multi diretorios
os.makedirs('outro/mais/um')
"""
import os

os.rename('frutas2.txt', 'frutas3.txt')
os.rename('outro/mais/um/teste.txt', 'outro/mais/um/teste2.txt')