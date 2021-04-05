def winner(n1, d1, v1, n2, d2, v2):
    t1 = d1 / v1
    t2 = d2 / v2
    if(t1 > t2):
        print(n2)
    elif(t2 > t1):
        print(n1)

n1, d1, v1 = [int(x) for x in input("Digite os dados: ").split()]
n2, d2, v2 = [int(x) for x in input("Digite os dados: ").split()]
winner(n1, d1, v1, n2, d2, v2)