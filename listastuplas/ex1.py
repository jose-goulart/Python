n = int(input())
classScore = []
i = 0
avg = 0
highestScore = 0
lowestScore = 0
while(i < n):
    score = float(input())
    if(0 <= score <= 10):
        classScore.append(score)
        i += 1
    else:
        print("As notas do alunos devem estar entre 0 e 10")
lenArray = len(classScore)
for j in range(0, lenArray):
    avg += classScore[j]
    if(highestScore == 0):
        highestScore = classScore[j]
    elif(classScore[j] > highestScore):
        highestScore = classScore[j]
    if(lowestScore == 0):
        lowestScore = classScore[j]
    elif(classScore[j] < lowestScore):
        lowestScore = classScore[j]
avg = avg / lenArray
print(f"Media das notas: {avg}")
print(f"Maior nota: {highestScore}")
print(f"Menor nota: {lowestScore}")
print(f"Diff maior e menor nota: ", highestScore - lowestScore)

