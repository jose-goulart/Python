i = 1
highestnumber = 0
while(i <= 100):
    n = int(input(f"Digite o {i}º inteiro: "))
    if(n > highestnumber):
        highestnumber = n
        position = i
    i+=1
print(f"{highestnumber}\n{position}º")

