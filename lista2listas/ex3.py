x = []
for i in range(10):
    x.append(int(input()))
for j in range(10):
    if(x[j] <= 0):
        x[j] = 1
    print(f"x[{j}] = {x[j]}")