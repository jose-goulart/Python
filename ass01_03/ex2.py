l1, l2, l3 = [int(x) for x in input(
    "Digite os 3 lados de um triangulo: ").split(" ")]

if(l1 + l2 > l3):
    if(l1 + l3 > l2):
        if(l2 + l3 > l1):
            if(l1 == l3 and l2 == l3 and l1 == l2):
                t = "Equilátero"
                print(f"É um triangulo {t}!")
            elif(l1 != l2 and l1 != l3 and l2 != l3):
                t = "Escaleno"
                print(f"É um triangulo {t}!")
            else:
                t = "Isosceles"
                print(f"É um triangulo {t}!")
        else:
            print("Não é um triangulo!")
    else:
        print("Não é um triangulo!")
else:
    print("Não é um triangulo!")
