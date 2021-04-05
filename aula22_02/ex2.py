n = int(input("Nmro de bandejas que tentou carregar: "))
broke = 0
if(1 <= n <= 100):
    for i in range(1, n + 1):
        l,c = [int(x) for x in (input("Digite o num de latas e num de copos: ")).split()]
        if(l >= 0 and c <= 100):
            if(l > c):
                broke += c
print(f"O garcom quebrou {broke} copos")