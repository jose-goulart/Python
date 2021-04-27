class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangleType(self):
        if(self.a == self.b == self.c):
            print("Equilátero")
        elif(self.a != self.b != self.c):
            print("Escaleno")
        else:
            print("Isósceles")
