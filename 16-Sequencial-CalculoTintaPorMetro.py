# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

metrosQuadrado = float(input("quantos metros quadrados tem a área a ser pintada? "))
litrosUsados = metrosQuadrado / 3
valorLata = 80
litrosLata = 18
latasNecessarias = math.ceil(litrosUsados / litrosLata)
valorTotal = latasNecessarias * valorLata


if litrosUsados <= 18:
    print("você vai precisar de 1 lata e fica no valor de R$80")
else:
    print("você vai precisar de ",latasNecessarias, "latas e fica no valor total de R$", valorTotal)
