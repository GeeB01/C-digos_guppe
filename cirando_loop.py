def meu_loop(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


lista = [1, 2, 3, 4, 5, 6]

meu_loop(lista)
