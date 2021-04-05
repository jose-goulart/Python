# 6) Uma empresa de vendas oferece para seus clientes um desconto
# em função do valor da compra do cliente. Esse desconto é de 20%
# se o valor da compra for maior ou igual a R$ 5.000,00 e 15% se for menor.
# Faça um programa para imprimir o valor da compra, o desconto obtido por um determinado
# cliente e o valor da compra com desconto.

purchValue = float(input("Digite o valor da compra: "))

if(purchValue >= 5000):
    discount = 20
    valueOff = purchValue * ((100 - discount)/100)
    print(
        f"Valor da compra: R$ {purchValue}. Desconto: {discount}%. Valor com desconto: R$ {valueOff}")
else:
    discount = 15
    valueOff = purchValue * ((100 - discount)/100)
    print(
        f"Valor da compra: R$ {purchValue}. Desconto: {discount}%. Valor com desconto: R$ {valueOff}")
