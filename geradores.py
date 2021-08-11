"""
Geradores

- Geradores são iterators . Nem todo iterator é um generator
- podem ser criados com funções geradoras
- funções geradoras utilizam a palavra reservado yield
- generators podem ser criados com expressoes geradoras

Diferenças entre funções e generator functions (funções geradoras)

--------------------------------------------------------------------------------
|Funções                                    |Generator Functions
--------------------------------------------------------------------------------
|utilizam return                            |utilizam yild
--------------------------------------------------------------------------------
|retornam uma vez                           |podem utilizar yild multiplas vezes
--------------------------------------------------------------------------------
|quando executada retorna um valor          |quando executada retorna um generator
--------------------------------------------------------------------------------

"""
# Exemplo de Generator Function
def conta(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta(4)
print(list(gen))