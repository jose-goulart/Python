count = 0
sum = 0
lowest = 0
highest = 0
ask = "S"
while(ask == "S"):
    n = int(input("Digite um número inteiro: "))
    sum += n
    if(lowest == 0):
        lowest = n
    elif(n < lowest):
        lowest = n

    if(highest == 0):
        highest = n
    elif(n > highest):
        highest = n
    
    count += 1
    ask = input("Quer continuar digitando? ").upper()
avg = sum / count
print(f"Média entre todos: {avg}. Maior: {highest} e Menor: {lowest}")
