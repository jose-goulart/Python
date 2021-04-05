# 7) Faça um programa que auxilie no caixa de um supermercado.
# Este algoritmo deve receber dois valores, o primeiro valor indica o preço de um determinado
# produto e o segundo valor indica o valor pago. A partir destas informações, seu algoritmo
# deve calcular o troco (se houver) ou solicitar quantia faltante para finalizar o pagamento.

productPrice, payedPrice = [int(x) for x in input("Digite o valor do produto e o o valor pago: ").split()]

if(payedPrice < productPrice):
    diff = productPrice - payedPrice
    print(f"Faltam R$ {diff} para fechar o valor do produto!")
elif(payedPrice > productPrice):
    diff = payedPrice - productPrice
    print(f"Seu troco eh de R$ {diff}!")
else:
    print(f"Agradecemos a preferencia!")
