# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
inteiro1 = int(input("digite o primeiro numero inteiro: "))
inteiro2 = int(input("digite o segundo numero inteiro: "))
real1 = float(input("digite o numero real: "))

produto = (inteiro1 * 2) * (inteiro2 / 2)
soma = (inteiro1 * 3) + real1
terceiro = real1 ** 3

print("a) o produto do dobro do primeiro com metade do segundo: ", produto)
print("b) a soma do triplo do primeiro com o terceiro: ", soma)
print("c) o terceiro elevado ao cubo: ", terceiro)
