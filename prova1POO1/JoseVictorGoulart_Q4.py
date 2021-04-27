# Nome: José Victor Goulart dos Santos
# Matrícula: 20200412
def calc(n, s):
    i = 0
    currentBalance = s
    lowestBalance = 0
    if((1 <= n <= 30) and (-10000 <= s <= 10000)):
        while(i < n):
            m = int(input())
            if((-10000 <= m <= 10000)):
                currentBalance += m
            if(lowestBalance == 0):
                lowestBalance = currentBalance
            elif(currentBalance < lowestBalance):
                lowestBalance = currentBalance
            i += 1
        print(f"Menor Saldo: R$ {lowestBalance},00")
        return currentBalance
n, s = [int(x) for x in input().split()]
print("Saldo Atual: R$", calc(n, s), end=",00")