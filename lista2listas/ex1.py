while(True):
    name = input("Atleta: ")
    if(name == ""):
        break
    s = []
    highestS = 0
    lowestS = 0
    avg = 0
    for i in range(5):
        s.append(float(input(f"Salto {i + 1}: ")))
    avgList = s[:]
    for j in range(0, len(s)):
        if(highestS == 0):
            highestS = s[j]
        elif(s[j] > highestS):
            highestS = s[j]
        if(lowestS == 0):
            lowestS = s[j]
        elif(s[j] < lowestS):
            lowestS = s[j]
    avgList.remove(highestS)
    avgList.remove(lowestS)
    for k in range(0, len(avgList)):
        avg += avgList[k]
    avg = round(avg / len(avgList), 1)

    print(f"Atleta: {name}")
    print(f"Primeiro salto: {s[0]} m")
    print(f"Segundo salto: {s[1]} m")
    print(f"Terceiro salto: {s[2]} m")
    print(f"Quarto salto: {s[3]} m")
    print(f"Quinto salto: {s[4]} m")

    print(f"Melhor salto: {highestS} m")
    print(f"Pior salto: {lowestS} m")
    print(f"Media dos demais saltos: {avg} m")

    print(f"Resultado final: {avg} m")
