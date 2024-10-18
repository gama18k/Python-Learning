# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litrosVendidos = float(input("quantos litros vc quer: "))
tipoCombustivel = input("qual tipo vc quer? A-álcool, G-gasolina" ).upper()
precoGasolina = 2.5
precoAlcool = 1.9
precoTotal = 0

if tipoCombustivel == 'G':
    if litrosVendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    precoTotal = litrosVendidos * precoGasolina * (1 - desconto)
elif tipoCombustivel == 'A':
    if litrosVendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    precoTotal = litrosVendidos * precoAlcool * (1 - desconto)
else:
    print("tipo de combustivel invalido")

if precoTotal > 0:
    print(f"O valor a ser pago pelo cliente é: R$ {precoTotal:.2f}")
