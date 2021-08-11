"""
Herança Multipla

Herança Multipla nada mais é do que possibilidade de uma classe herdar de muiltiplas classes, fazendo com que
a classe filha herde todos os atributos e metodos de todas as classes herdadas

OBS: A herança multipla pode ser feita de duas maneiras:
    - por multi derivação direta
    - por multi derivação indireta

# Multi derivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivacao(Base1, Base2, Base3):
    pass

# Multi Derivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivacao(Base3):
    pass

OBS: Não importa se a derivação é direta ou indireta, a classe que ralizar a herança herdara todos
os atributos e metodos das super classes
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Penguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


peixe = Aquatico('PIZ')
urso = Terrestre('Cerveja')
pen = Penguim('PEN')

print(peixe.nadar())
print(peixe.cumprimentar())
print(urso.andar())
print(urso.cumprimentar())
print(pen.andar())
print(pen.nadar())
print(pen.cumprimentar())
