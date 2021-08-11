"""
Em Python dividimos os atributos em 3 grupos
    - Atributos de instancia
    - Atributos de classes
    - Atributos dinamicos


# Atributos de instancia - São atributos declarados dentro do metodo construtor
OBS: metodo construtor é um metodo especial utilizado para a construção do objeto

"""
# Classe com atributos publicos


class Lampada:

    def __init__(self, cor, voltagem):
        self.cor = cor
        self.voltagem = voltagem
        self.ligada = False

# Classe com atributos privados


class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.__email)

    def mostra_senha(self):
        print(self.__senha)


lamp = Lampada('Azul', 220)
user = Acesso('kawkawk@kawkakw.com', '123123')
user.mostra_email()
user.mostra_senha()
print(lamp.cor, lamp.voltagem)

# O que significa atributos de instancia ?

# Significa que ao criarmos instancias de uma classe, todas as instancias terão estes atributos

# Atributos de classe
user1 = Acesso('awkkawk@kawkwa.com', '123111')
user2 = Acesso('Mansie@mail.com', '456888')

# Atributos de classe, são atributos que são declarados diretamente na classe, ou seja
# fora do construtor, geralmente ja inicializamos um valor e
# este valor é compartilhado entre todas as instancias da classe, ou seja ao inves de cada instancia
# da classe ter seus proprios valores como é o caso dos atributos de instancia, com os atributos de
# classe todas as instancias terão o mesmo valor para este atributo


class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('ps5', 'Console', 5000)
p2 = Produto('xone', 'Console', 2500)

print(p1.id)
print(p2.id)


# Atributos dinamicos -> Um atributo de instancia que pode ser criado em tempo de execução
# OBS: O atributo dinamico será exclusivo da instancia que o criou
p1.game = 'god of war'
del p1.nome
print(p1.__dict__)
