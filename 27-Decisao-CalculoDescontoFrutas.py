# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kgsMorango = float(input("quantos kg de morango vc quer: "))
kgsMaca = float(input("quantos kg de maçã vc quer: "))
kgsTotal = kgsMorango + kgsMaca
if kgsMorango <= 5:
    valorMorango = kgsMorango * 2.5
else:
    valorMorango = kgsMorango * 2.2

if kgsMaca <= 5:
    valorMaca = kgsMaca * 1.8
else:
    valorMaca = kgsMaca * 1.5

valorTotal = valorMaca + valorMorango

if kgsTotal >= 8  or valorTotal >= 25:
    desconto = 0.1
    valorTotal = valorTotal * (1 - desconto)
    print(f"valor a ser pago: {valorTotal}")
else:
    print(f"valor a ser pago: {valorTotal}")
