c1 = []
c2 = []
count = 0
for i in range(5):
    c1.append(int(input()))
for j in range(5):
    c2.append(int(input()))
for k in range(5):
    if(c1[k] != c2[k]):
        count += 1
if(count == 5):
    print("Y")
else:
    print("N")