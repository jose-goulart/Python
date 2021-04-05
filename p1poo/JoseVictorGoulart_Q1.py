# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
h, p, f, d = [int(x) for x in input().split()]
if(15 >= h >= 0 and 15 >= p >= 0 and 15 >= f >= 0):
    if(d == 1 or d == -1):
        if(h != p != f):
            if((f > h and p > f) or (f < h and h < p) or (p < h and h < f)):
                if(d == 1):
                    print("N")
                else:
                    print("S")
            else:
                if(d == 1):
                    print("S")
                else:
                    print("N")
        else:
            print("As posições do helicóptero, do policial e do fugitivo devem ser distintas")
    else:
        print("A direção deve ser 1 (sentido anti-horário) ou -1 (sentido horário)")
else:
    print("As posições do helicóptero, do policial e do fugitivo devem ser maiores ou iguais a zero, e menores ou iguais a 15")
