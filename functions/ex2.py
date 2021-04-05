def faster (a, b, c):
    p = ""
    if(a < b and a < c):
        p = "Otavio"
    elif(b < a and b < c):
        p = "Bruno"
    elif(c < a and c < b):
        p = "Ian"
    else:
        p = "Empate"
    return p

n1, n2, n3 = [float(x) for x in input("Digite os tempos de cada nadadaor: ").split()]
print(faster(n1, n2, n3))