# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

# le 2 numeros
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

# pergunta operação
operacao = input("qual operação vc quer realizar: ")

# realiza operações
if operacao == "+":
    resultado = num1+num2
elif operacao == "-":
    resultado = num1-num2
elif operacao == "*":
    resultado = num1*num2
elif operacao == "/":
    # se o numero de baixo for 0 não vai
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = None
        print("divisão por zero não é permitida")
# se digitar em operação algo q n seja +-/*, n funciona
else:
    resultado = None
    print("operação inválida")


if resultado is not None:
    # verifica se é decimal
    if resultado.is_integer():
        print("é inteiro")
    else:
        print("é decimal")

    # verifica se é par
    # só tem como ser par se for inteiro
    if isinstance(resultado, int):
        if resultado % 2 == 0:
            print("é par")
        else:
            print("é impar")

    # positivo ou negativo
    if resultado > 0:
        print("positivo")
    else:
        print("negativo")
