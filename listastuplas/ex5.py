x = []
y = []
temp = 0
for i in range(20):
    x.append(i)

for j in range(20):
    y.append(x[len(x) - j - 1])
    
x = y[:]
print(x)