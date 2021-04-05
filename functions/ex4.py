def calc(a1, g1, a2, g2):
    rend1 = a2 / a1
    rend2 = g2 / g1
    if(rend1 > rend2):
        c = "A"
    else:
        c = "G"
    return c
a1, g1, a2, g2 = [float(x) for x in input("A p/l, G p/l, A km/l e G km/l: ").split()]
print(calc(a1, g1, a2, g2))