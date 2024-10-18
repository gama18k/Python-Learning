# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))

maiorNum = max(num1, num2, num3)
menorNum = min(num1, num2, num3)

print(f"O maior número é: ", maiorNum)
print(f"O menor número é: ", menorNum)
