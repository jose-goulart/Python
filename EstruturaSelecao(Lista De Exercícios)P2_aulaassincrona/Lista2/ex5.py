# 5) Escreva um programa que, para um determinado valor, 
# informe se este é positivo, negativo ou zero. 

value = int(0)

if(value < 0):
    print(f"{value} eh negativo")
elif(value > 0):
    print(f"{value} eh positivo")
else:
    print(f"Seu valor eh igual a {value}")