highest = 0
for i in range(1, 5):
    n = int(input(f"Digite o {i}º inteiro: "))
    if(n > highest):
        highest = n
        position = i
print(f"{highest}\n{position}")