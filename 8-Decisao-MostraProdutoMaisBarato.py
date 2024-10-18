# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
valorProduto1 = float(input("qual valor do primeiro produto?"))
valorProduto2 = float(input("qual valor do segundo produto?"))
valorProduto3 = float(input("qual valor do terceiro produto?"))

menorValor = min(valorProduto1, valorProduto2, valorProduto3)

print("sugiro que compre o produto que custa ", menorValor)
