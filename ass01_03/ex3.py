n = 0
n1 = 0
n2 = 0
i = 0
tot = 0
while(i <= 1):
    n = float(input("Digite a nota do aluno: "))
    if(i == 0):
        n1 = n
    else:
        n2 = n
    i += 1
avg = 0
avg = (n1 + n2)/ 2
if(9 < avg <= 10):
    c = "A"
elif(7.5 < avg <= 9):
    c = "B"
elif(6 < avg <= 7.5):
    c = "C"
elif(4 < avg <= 6):
    c = "D"
else:
    c = "E"
print(f"Media: {avg} Conceito: {c} Nota 1: {n1} Nota 2: {n2}")
