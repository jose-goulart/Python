spentTime = int(input("Digite o tempo gasto: "))
avgSpeed = int(input("Digite a Velocidade media: "))

totalKm = spentTime * avgSpeed
totalGas = round(totalKm / 12, 3)
print(totalGas)
