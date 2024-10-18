# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o número número: "))

numeros = [num1, num2, num3]
numeros.sort(reverse=True) # ordena a lista em ordem decrescente

print("numeros em ordem decrescente:", numeros)

# # outra forma de fazer:
# numeros = []

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)

# numeros.sort(reverse=True)

# print("Números em ordem decrescente:", numeros)
