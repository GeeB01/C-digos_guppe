"""
Objetos -> São instancias das classe, ou seja, após o mapeamento do objeto do mundo real para a sua
representação computacional, devemos poder criar quantos objetos forem necessarios.
Podemos pensar nos objetos/instancia de uma classe como variaveis do tipo definido na classe

"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

    def mostra_cor(self):
        print(self.__cor)

class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

lamp1 = Lampada('qazu', '110', 'aaa')

lamp1.mostra_cor()