def calc(a,b,c,h,l):
    count = 0
    if(a <= h or a <= l):
        count += 1
    if(b <= h or b <= l):
        count += 1
    if(c <= h or c <= l):
        count += 1
    if(count >= 2):
        out = "Procure por outro colchão João"
        return out
    else:
        out = "Parabéns pela compra!"
        return out


a,b,c = [int(x) for x in input().split()]
h,l = [int(x) for x in input().split()]
print(calc(a,b,c,h,l))