from inputFunction import getInput
from random import uniform

q = getInput("", int, 1, 4, 233000)

v = [int(x) for x in input("").split()]
stop = 0
while(stop == 0):
    for i in v:
        if(i == 0 or i == 1):
            stop = 1
        else:
            print("Digite 0 ou 1")
            v = [int(x) for x in input("").split()]
    # if(len(v) != q[0]):
    #         print(f"Digite {q[0]} elementos")
    #         v = [int(x) for x in input("").split()]
    # else:
    #     stop = 1
    

y = 0
n = 0
s = 0
for i in v:
    if(i == 0):
        y += 1
    else:
        n += 1

if(y > (q[0] // 2)):
    print("S")
else:
    print("N")

