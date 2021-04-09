def ord(array):
    ordered = []
    firstPosition = array[0]
    k = 0
    while (len(array) > 0):
        if(array[k] < firstPosition):
            firstPosition = array[k]
        k += 1
        if(k == len(array)):
            ordered.append(firstPosition)
            array.remove(firstPosition)
            if(array):
                firstPosition = array[0]
            k = 0
    return ordered


numeros = [[], []]
for i in range(7):
    n = int(input(f"Digite o {i + 1}o Valor: "))
    if(n % 2 == 0):
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(ord(numeros[0]))
print(ord(numeros[1]))
