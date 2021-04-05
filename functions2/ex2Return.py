def function():
    highest = 0
    avg = 0
    i = 0
    while(i <= 4):
        score = float(input())
        i += 1
        if(score > highest):
            highest = score
        avg += score
    if(highest >= 5.75):
        print("Aprovado")
    elif(highest >= 2.75):
        print("Recuperação")
    else:
        print("Reprovado")
    avg = avg / 5
    return avg, highest

print(function())