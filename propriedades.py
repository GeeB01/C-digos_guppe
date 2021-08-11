"""
Propreidades - Properties

Em linguagens de programação como o JAVA,Ao declararmos atributos privados nas classes, costumamos criar
metodos publicos para manipulação desses atributos, esses metodos são conhecidos por getters e setters
Onde os getters retornam o valor do atributos e os Setters alteram o valor do mesmo
"""

from metodos import Lampada

class Conta(Lampada):

    contador = 0

    def __init__(self, titular, saldo, limite, cor, voltagem, luminosidade):
        super().__init__(cor, voltagem, luminosidade)
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def mostra_cor(self):
        return self._Lampada__cor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'saldo de: {self.__saldo} do cliente : {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


cli = Conta('Gabriel', 5000, 1500, 'azu', 110, 'alta')
cli2 = Conta('Gabriel', 5000, 1500, 'vermelha', 220, 'baixa')
soma = cli.saldo + cli2.saldo
print(soma)
print(cli.limite)
print(cli.mostra_cor)
cli.limite = 1000
print(cli.limite)
cli.titular = 'Jonas'
print(cli.titular)
