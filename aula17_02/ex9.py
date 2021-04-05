# 9)	Desenvolva um gerador de tabuada, capaz de 
# gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# - 5 x 1 = 5
# - 5 x 2 = 10
# - ...
# - 5 x 10 = 50

num = int(input("Digite o numero que vc quer ver a tabuada: "))
result = 0
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")