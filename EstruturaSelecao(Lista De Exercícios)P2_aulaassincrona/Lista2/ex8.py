# 8) Faça um programa que receba o valor do quilo de um produto e a quantidade
#  de quilos do produto consumida calculando o valor final a ser pago.

kgValue, qttKg = [float(x) for x in input("Digite a valor do quilo e a quantidade (Kg): ").split()]

total = kgValue * qttKg
print(f"O total eh de: R$ {total}") 