from Triangulo import Triangle

a, b, c = [int(x) for x in input("Digite os 3 lados de um triângulo: ").split()]

if(((a + b) > c) or ((b + c) > a) or ((a + c) > b)):
    t1 = Triangle(a, b, c)
    t1.triangleType()
else:
    print("Não é um triangulo")
