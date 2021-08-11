"""
Herança - Inheritance

A ideia de heranã é a de reaproveitar códigos. E tambem extender nossas classes
OBS: Com a herança à partir de uma classe existente nós extendemos outra classe que passa a herdar
atributos e metodos da classe herdada

Sobrescrita de metodo ocorre quando reescrevemos um metodo presente na super classe em classes filhas
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome} {self._Pessoa__sobrenome}'

cliente1 = Cliente('Gabriel', 'Silveira', '44730263880', '1000')
funcionario1 = Funcionario('Gabriel', 'Silveira', '44730263880', '1000')
print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print(cliente1.__dict__)