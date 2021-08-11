"""
Metodos -> Representam os comportamentos do objeto. ou seja, as ações que este objeto pode
realizar no seu sistema.

Em Python dividimos os metodos assim como os atributos, em dois grupos:Metodos de instancia e
Metodos de classe

# Metodos de instancia
# O metodo __init__ é um metodo especial chamado de contrutor e sua funcao é contruir o objeto a partir da classe

OBS : Todo o elemento em Python que inicia e finaliza com duplo underline é chamado de dunder(double underline)
OBS : Os metodos dunder em Python são chamados de metodos magicos.
ATENCAO: Por mais que possamos criar nossas proprias funções utilizando dunder, não é aconselhado.
Python possue varios metodos com essa forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções magicas internas da linguagem, então evite ao maximo, de preferencia nunca ò faça

nome = input('Digite seu nome')
sobrenome = input('Digite seu sobre nome')
email = input('Digite seu e-mail')
senha = input('Digite uma senha')
confirma_senha = input('Confirme sua senha')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere ...')
    exit(4)

print('Usuario criado com sucesso')

senha = input('Informe senha para acesso')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'senha cripto {user._Usuario__senha}') # forma errada de se acessar


"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltegem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def ver(cls):
        print(cls)
        print(Usuario.contador)

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split("@")[0]

user = Usuario('a', 'b', 'c@a', 'd')
