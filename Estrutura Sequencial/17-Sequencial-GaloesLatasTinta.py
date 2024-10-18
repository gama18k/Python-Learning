# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
import math
metrosQuadrado = float(input("quantos metros quadrados tem a área a ser pintada? "))
valorLata = 80
litrosLata = 18
valorGalao = 25
litrosGalao = 3.6
litrosUsados = metrosQuadrado / 6
latasNecessarias = math.ceil(litrosUsados / litrosLata)
litrosRestantes = litrosUsados - (latasNecessarias * litrosLata)
galaoNecessario = math.ceil(litrosRestantes / litrosGalao)
valorTotal = (latasNecessarias * valorLata) + (galaoNecessario * valorGalao)

print(f"Quantidade de latas de tinta necessárias: {latasNecessarias}")
print(f"Quantidade de galões de tinta necessárias: {galaoNecessario}")
print(f"Preço total: R$ {valorTotal:.2f}")
