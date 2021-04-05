#Ler o preço de um produto inserido pelo teclado
productPrice = float(input('Digite o preço do produto: R$ '))

#Calcular quanto será descontado do valor do produto
#em reais
discount = 0.25 * productPrice

#Descontar do valor do produto e guardar em uma
#nova variavel o valor do produto com desconto
priceOff = productPrice - discount

#Imprimir o valor do produto com desconto
print(f'R$ {priceOff}')