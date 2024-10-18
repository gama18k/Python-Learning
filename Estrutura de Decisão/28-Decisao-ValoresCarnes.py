# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.

# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoCarne = input("qual tipo de carne você deseja comprar? (1 - Filé Duplo, 2 - Alcatra, 3 - Picanha): ")
kgs = float(input("quantos kg: "))

precos = {
    "1": (4.90, 5.80),  # Filé Duplo
    "2": (5.90, 6.80),  # Alcatra
    "3": (6.90, 7.80)   # Picanha
}

if tipoCarne not in precos:
    print ("tipo de carne invalido")
else:
    if tipoCarne == '1':
        if kgs <= 5:
            valorTotal = kgs * 4.9
        else:
            valorTotal = kgs * 5.8
    if tipoCarne == '2':
        if kgs <= 5:
            valorTotal = kgs * 5.9
        else:
            valorTotal = kgs * 6.8
    if tipoCarne == '3':
        if kgs <= 5:
            valorTotal = kgs * 6.9
        else:
            valorTotal = kgs * 7.8

formaPagamento = input("Você irá pagar com cartão Tabajara? S/N: ").upper()

if formaPagamento == "S":
        desconto = valorTotal * 0.05  # 5% de desconto
        valorAPagar = valorTotal - desconto
else:
    desconto = 0
    valorAPagar = valorTotal


print("\n--- Cupom Fiscal ---")
if tipoCarne == "1":
    nomeCarne = "Filé Duplo"
elif tipoCarne == "2":
    nomeCarne = "Alcatra"
elif tipoCarne == "3":
    nomeCarne = "Picanha"
    
print(f"Tipo de carne: {nomeCarne}")
print(f"Quantidade: {kgs} kg")
print(f"Preço total: R$ {valorTotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valorAPagar:.2f}")
