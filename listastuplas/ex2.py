numbers = []
n = int(input())
i = 0
repeated = 0

while(i < n):
    numbers.append(int(input()))
    i += 1

# numbers.sort()
# Sort function feita manualmente
ordered = []
firstPosition = numbers[0]
k = 0
while (len(numbers) > 0):
    if(numbers[k] < firstPosition):
        firstPosition = numbers[k]
    k += 1
    if(k == len(numbers)):
        ordered.append(firstPosition)
        numbers.remove(firstPosition)
        if(numbers):
            firstPosition = numbers[0]
        k = 0

for j in range(len(ordered)):
    if(ordered[j] == ordered[j - 1]):
        repeated += 1
if(repeated > 0):
    print("Existe numero repetido!")
else:
    print("Nao existe numero repetido!")
