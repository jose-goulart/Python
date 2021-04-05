v = int(input())
if(v <= 50):
    n = [v]
    for i in range(1, 10):
        previous = n[i - 1]
        n.append(previous * 2)
    for j in range(10):
        if(n[j] <= 0):
            n[j] = 1
        print(f"N[{j}] = {n[j]}")
else:
    print("O primeiro valor deve ser menor ou igual a 50")
