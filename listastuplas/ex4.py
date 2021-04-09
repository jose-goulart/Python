n = int(input("Quantos elementos vc quer na lista? "))

i = 0
x = []
y = []
while(i < n):
    elements = int(input(f"Digite o elemento {i + 1} da lista: "))
    x.append(elements)
    i += 1
k = int(input("Por qual numero vc deseja multiplicar os elementos da lista? "))

for j in x:
    y.append(k * j)
print(y)