class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def semelhantes(self, triangulo):
        r1 = self.a / triangulo.a
        r2 = self.b / triangulo.b
        r3 = self.c / triangulo.c

        if(r1 == r2 and r2 == r3 and r1 == r3):
            return True
        return False