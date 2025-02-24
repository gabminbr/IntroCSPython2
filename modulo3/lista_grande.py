import random


def lista_grande(n):
    list = []
    for i in range(0, n, 1):
        rand_number = random.randrange(0, 100)
        list.append(rand_number)
    return list
