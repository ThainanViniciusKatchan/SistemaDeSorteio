from random import SystemRandom


class Sorteio(str):
    def __init__(self):
        pass

    def random_name(lista, chave):  # Função para o sorteio do nome e a remoção do nome da lista
        random = SystemRandom()
        random.seed(10)
        random_name = random.choice(lista)
        for i in range(0, len(lista)):
            nome_sorteado = random_name[f'{chave}']
        if nome_sorteado:
            lista.remove(random_name)
        return nome_sorteado

    def Two_random_name(lista, chave):  # Função para o sorteio do nome e a remoção do nome da lista
        random = SystemRandom()
        random.seed(10)
        random_name = str
        for i in range(0, 2):
            random_name = random.choice(lista)
            break
        if random_name:
            lista.remove(random_name)
        return random_name

