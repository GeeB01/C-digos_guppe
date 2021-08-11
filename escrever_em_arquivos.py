"""
Escrevendo em arquivos

#Obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma se abrirmos um arquivo para escrita, não podemos le-lo, somente escrever nele

#obs: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional
para escrevermos dados em um arquivo apos a criação , usamos a função write()
esta função recebe uma string como parametro

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado.
Caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma todo
o conteudo no arquivo anterior é perdido

# Exemplo de escrita
with open('novotexto.txt', 'w') as arquivo:
    arquivo.write('gostei de saber que da pra escrever nos arquivos por aqui.\n')
    arquivo.write('da pra por quantas linhas quisermos\n')
    arquivo.write('agora a ultima linha')


"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('escreva uma druta ou digite sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

