class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def retangulo(self):
        maior_lado = self.a
        cat1 = self.b
        cat2 = self.c
        if(self.b > maior_lado):
            maior_lado = self.b
            cat1 = self.a
        if(self.c > maior_lado):
            aux = maior_lado
            maior_lado = self.c
            cat2 = aux

        if(maior_lado ** 2 == cat1 ** 2 + cat2 ** 2):
            return True
        return False