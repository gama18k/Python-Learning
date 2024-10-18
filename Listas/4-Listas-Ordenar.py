# 4. Ordenação: Dada uma lista com os números `[3, 1, 4, 1, 5, 9]`, ordene-a em ordem crescente e decrescente.
lista  = [3, 1, 4, 1, 5, 9]
crescente = sorted(lista, reverse=True)
decrescente = sorted(lista, reverse=False)
print("lista crescente:", decrescente)
print("lista decrescente:", crescente)