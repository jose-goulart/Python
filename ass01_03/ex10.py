n = int(input("Nmro de bandejas que tentou carregar: "))
broke = 0
i = 1
if(1 <= n <= 100):
    while(i <= n):
        l,c = [int(x) for x in (input("Digite o num de latas e num de copos: ")).split()]
        if(l >= 0 and c <= 100):
            if(l > c):
                broke += c
        i += 1
print(f"O garcom quebrou {broke} copos")