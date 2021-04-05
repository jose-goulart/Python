score1, score2, score3 = [int(x) for x in input("Digite suas 3 notas: ").split()]

calcAvg = (score1 + score2 + score3) / 3

if(calcAvg < 5):
    print("Reprovado")
elif(calcAvg < 7):
    print("Em Recuperação")
else:
    print("Aprovado")
