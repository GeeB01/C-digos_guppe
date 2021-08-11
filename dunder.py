"""
Dunder Name e Dunder Main

Dunder Name -> __name__
Dunder Main -> __main__

EM python são utilizados dunder para criar funções, atributos, propriedades e etc, utilizando
dunder para não gerar conflito com os nomes desses elementos na programação.

# na linguagem C. temos um programa da seguinte forma:
int main(){
    return zero;
}

# em Java :
public static void main(String[] args){
}

# em Python , se executarmos um modulo python diretamente na linha de comando, internamente o python atribuira
a variavel dunder __name__ o valor __main__, indicando que este modulo é o modulo de execução principal
"""

from gb.gabriel1 import funcao

print(funcao())
