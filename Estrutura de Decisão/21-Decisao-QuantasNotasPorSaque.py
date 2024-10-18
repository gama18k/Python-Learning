# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valorSaque = int(input("qual valor quer sacar: "))

if valorSaque < 10 or valorSaque > 600:
    print("valor inválido. deve ser entre 10 e 600.")
else:
    # calcular a quantidade de notas de 100
    notas_100 = valorSaque // 100
    # atualiza o valor do saque com o restante
    valorSaque %= 100

    notas_50 = valorSaque // 50
    valorSaque %= 50

    notas_10 = valorSaque // 10
    valorSaque %= 10

    notas_5 = valorSaque // 5
    valorSaque %= 5

    notas_1 = valorSaque // 1  # O restante será a quantidade de notas de 1

    print(f"Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de 100 reais")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de 50 reais")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de 10 reais")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de 5 reais")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de 1 real")   
